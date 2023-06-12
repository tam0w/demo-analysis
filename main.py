import numpy as np
import cv2 as cv
import youtube_dl
import pprint
import time

youtube_url = input('Enter the video url: \n')

# https://www.youtube.com/watch?v=30kOuEWrwro

ydl_opts = {
    'format': 'bestvideo[height=720]',
    'quiet': True
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    pprint.pprint(info_dict)
    video_url = info_dict['url']
    print(video_url)


cap = cv.VideoCapture(video_url)

# Read and process frames

frame_interval = 45  # Process one frame every 30 frames
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:
        cv.imshow('Video', frame)

    if cv.waitKey(5) & 0xFF == ord('q'):
        break


    frame_count += 1


cap.release()
cv.destroyAllWindows()

