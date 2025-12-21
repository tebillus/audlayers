import cv2
from ultralytics import YOLO
import pygame
import os
import glob

# initialize yolo model
# uses nano model because it offers the fastest inference speed on cpu
model = YOLO('yolo11n.pt')

# initialize pygame mixer
# handles audio mixing because it supports multiple channels efficiently
pygame.mixer.init()

# load audio files
# supports both .wav and .mp3 files dynamically
# uses glob to find all audio files in current directory
audio_layers = []
for file in sorted(glob.glob("*.wav") + glob.glob("*.mp3")):
    audio_layers.append(pygame.mixer.Sound(file))

active_channels = []

# open default camera
# uses index 0 because this maps to the primary laptop webcam
cap = cv2.VideoCapture(0)

# frame counter
# tracks frames because detection runs only periodically to save resources
frame_count = 0
person_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # resize frame
    # reduces height to 320 pixels because lower resolution speeds up processing
    # calculates width dynamically because aspect ratio must be preserved
    height, width = frame.shape[:2]
    new_height = 320
    new_width = int((new_height / height) * width)
    frame = cv2.resize(frame, (new_width, new_height))

    # run inference every 5 frames
    # skips frames because continuous detection is unnecessary and cpu-intensive
    if frame_count % 5 == 0:
        results = model(frame, classes=0, verbose=False, device="cpu")
        # count persons
        # counts bounding boxes because this estimates crowd size without complex tracking
        person_count = len(results[0].boxes)

    # manage audio layers
    # adds channels because current count exceeds active audio layers
    while len(active_channels) < person_count and len(active_channels) < len(audio_layers):
        channel = audio_layers[len(active_channels)].play(-1)
        active_channels.append(channel)
    
    # removes channels because current count is lower than active audio layers
    while len(active_channels) > person_count:
        if active_channels:
            active_channels.pop().stop()

    # display frame
    # shows video feed because it confirms the camera is working
    cv2.imshow('feed', frame)
    
    # increment counter
    frame_count += 1

    # exit condition
    # checks for 'q' key because it provides a manual kill switch
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup resources
cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
