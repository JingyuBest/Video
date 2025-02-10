import cv2
import os
def Piccom():
    pathSrc="runs\detect\predict"
    #pathSrc="runs\pose\predict"
    first_img_path = os.path.join(pathSrc, "equ_frame_0.jpg")
    img=cv2.imread(first_img_path)
    fps=30
    imgInfo=img.shape
    size=(imgInfo[1],imgInfo[0])
    print(size)
    fourcc=cv2.VideoWriter_fourcc(*"mp4v")
    videoWrite=cv2.VideoWriter("output.mp4",fourcc,fps,size)
    files=[f for f in os.listdir(pathSrc) if f.endswith('.jpg')]
    files.sort(key=lambda x:int(x.split('_')[-1].split('.')[0]))
    for file in files:
        file_path=os.path.join(pathSrc,file)
        img=cv2.imread(file_path)
        videoWrite.write(img)
    videoWrite.release()
    print("视频保存成功")