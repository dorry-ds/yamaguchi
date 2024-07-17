from flask import Flask, Response, jsonify, render_template, request
import cv2
import torch 
import numpy as np
import pandas as pd

# Flask 应用初始化
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
  # or yolov5m, yolov5l, yolov5x
cap = None
running = True
num_people = 0

def detect_people():
    global cap, running
    running = True
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    cap = cv2.VideoCapture(1)  # 0 是默认的摄像头设备 ID
    while running and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print(404)
            break
        
        # 图像处理与检测
        results = model(frame)
        detected_people = [x for x in results.xyxy[0].numpy() if x[5] == 0]
        num_people = len(detected_people)

        # 在图像上绘制检测框和文字
        for det in detected_people:
            x1, y1, x2, y2, conf, cls = det
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.putText(frame, 'Person', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # 显示人数
        cv2.putText(frame, f'Count: {num_people}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 将处理后的帧转换为 JPEG 格式，用于在 HTML 页面上显示
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


        # 'q'键退出
    # cap.release()
    # cv2.destroyAllWindows()

@app.route('/detect')
def detect():
    return Response(detect_people(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cameraoff', methods=['POST'])
def cameraoff():
    global running, cap
    running = False
    cap.release()
    return 'Function executed successfully!'

@app.route('/get_variable')
def get_variable():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    cap = cv2.VideoCapture(1)  # 0 是默认的摄像头设备 ID
    ret, frame = cap.read()
    results = model(frame)
    detected_people = [x for x in results.xyxy[0].numpy() if x[5] == 0]
    num_people = len(detected_people)
    cap.release()
    print(num_people)
    return jsonify(variable=num_people)

if __name__ == '__main__':
    app.run(debug=False)

