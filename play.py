import time
import os

txt_path = "text/"
with open(txt_path+"info.txt",'r') as info:
    fps = float(info.readline()) + 10.0
    count = int(info.readline())

for i in range(count):
    os.system('cat '+txt_path+str(i)+'.txt')
    time.sleep(1.0/fps)
    os.system('clear')
