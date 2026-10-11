from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO(r"yolo11n.pt")
    model.train(
        data=r"data.yaml",
        epochs=30,
        batch=25,
        imgsz=640,
        workers=1,
        cache="ram",
        project="results",
        name="yolo11n",
    )