#coding = utf-8

import cv2
import time
import numpy
import os

def save_itxt(txt,txt_name):		#定义保存文件的函数
    with open(txt_name,"w") as f:
        f.write(txt)


videoCapture = cv2.VideoCapture("video.avi")	#打开视频文件

w = videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)	#获取视频的宽度，长度，帧率
h = videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)

Image_Count = 0		#视频帧计数
success, frame = videoCapture.read()	#读取视频的第一帧

txt_path = "text/"		#设置保存转换后的txt保存的文件夹

while success:				#将视频转换为字符
    Image_Count += 1
    frame = cv2.resize(frame,(110,33))		#缩小图片的尺寸
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    tmg = ""
    file_name = txt_path + str(Image_Count) + ".txt"
    for w in range(frame.shape[0]):
        for h in range(frame.shape[1]):
            if frame[w][h] < 127:
                tmg += "#"
            else:
                tmg += " "
        tmg += "\n"
    save_itxt(tmg,file_name)
    success, frame = videoCapture.read()

info =str(fps) + "\n" + str(Image_Count)
save_itxt(info,txt_path+"info.txt")		#保存视频信息
