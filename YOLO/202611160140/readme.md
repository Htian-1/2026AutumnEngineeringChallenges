# YOLO 目标检测项目报告

## 一、环境配置（Level 1）

- Python 3.11 / PyTorch 2.14.0+cu132 / Ultralytics 8.3.163
- GPU：RTX 5060 Laptop

## 二、数据集整理（Level 1）

- 原始数据：obstacle / cola / football
- 划分比例：70% train / 30% val，随机种子 42

## 三、数据标注（Level 2）

- 工具：LabelImg
- 类别：0 obstacle / 1 cola / 2 football

## 四、模型训练（Level 3）

- 模型：yolo11n.pt
- epochs：100
- mAP@0.5：0.899（或 0.979）

## 五、新图片推理（Level 4）

- 加载 best.pt，对 15 张新图推理

## 六、问题与解决

- conda 清华源 403 → 换源
- GitHub 下载超时 → 手动下载权重
- 标签路径不匹配 → 改 data.yaml
- shm.dll 被拦截 → 关闭智能应用控制
