# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:18:30 2020

@author: dell
"""
import  os
def make_train_txt(img_floder, txt_floder, train_txt_Path):
    img_list = os.listdir(img_floder)
    #  打开要写的train_txt_Path
    train_txt_f = open(train_txt_Path, 'a')
    for img_name in img_list:
        #  去除.jpg后缀
        name = img_name[:-4]
        #  图像完整路径
        img_path = img_floder + "\\" + img_name
        #  对应图像完整路径
        txt_path = txt_floder + "\\" + name + ".txt"
        #  在train_txt_Path中写入图像路径
        train_txt_f.write(img_path)
        with open(txt_path, "r") as f_in:
            lines = f_in.readlines()
            #  逐行读取
            for line  in lines:
                line = line.strip('\n')  
                line = line.split("      ")
                xmin = min(int(line[1]), int(line[3]), int(line[5]), int(line[7]))
                xmax = max(int(line[1]), int(line[3]), int(line[5]), int(line[7]))
                ymin = min(int(line[2]), int(line[4]), int(line[6]), int(line[8]))
                ymax = max(int(line[2]), int(line[4]), int(line[6]), int(line[8]))
                if(line[9] == "  0  0"):
                    train_txt_f.write(' %s,%s,%s,%s,0'%(xmin, ymin, xmax, ymax))
                if(line[9] == "  0  1"):
                    train_txt_f.write(' %s,%s,%s,%s,1'%(xmin, ymin, xmax, ymax))
            train_txt_f.write('\n')
    print("Done!")
#  数据集的标签文件存放文件夹 
txt_floder = r"D:\WangZhenqing\Coin_detection_FasterRCNN\coin_data\labels"
#  像数据集图像存放文件夹
img_floder = r"D:\WangZhenqing\Coin_detection_FasterRCNN\coin_data\images"
#  train.txt路径
train_txt_Path = r"..\train_flip.txt"

make_train_txt(img_floder, txt_floder, train_txt_Path)