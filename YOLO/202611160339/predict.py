from ultralytics import YOLO

# 注意这里改成了 train-2！
model = YOLO('runs/detect/train-2/weights/best.pt')

model.predict(source='test_images', save=True, conf=0.5)