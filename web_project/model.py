import cv2
import torch 
import numpy as np
import pandas as pd


print(1)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
torch.save(model, 'yolov5s_model.pth')