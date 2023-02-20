import cv2
import os

RTSP_URL = "rtsp://test.lhehs.com:32701/profile1"
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("Cannot open RTSP stream")
    exit(-1)

while cap.isOpened:
    _, frame = cap.read()
    cv2.imshow("RTSP stream", frame)

key = cv2.waitKey(1)
if "q" == ord(key):
    cap.release()
    cv2.destroyAllWindows()
