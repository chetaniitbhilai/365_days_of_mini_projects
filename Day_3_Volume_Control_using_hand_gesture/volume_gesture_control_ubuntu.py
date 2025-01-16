import hand_tracking as htm  # Import the hand tracking module
import cv2  # Import OpenCV for image processing
import time  # Import time for managing timing events
import math  # Import math for geometric calculations
import numpy as np  # Import numpy for numerical operations
import subprocess  # Import subprocess to control system commands

# Set webcam resolution
wCam , hCam = 720,640

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3,wCam)  # Set the width of the webcam frame
cap.set(4,hCam)  # Set the height of the webcam frame

# Initialize hand detector with a minimum confidence of 0.7
detector = htm.handDetector(detectionCon=0.7)

p_time = 0  # Initialize the previous time variable for FPS calculation
while True:
    success, img = cap.read()  # Capture a frame from the webcam
    if not success:  # If no frame is captured, exit the loop
        break
    # Detect hands in the image
    img, results = detector.findHands(img)
    
    # Get the positions of hand landmarks
    landmark_list = detector.findPosition(img, draw=False)
    
    if len(landmark_list) != 0:  # If landmarks are detected
        # Get the coordinates of the thumb (index 4) and the index finger (index 8)
        x1, y1 = landmark_list[4][1], landmark_list[4][2]
        x2, y2 = landmark_list[8][1], landmark_list[8][2]
        
        # Draw circles on the thumb and index finger landmarks
        cv2.circle(img, (x1, y1), 9, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 9, (255, 0, 255), cv2.FILLED)
        
        # Draw a line between the thumb and index finger
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        
        # Calculate the distance between thumb and index finger
        length = math.hypot(x2 - x1, y2 - y1)

        # Map the distance (length) to a volume range (0 to 100)
        vol = np.interp(length, [50, 250], [0, 100])
        print(vol)  # Print the calculated volume

        # Set the system volume using the 'amixer' command on Linux
        command = ["amixer", "set", "Master", f"{vol}%"]
        subprocess.run(command)  # Execute the system command to adjust volume

    # Display the image with the hand landmarks and volume control line
    cv2.imshow("Image", img)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window after exiting the loop
cap.release()
cv2.destroyAllWindows()
