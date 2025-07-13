'''import cv2
#access &save video using mobile phone
#make sure to install opencv-python and opencv-python-headless
#use ip webcam app in mobile phone to stream video
camera="http://172.16.11.177:8080/video"
cap=cv2.VideoCapture(0)
cap.open(camera)
print("check=",cap)

fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("Video_from_mobile/output_m.mp4",fourcc,20.0,(640,480))
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        frame=cv2.resize(frame,(500,300)) 
        cv2.imshow("frame",frame)
        output.write(frame)
        if cv2.waitKey(25) & 0xFF ==ord('c'):
            break

cap.release()
output.release()
cv2.destroyAllWindows()'''

'''
# IP webcam stream URL
camera = "http://172.16.11.177:8080/video"
cap = cv2.VideoCapture(camera)

if not cap.isOpened():
    print("Failed to open camera stream.")
    exit()

# Use mp4v codec for .mp4, or XVID for .avi
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("Video_from_mobile/output_m.mp4", fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (500, 300))
        cv2.imshow("frame", frame)
        output.write(frame)
        if cv2.waitKey(25) & 0xFF == ord('c'):
            break
    else:
        print("Frame not received")
        break

cap.release()
output.release()
cv2.destroyAllWindows()
'''

#access online video without downloading
"""import pafy
url = "https://youtu.be/M2or_zdYA7g"
data= pafy.new(url)
data= data.getbest(preftype="mp4") 
cap=cv2.VideoCapture(0)
cap.open(data.url)
print("check=",cap)

#fourcc=cv2.VideoWriter_fourcc(*"XVID")
#output=cv2.VideoWriter("Video capture from mobile/output_m.mp4",fourcc,20.0,(640,480))
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        frame=cv2.resize(frame,(500,300))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        cv2.imshow("frame",frame)
        cv2.imshow("gray", gray)
        #output.write(frame)
        if cv2.waitKey(25) & 0xFF ==ord('c'):
            break

cap.release()
#output.release()
cv2.destroyAllWindows()"""

'''from yt_dlp import YoutubeDL

# Step 1: Get best video URL using yt-dlp
url = "https://youtu.be/M2or_zdYA7g"

ydl_opts = {
    'format': 'best[ext=mp4][protocol=https]',
    'quiet': True,
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    video_url = info['url']

# Step 2: Open video stream in OpenCV
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Failed to open video stream.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (500, 300))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)

        if cv2.waitKey(25) & 0xFF == ord('c'):
            break
    else:
        print("Stream ended or couldn't read frame.")
        break

cap.release()
cv2.destroyAllWindows()'''



#access online video and downloading
import cv2
from yt_dlp import YoutubeDL

url = "https://youtu.be/M2or_zdYA7g"

# Step 1: Get direct video URL
ydl_opts_stream = {
    'format': 'best[ext=mp4][protocol=https]',
    'quiet': True,
}
with YoutubeDL(ydl_opts_stream) as ydl:
    info = ydl.extract_info(url, download=False)
    video_url = info['url']

# Step 2: Play video using OpenCV
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Failed to open video stream.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (500, 300))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)

        if cv2.waitKey(25) & 0xFF == ord('c'):
            break
    else:
        print("Stream ended or couldn't read frame.")
        break

cap.release()
cv2.destroyAllWindows()

print("Now downloading the video...")
ydl_opts_download = {
    'format': 'best[ext=mp4][protocol=https]',
    'outtmpl': 'downloaded_video.%(ext)s',
}
with YoutubeDL(ydl_opts_download) as ydl:
    ydl.download([url])

print("Download complete.")
