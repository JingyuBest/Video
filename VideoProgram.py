import cv2
import os
import Pic
import PicCombine
import OsComm
#定义输出文件架
def Program():
    path="Camera_Output"
    if not os.path.exists(path):
        os.makedirs(path)
    #定义帧数
    frame_num=0
    cap=cv2.VideoCapture("PeopleTest2.mp4")
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret,frame=cap.read()
        if not ret:
            print("Video Play Over")
            break
        cv2.imshow("Camera",frame)
        #转为灰度图像
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame_filename=os.path.join(path,"frame_"+str(frame_num)+".jpg")
        cv2.imwrite(frame_filename,gray_frame)
        print(frame_num)
        frame_num+=1
        cv2.imshow("Gray Camera",gray_frame)
        #按q键退出，waitkey中参数为等待时间，ms
        if cv2.waitKey(1)==ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    Pic.Pic()
    OsComm.OsComm()
    PicCombine.Piccom()
