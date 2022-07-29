# MEDIAPIPE AND OPENCV CODE TO DETECT POSE IN A VIDEO AND WRITE TO JSON FILE
import cv2
import mediapipe as mp
import tkinter
from tkinter import filedialog

# Used to select the video file to run pose tracking on
tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
file = filedialog.askopenfilenames()

# Mediapipe section
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(file[0])
frame = 1

f = open(file[0].split(".")[0]+"_detected_pose.txt","w")

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.4,
    model_complexity=2,
    smooth_landmarks=True) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            break

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # To save the detected landmarks in the file
        f.write(str(frame)+"\n")
        f.write(str(list(results.pose_landmarks.landmark))+"\n\n")
        frame+=1
        #print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE])

        # Draw the pose annotation on the image.
        # image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Pose', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
f.close()