from ultralytics import YOLO

def train():
    model = YOLO("yolov8s.pt")

    model.train(
        data="configs/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        workers=4
    )

if __name__ == "__main__":
    train()