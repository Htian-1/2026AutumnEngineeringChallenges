基于YOLO的机器人场景目标检测 - 工程实践

项目环境：Windows系统、无独立显卡（Intel核显）、纯CPU训练（12代i5-12450H, 16GB内存）

一、项目简介

本项目基于 Ultralytics YOLOv8n 模型，完成了对机器人场景下三类目标（obstacle、cola、football）的完整目标检测工程链路。项目涵盖了数据整理、LabelImg 数据标注、YOLO 模型训练以及新图片推理测试。在无GPU的纯CPU环境下，最终模型在验证集上的 mAP50 达到 0.91。

二、环境配置

\- 操作系统：Windows

\- 环境管理：Anaconda（Python 3.10 虚拟环境 yolo\_env）

\- 深度学习框架：PyTorch 2.14.0（CPU版）+ Ultralytics 8.4.163

\- 标注工具：LabelImg

三、数据集信息

\- 类别映射（核心配置）：本项目在标注时定义的类别索引严格如下：

&#x20; - 0: football（足球）

&#x20; - 1: obstacle（障碍物）

&#x20; - 2: cola（可乐）

\- 数据划分：总计约240张图片，按照 8:2 划分训练集（192张）与验证集（48张）。

\- 数据说明：受限于GitHub上传限制，仓库未上传原始图片，仅保留了标注生成的 .txt 标签文件（位于 dataset/labels/）以及数据配置说明文件。

四、核心工程问题与解决方案（工程实践复盘）

在零基础且无硬件支持的条件下，本次实践成功排查并解决了多个工程级Bug，具体如下：

1\. 中文路径与用户名导致的报错

&#x20;  - 现象：Windows用户名为中文，导致PyTorch和YOLO在读取文件时频繁报错。

&#x20;  - 解决：将整个项目迁移至纯英文路径 D:\\yolo\_project，并在虚拟环境中执行所有命令，彻底规避路径编码问题。

2\. 网络限制导致依赖下载失败

&#x20;  - 现象：训练时YOLO自动下载 yolov8n.pt 权重和 Arial.ttf 字体时，由于国内网络环境导致连接超时（RemoteDisconnected）。

&#x20;  - 解决：手动下载 yolov8n.pt 并放入项目根目录；手动复制系统的 arial.ttf 字体文件到 %APPDATA%\\Ultralytics 目录，绕过网络限制。

3\. 标注工具闪退

&#x20;  - 现象：在Python 3.10环境下，LabelImg打开即闪退。

&#x20;  - 解决：新建一个Python 3.9的独立虚拟环境（labelimg\_env）单独安装LabelImg，解决了兼容性闪退问题。

4\. 核心Debug：标签索引与YAML配置错位（严重误检与修复）

&#x20;  - 现象：初期训练后，模型出现严重的“指鹿为马”误检现象（将足球识别为obstacle，将可乐识别为football）。

&#x20;  - 排查：经过复盘，发现LabelImg生成的标签索引（0=football, 1=obstacle, 2=cola）与 data.yaml 中定义的类别顺序（0=obstacle, 1=cola, 2=football）不一致。

&#x20;  - 解决：修正 data.yaml 中的 names 顺序，使其与标注文件中的数字索引完全对齐。重新训练后模型彻底恢复正常，mAP50达到0.91。这让我深刻理解了“数据对齐”在计算机视觉工程中的重要性。

5\. 小样本训练的泛化能力局限

&#x20;  - 现象：在复杂背景的新场景测试中，模型容易将深色长方体误检为cola（置信度约0.8）。

&#x20;  - 反思：这是典型的过拟合现象。由于数据量较小（240张）且背景单一，模型未能学习到目标的几何本质特征，而是学到了“灰地毯+黄线+深色物体=cola”的表面特征。这为未来的优化（增加负样本、数据增强）指明了方向。

五、目录结构说明

学号/

├── README.md              # 项目说明文件

├── report.md              # 详细实验报告

├── train.py               # 模型训练脚本

├── predict.py             # 新图片推理脚本

├── data.yaml              # 数据集配置文件

├── requirements.txt       # 环境依赖列表

├── dataset/               # 数据集目录（含标签文件及说明）

│   ├── 说明.txt

│   └── labels/

├── runs/                  # 训练结果目录（含最佳模型权重）

│   └── weights/

│       └── best.pt

└── results/               # 过程记录截图（环境、标注、训练曲线、预测结果等）

六、如何运行与复现

1\. 配置环境：pip install -r requirements.txt

2\. 训练模型：python train.py

3\. 推理测试：将新图片放入 test\_images 文件夹，运行 python predict.py

