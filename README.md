# 🎥 YouTube Streaming & Downloading with Python + OpenCV

This project shows how to **stream and process YouTube videos in real time** using `yt_dlp` and `OpenCV`, and optionally **download** them for offline use.

---

## 🔧 Features

- Stream YouTube videos directly (no pre-download)
- Real-time frame processing (e.g., grayscale, resize)
- Optional video downloading using `yt_dlp`

---

## 🛠️ Requirements

```bash
pip install opencv-python yt-dlp
🚀 Usage
Stream & Process:

from yt_dlp import YoutubeDL
import cv2

url = "https://youtu.be/M2or_zdYA7g"
with YoutubeDL({'format': 'best[ext=mp4]', 'quiet': True}) as ydl:
    info = ydl.extract_info(url, download=False)
    video_url = info['url']

cap = cv2.VideoCapture(video_url)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    if cv2.waitKey(25) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()
Download Full Video (Optional):
with YoutubeDL({'outtmpl': 'downloaded_video.mp4'}) as ydl:
    ydl.download([url])
📁 Note
📌 The downloaded video file is not included in this repo due to large file size.

🔗 GitHub
github.com/munawar123421/Image-Processing-Computer-Vision

🧑‍💻 Author
Munawar
