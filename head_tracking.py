import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

running = False

def stop():
    global running
    running = False

def run():
    global running 
    running = True

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.6, min_tracking_confidence=0.6)
    cam = cv2.VideoCapture(0)
    screen_w, screen_h = pyautogui.size()

    prev_x, prev_y = pyautogui.position()
    alpha = 0.2  # smoothing factor

    def eye_aspect_ratio(landmarks, frame_w, frame_h):
        #right eye landmarks
        top = landmarks[386]
        bottom = landmarks[374]
        left = landmarks[263]
        right = landmarks[362]

        vert_dist = abs(int(top.y * frame_h) - int(bottom.y * frame_h))
        horiz_dist = abs(int(left.x * frame_w) - int(right.x * frame_w))

        if horiz_dist == 0:
            return 0
        
        ratio = vert_dist / horiz_dist
        return ratio

    last_click_time = 0
    cooldown = 0.7 #in seconds

    while running:
        success, frame = cam.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = face_mesh.process(rgb_frame)
        frame_h, frame_w, _ = frame.shape

        if res.multi_face_landmarks:
            landmarks = res.multi_face_landmarks[0].landmark
            
            #nose tip landmark
            nose = landmarks[1]
            nose_x = int(nose.x * frame_w)
            nose_y = int(nose.y * frame_h)
            nose_coords = (nose_x,nose_y)
            cv2.circle(frame, nose_coords, 6, (0,255,0),-1)
            text = f"Nose Position: ({nose_x},{nose_y})"
            cv2.putText(frame, text, (10, frame.shape[0]-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)

            #right eye landmarks
            top = landmarks[386]
            bottom = landmarks[374]
            left = landmarks[263]
            right = landmarks[362]

            for p in [top,bottom,left,right]:
                x,y = int(p.x * frame_w), int(p.y * frame_h)
                cv2.circle(frame, (x,y), 5, (0,0,255),-1)

            screen_x = np.interp(nose.x, [0.3, 0.7], [0, screen_w])
            screen_y = np.interp(nose.y, [0.3, 0.7], [0, screen_h])

            screen_x = alpha * screen_x + (1 - alpha) * prev_x
            screen_y = alpha * screen_y + (1 - alpha) * prev_y

            if abs(screen_x - prev_x) > 3 or abs(screen_y - prev_y) > 3:
                pyautogui.moveTo(screen_x, screen_y)
                prev_x, prev_y = screen_x, screen_y

            blink_ratio_value = eye_aspect_ratio(landmarks, frame_w, frame_h)

            blink_text = f"Blink Ratio: {blink_ratio_value:.2f}"
            cv2.putText(frame, blink_text, (10, frame.shape[0]-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            current_time = time.time()
            if blink_ratio_value < 0.2 and (current_time - last_click_time > cooldown):
                pyautogui.click()
                last_click_time = current_time
        #frame with nose and eye landmarks
        cv2.imshow('AirCursor', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or not running:
            break
    cam.release()
    cv2.destroyAllWindows()