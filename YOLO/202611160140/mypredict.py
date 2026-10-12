from ultralytics import YOLO

model =YOLO(r"D:\yolo\ultralytics-8.3.163\ultralytics-8.3.163\runs\detect\train18\weights\best.pt")
model.predict(
    source=r"C:\Users\智\Desktop\images\train",
    save=True,
    show=False,
    save_txt=True,
)