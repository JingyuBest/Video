#encoding:utf-8
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
def Pic():
    pathSrc="Camera_Output"
    pathResult="Histogram"
    if not os.path.exists(pathResult):
        os.makedirs(pathResult)
    images_files=[f for f in os.listdir(pathSrc) if f.endswith('.jpg')]
    if not images_files:
        print("No images files found")
        exit()
    for image_file in images_files:
        img_path=os.path.join(pathSrc,image_file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        equ = cv2.equalizeHist(img)
        output_path=os.path.join(pathResult,f"equ_{image_file}")
        cv2.imwrite(output_path,equ)
        print("已保存文件：",output_path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def main():
    print("Start")
    Pic()
if __name__ == "__main__":
    main()