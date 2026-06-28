import torch
import ultralytics
import flwr
import mlflow
import cv2
import numpy as np
import pandas as pd

print("Environment check")
print("-----------------")
print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

print("Ultralytics YOLO: OK")
print("Flower: OK")
print("MLflow:", mlflow.__version__)
print("OpenCV:", cv2.__version__)
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)