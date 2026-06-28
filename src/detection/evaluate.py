from ultralytics import YOLO

def evaluate():
    model = YOLO("models/best.pt")
    metrics = model.val()

    print(metrics)

if __name__ == "__main__":
    evaluate()