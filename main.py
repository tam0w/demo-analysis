import numpy as np, cv2 as cv, youtube_dl, pprint, time, easyocr, pandas as pd

youtube_url = input('Enter the video url: \n')

# https://www.youtube.com/watch?v=30kOuEWrwro

ydl_opts = {
    'format': 'bestvideo[height=720][fps<=?30]',
    'quiet': True
}

df = pd.DataFrame(columns = ['round_no','first_blood','round_outcome','win_type','side','retake','postplant','bombsite','kills'])
newroundlist = []

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    pprint.pprint(info_dict)
    video_url = info_dict['url']
    print(video_url)


cap = cv.VideoCapture(video_url)

# Read and process frames

frame_interval = 45  # Process one frame every 30 frames
frame_count = 0
buy = cv.imread(r'images\buy.png')
defe = cv.imread(r'images\defeat.png')
frame_no = 0
round_counter = 0
timer = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:
        temp = cv.matchTemplate(frame, buy, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(temp)
        print(max_val)
        if max_val > 0.4:
            print('found')
            round_counter =+ 1
            timer = 25

        defeat = cv.matchTemplate(frame, defe, cv.TM_CCOEFF_NORMED)
        min_val, def_val, min_loc, def_loc = cv.minMaxLoc(defeat)
        if def_val < 0.7:
            print(frame_count)

        # reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
        # result = reader.readtext(frame)
        # print(result)


    if cv.waitKey(5) & 0xFF == ord('q'):
        break
    timer =- 1
    frame_count += 1

print(max_val,def_val,frame_count)
cap.release()
cv.destroyAllWindows()

