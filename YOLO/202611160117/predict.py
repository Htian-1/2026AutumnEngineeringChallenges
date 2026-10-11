from  ultralytics import YOLO

model = YOLO(r"E:\deeplearning\ultralytics-8.3.163\runs\detect\train9\weights\best.pt")
model.predict(
    source=r"E:\deeplearning\yolo_project\dataset\images",
    save=True,
    show=False,
    save_txt=True,
   )