import cv2
import torch
import numpy as np
import pandas as pd

cap = cv2.VideoCapture(0)  # 0 是默认的摄像头设备 ID

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print(404)
        break
        
    frame = cv2.imread('1.png')
        # 图像处理与检测
    results = model(frame)
    detected_people = [x for x in results.xyxy[0].numpy() if x[5] == 0]
    num_people = len(detected_people)

        # 在图像上绘制检测框和文字
    for det in detected_people:
        x1, y1, x2, y2, conf, cls = det
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.putText(frame, 'Person', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.putText(frame, f'Count: {num_people}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('YOLOv5 Real-time Detection', frame)
        # 显示人数
        # 将处理后的帧转换为 JPEG 格式，用于在 HTML 页面上显示
        # 'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()