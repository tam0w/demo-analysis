# import cv2
# import pafy
#
# try:
#     url = 'https://www.youtube.com/watch?v=30kOuEWrwro'
#     video = pafy.new(url)
#     best_stream = video.getbest()
# except Exception as e:
#     print(e)
#
# capture = cv2.VideoCapture()
# capture.open(best_stream.url)
import time

import cv2
import youtube_dl
import pprint

youtube_url = 'https://www.youtube.com/watch?v=30kOuEWrwro'

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': '%(id)s.%(ext)s',
    'quiet': True
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    pprint.pprint(info_dict)
    video_url = info_dict['formats'][5]['url']
    print(video_url)


capture = cv2.VideoCapture(video_url)

# Read and process frames
while True:
    ret, frame = capture.read()
    if not ret:
        break

    time.sleep(0.01)
    cv2.imshow('Video', frame)

    # Exit the loop by pressing 'q'
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

# Release resources
capture.release()
cv2.destroyAllWindows()

