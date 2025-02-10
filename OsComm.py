# import os
# def OsComm():
#     os.system('yolo predict model=./best.pt source=./Histogram')
from ultralytics import YOLO
model = YOLO('best.pt')
results = model('Histogram')
tuili_jieguo=[]
#循环遍历每一张图片
for result in results:
    #如果图片中有检测到目标
    if len(result.boxes.cls)>0:
        #循环遍历每一个目标
        for i in range(len(result.boxes.cls)):
            #获取类别id
            leibie_id=int(result.boxes.cls[i].item())
            #获取类别名称
            leibie=result.names[leibie_id]
            #获取置信度
            xiangsidu=result.boxes.conf[i].item()
            #获取物体的边界框坐标值
            zuobiao = result.boxes.xyxy[i].tolist()
            tuili_jieguo.append({
                '类别':leibie,
                '相似度':xiangsidu,
                '坐标':zuobiao
            })
if len(tuili_jieguo)>0:
    for info in tuili_jieguo:
        print(info)
else:
    print("无元素")


