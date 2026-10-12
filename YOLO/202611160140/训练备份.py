from ultralytics import YOLO

if __name__ == "__main__":
    model =YOLO(r"D:\yolo\ultralytics-8.3.163\ultralytics-8.3.163\runs\detect\train18\weights\best.pt")
    model.train(
        data=r"666.yaml",
        epochs=30,
        imgsz=640,
        batch=24,
        cache=False,
        workers=1,
    )