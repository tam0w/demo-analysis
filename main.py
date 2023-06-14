import numpy as np, cv2 as cv, youtube_dl, pprint, time, easyocr, pandas as pd

youtube_url = input('Enter the video url: \n')

# https://www.youtube.com/watch?v=30kOuEWrwro

ydl_opts = {
    'format': 'bestvideo[height=720]',
    'quiet': True
}

df = pd.DataFrame(columns = ['round_no','first_blood','round_outcome','win_type','side','retake','postplant','bombsite','kills'])
newroundlist = []

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    # pprint.pprint(info_dict)
    video_url = info_dict['url']
    print(video_url)


cap = cv.VideoCapture(video_url)

# Read and process frames

frame_interval = 45  # Process one frame every 30 frames
frame_count = 0
buy = cv.imread(r'images\buy.png')
defe = cv.imread(r'images\defeat.png')
frame_no = 0
roundstartframe = 41

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:
        temp = cv.matchTemplate(frame, buy, cv.TM_COEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.MinMaxLoc(temp)
        if max_val > 0.6:

            frame_no =+ 1
        elif max_val < 0.6 & 0 < frame_no < 40:
            frame_no =+ 1
        else:
            frame_no = 0
            defeat = cv.matchTemplate(frame, defe, cv.TM_COEFF_NORMED)
            min_val, def_val, min_loc, def_loc = cv.MinMaxLoc(defeat)
            if def_val < 0.7:
                cv.imshow('Video', frame)

        # reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
        # result = reader.readtext(frame)
        # print(result)


    if cv.waitKey(5) & 0xFF == ord('q'):
        break

    frame_count += 1


cap.release()
cv.destroyAllWindows()

