import cv2
import time
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np

model_path = "hand_landmarker.task"

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode


MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green



def detect_shoot(results):
    if results.hand_landmarks:
        for world_landmarks in results.hand_world_landmarks:
          up = [7,8,11,12]
          down = list(range(21))
          for point in up:
              down.remove(point)
          if all([all([world_landmarks[point].y<world_landmarks[down_point].y for down_point in down]) for point in up]):
              return True
    return False

def get_xpos(results,default_xpos=0):
    if results.hand_landmarks:
        for world_landmarks in results.hand_world_landmarks:
          return world_landmarks[8].x
    else:
      return default_xpos
        
        

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE, num_hands=1)
with HandLandmarker.create_from_options(options) as landmarker:
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        detection_result = landmarker.detect(mp_image)

        detect_shoot(detection_result)
        get_xpos(detection_result)
        #cv2.imshow("preview",annotated_image)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    cv2.destroyWindow("preview")
    vc.release()