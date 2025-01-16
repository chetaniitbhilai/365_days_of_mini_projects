import hand_tracking as htm
import cv2
import time
import math
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize audio control for Windows
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange()  # Min and Max volume range in dB
minVol = volRange[0]
maxVol = volRange[1]

# Camera settings
wCam, hCam = 720, 640
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7)
p_time = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img, results = detector.findHands(img)
    landmark_list = detector.findPosition(img, draw=False)

    if len(landmark_list) != 0:
        x1, y1 = landmark_list[4][1], landmark_list[4][2]  # Thumb tip
        x2, y2 = landmark_list[8][1], landmark_list[8][2]  # Index finger tip

        # Draw visuals
        cv2.circle(img, (x1, y1), 9, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 9, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # Calculate distance
        length = math.hypot(x2 - x1, y2 - y1)

        # Interpolate hand range (50-250 pixels) to volume range
        vol = np.interp(length, [50, 250], [minVol, maxVol])
        volume.SetMasterVolumeLevel(vol, None)

        # Display volume percentage
        vol_percentage = np.interp(length, [50, 250], [0, 100])
        cv2.putText(img, f"Volume: {int(vol_percentage)}%", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show camera feed
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
