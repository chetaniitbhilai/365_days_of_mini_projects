#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mediapipe as mp
import time


# In[3]:


# # Initialize video capture
# cap = cv2.VideoCapture(0)

# # Initialize MediaPipe Hands
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands()
# mp_draw = mp.solutions.drawing_utils

# while True:
#     # Capture frame-by-frame
#     success, img = cap.read()
#     if not success:
#         break

#     # Convert the BGR image to RGB
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     # Process the image and detect hands
#     results = hands.process(img_rgb)
#     # print(results.multi_hand_landmarks)
#     # Draw hand landmarks on the original image
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:# for a hand
        
#             mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             for id, lm in enumerate(hand_landmarks.landmark):
#             # print(id,lm) # landmark for each point given in x,y and z coordinate
#             #now we need to change it in pixel value
#                 h,w,c = img.shape
#                 cx,cy =int(lm.x*w),int(lm.y*h)
                    
                
#     # Display the resulting frame
#     cv2.imshow("Image", img)

#     # Break the loop on 'q' key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the capture and close any OpenCV windows
# cap.release()
# cv2.destroyAllWindows()


# In[ ]:


import cv2
import mediapipe as mp
import time

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=self.mode,
                                         max_num_hands=self.maxHands,
                                         min_detection_confidence=self.detectionCon,
                                         min_tracking_confidence=self.trackCon)
        self.mp_draw = mp.solutions.drawing_utils 

    def findHands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return img, self.results

    def findPosition(self, img, handNo=0, draw=True):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return landmark_list

def main():
    p_time = 0
    c_time = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        if not success:
            break

        img, results = detector.findHands(img)
        landmark_list = detector.findPosition(img)
        if len(landmark_list) != 0:
            print(landmark_list[4])  # Print the coordinates of the landmark with id 4

        # Calculate and display FPS
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()


# In[ ]:





# In[ ]:




