#!/usr/bin/env python

# chmod +x *.py

# pip install --only-binary=:all: opencv-python

import cv2
# print(cv2.__version__)

def capture_snapshot(stream_url, output_path):
    # Open the video stream
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    # Read a frame from the video
    ret, frame = cap.read()

    if ret:
        # Save the frame as an image
        cv2.imwrite(output_path, frame)
        print(f"Snapshot taken and saved to {output_path}")
    else:
        print("Error: Could not read frame from video stream.")

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    my_url = "https://vdo.ninja/?view=cyerbvz&solo&room=photo_turntable_1_3_4_2"
    capture_snapshot(my_url, "./snapshots/pic.jpg")