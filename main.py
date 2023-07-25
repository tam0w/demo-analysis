# import numpy as np, cv2 as cv, youtube_dl, pprint, time, easyocr, pandas as pd, time
#
# youtube_url = input('Enter the video url: \n')
# tic = time.perf_counter()
#
# # https://www.youtube.com/watch?v=30kOuEWrwro
#
# ydl_opts = {
#     'format': 'bestvideo[height=1080]',
#     'quiet': True
# }
#
# df = pd.DataFrame(columns = ['round_no','first_blood','round_outcome','win_type','side','retake','postplant','bombsite','kills'])
# newroundlist = []
#
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     info_dict = ydl.extract_info(youtube_url, download=False)
#     # pprint.pprint(info_dict)
#     video_url = info_dict['url']
#     print(video_url)
#
#
# cap = cv.VideoCapture(video_url)
#
# # Read and process frames
# cur_frame = 1000000000000000000000000
# frame_interval = 90  # Process one frame every 90 frames
# frame_count = 0
# flag = 0
# buy = cv.imread(r'images\croppedbuytrans.png')
# defe = cv.imread(r'images\defeat.png')
# startr = cv.imread(r'images\roundstart.png')
# round_counter = 0
# buytimer = 25
#
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     if frame_count % frame_interval == 0:
#         if flag == 0:
#             temp = cv.matchTemplate(frame, buy, cv.TM_CCOEFF_NORMED)
#             min_val, max_val, min_loc, max_loc = cv.minMaxLoc(temp)
#             print(max_val,frame_count)
#             cv.imwrite(f'screenshots/frame{frame_count}.png',frame)
#
#         # if max_val > 0.8 and flag == 0:
#         #     print('found')
#         #     flag = 1
#         #     cur_frame = (60 * buytimer) + frame_count
#         #
#         # if frame_count >= cur_frame and frame_count % frame_interval == 0:
#         #
#         #     start = cv.matchTemplate(frame, startr, cv.TM_CCOEFF_NORMED)
#         #     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(temp)
#         #     print(max_val, frame_count, "round start")
#         #     cv.imwrite(f'screenshots/frame{frame_count}.png', frame)
#
#         # defeat = cv.matchTemplate(frame, defe, cv.TM_CCOEFF_NORMED)
#         # min_val, def_val, min_loc, def_loc = cv.minMaxLoc(defeat)
#         # if def_val < 0.7:
#         #     print(frame_count)
#
#         # reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
#         # result = reader.readtext(frame)
#         # print(result)
#
#
#     if cv.waitKey(5) & 0xFF == ord('q'):
#         break
#     frame_count += 1
#
# toc = time.perf_counter()
# print("Time taken for video processing:", toc-tic)
# cap.release()
# cv.destroyAllWindows()
#

import numpy as np, cv2, youtube_dl, pprint, time, easyocr, pandas as pd

youtube_url = input('Enter the video url: \n')
tic = time.perf_counter()

# https://www.youtube.com/watch?v=30kOuEWrwro

ydl_opts = {
    'format': 'bestvideo[height=1080]',
    'quiet': True
}

# df = pd.DataFrame(columns = ['round_no','first_blood','round_outcome','win_type','side','retake','postplant','bombsite','kills'])
# newroundlist = []

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    # pprint.pprint(info_dict)
    video_url = info_dict['url']
    print(video_url)

def process_frame(frame):


    print('Frame no ', frame_counter)


cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Error opening video file")
    exit()

frame_skip = 90
frame_counter = 0

while True:
    # Grab the next frame without decoding and storing it
    if not cap.grab():
        break

    frame_counter += 1

    # Check if the frame_counter is a multiple of frame_skip
    if frame_counter % frame_skip == 0:
        # Retrieve and decode the grabbed frame for processing
        ret, frame = cap.retrieve()
        if not ret:
            break

        # Process the frame
        process_frame(frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

toc = time.perf_counter()
print("Time taken for video processing:", toc-tic)
cap.release()
cv2.destroyAllWindows()