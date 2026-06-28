import mlflow

def start_run():
    mlflow.set_experiment("traffic_detection")

    with mlflow.start_run():
        print("MLflow started")

if __name__ == "__main__":
    start_run()