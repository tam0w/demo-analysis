import numpy as np, cv2 as cv, youtube_dl, pprint, time, pandas as pd, time

youtube_url = input('Enter the video url: \n')
tic = time.perf_counter()

# https://www.youtube.com/watch?v=30kOuEWrwro

ydl_opts = {
    'format': 'bestvideo[height=1080]',
    'quiet': True
}

df = pd.DataFrame(
    columns=['round_no', 'first_blood', 'round_outcome', 'win_type', 'side', 'retake', 'postplant', 'bombsite',
             'kills'])
newroundlist = []

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    # pprint.pprint(info_dict)
    video_url = info_dict['url']
    print(video_url)

cap = cv.VideoCapture(video_url)

# Read and process frames
cur_frame = 1000000000000000000000000
frame_interval = 90  # Process one frame every 90 frames
frame_count = 0
flag = 0
buy = cv.imread(r'/content/images/croppedbuytrans.png')
defe = cv.imread(r'/content/images/defeat.png')
startr = cv.imread(r'/content/images/roundstart.png')
round_no = 0
buytimer = 25

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:
        if flag == 0:
            temp = cv.matchTemplate(frame, buy, cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(temp)
            print(max_val, frame_count)
            # cv.imwrite(f'/content/screenshots/frame{frame_count}.png',frame)

        if max_val > 0.8 and flag == 0:
            print('Buy Phase.')
            flag = 1
            round_no += 1
            cur_frame = (60 * buytimer) + frame_count
            print("Current Round: ", round_no)

        if frame_count >= cur_frame and frame_count % frame_interval == 0 and flag == 1:
            flag = 0
            temp = cv.matchTemplate(frame, buy, cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(temp)
            print(max_val, frame_count, "round start")
            cv.imwrite(f'/content/screenshots/frame{frame_count}.png', frame)

        # defeat = cv.matchTemplate(frame, defe, cv.TM_CCOEFF_NORMED)
        # min_val, def_val, min_loc, def_loc = cv.minMaxLoc(defeat)
        # if def_val < 0.7:
        #     print(frame_count)

        # reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
        # result = reader.readtext(frame)
        # print(result)

    if cv.waitKey(5) & 0xFF == ord('q'):
        break
    frame_count += 1

toc = time.perf_counter()
print("Time taken for video processing:", toc - tic)
cap.release()
cv.destroyAllWindows()

