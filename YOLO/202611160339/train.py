from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# 数据变多了，epochs 提升到 100，imgsz 提升到 416（更清晰）
model.train(data='D:/yolo_project/data.yaml', epochs=100, imgsz=416, device='cpu')