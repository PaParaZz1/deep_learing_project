# YOLOv2 in keras with mobilenet backend

### 1.编辑配置文件（目前文件名为config1.json）

​		“architecture”: "MobileNet"

​               "labels": ["car","bus"] (可以更改类别名从而更改输出类别)

   		编辑好对应的图片和标签文件夹目录

​                batch_size过大会爆显存，目前16最好

​		“debug” 为true时需要在用户目录下建立log文件夹

### 2.生成个人数据的anchor boxes

`python gen_anchors.py -c config.json`

运行结束之后会显示聚类百分比和对应生成的5个anchor box，将数值复制到json文件中即可。在gen_anchors.py中可以修改anchor 数量，但会与目前的已有训练权重冲突，所以更改之后需要重新开始训练。

### 3. 训练模型

（1）warmup阶段

将json文件中 “pretrained_weights" 设置为 ""

将"saved_weights_name"设置为自定义的权重文件名

将"warmup_epochs"设置为3-5（一般为3）

（2）正式训练阶段，

将"warmup_epochs"设置为0

将json文件中 “pretrained_weights" 设置为 warmup阶段生成的.h5文件名

将"saved_weights_name"设置为最终训练权重文件名



目前生成的权重名为best_video310.h5

两个阶段的命令相同，皆为

`python train.py -c config.json`

### 4. 预测阶段

`python predict.py -c config.json -w 权重文件路径及文件名 -i 预测的视频或图片路径及文件名`

最终在对应目录下生成带_detected后缀的文件

目前结合车牌检测的预测文件为predict1.py

同时在yolo目录下生成抓拍到的车辆图片，以及数据库文件db.db

