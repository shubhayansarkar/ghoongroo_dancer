import cv2
import time
import mediapipe as mp
import cvzone
import numpy as np


mp_pose=mp.solutions.pose
pose_object=mp_pose.Pose()
mp_draw=mp.solutions.drawing_utils
file=r'E:\jupyter_notebook\jupy\projects_22\computer_vision\pose_estimator\files\Ghungroo - James Combo Marino - Hrithik Roshan - War.mp4'
vid= cv2.VideoCapture(file)
sunglass=cv2.imread(r'E:\jupyter_notebook\jupy\projects_22\computer_vision\pose_estimator\files\Sunglasses-High-Quality-PNG.png',cv2.IMREAD_UNCHANGED)
smile=cv2.imread(r'E:\jupyter_notebook\jupy\projects_22\computer_vision\pose_estimator\files\smile-png-46512.png',cv2.IMREAD_UNCHANGED)
vest=cv2.imread(r'E:\jupyter_notebook\jupy\projects_22\computer_vision\pose_estimator\files\pngwing.com.png',cv2.IMREAD_UNCHANGED)
cap=cv2.imread(r'E:\jupyter_notebook\jupy\projects_22\computer_vision\pose_estimator\files\pngegg.png',cv2.IMREAD_UNCHANGED)
smile=cv2.resize(smile,(70,20))
vest=cv2.resize(vest,(120,180))
cap=cv2.resize(cap,(120,90))
# cv2.imshow('smile',parts)
sunglass=cv2.resize(sunglass,(120,30))
ptime=0
while True:

    _,frame=vid.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=pose_object.process(frame)


    if results.pose_landmarks:
        # mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        ids=[0,1,2,3,4,5,6,7,8,9,10]
        for id,lm in enumerate(results.pose_landmarks.landmark):
            bodyx,bodyy = [],[]
            h,w,c=frame.shape
            px,py=int(lm.x*w),int(lm.y*h)
            if id in ids:
                if id==5:
                    cv2.circle(frame,(px+350,py-25),45,(0,255,255),cv2.FILLED)
                    frame=cvzone.overlayPNG(frame,sunglass,[px+290,py-50])
                    frame = cvzone.overlayPNG(frame, smile, [px + 315, py-10 ])
                    # frame = cvzone.overlayPNG(frame, vest, [px + 290, py+30 ])
                    frame = cvzone.overlayPNG(frame, cap, [px + 290, py-120 ])

                else:pass
            elif id==20:
                cv2.circle(frame, (px + 350, py ), 15, (0,0,255), cv2.FILLED)
            elif id == 21:
                cv2.circle(frame, (px + 350, py), 15, (0,0,255), cv2.FILLED)

            else:
                # startpoint=
                # print(px[0],py[0])
                cv2.circle(frame,(px+350,py),12,(255,255,255),cv2.FILLED)
                # frame = cvzone.overlayPNG(frame, parts, [px + 270, py + 20])
                # cv2.rectangle(frame,(500,600),(900,800) (0,255,0), -1)


    cv2.imshow('framee',frame)
    if cv2.waitKey(1)==ord('q'):
        cv2.release()
