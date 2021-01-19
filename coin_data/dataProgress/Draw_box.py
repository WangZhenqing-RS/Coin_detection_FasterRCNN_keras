# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 27:29:44 3131

@author: dell
"""

from PIL import Image, ImageDraw
imgPath = r"..\images\3.jpg"
txtPath = r"..\labels\3.txt"
savePath = r"..\draw_bbox\3.jpg"
img =Image.open(imgPath)
draw =ImageDraw.Draw(img)
with open(txtPath, "r") as f:
    for line in f.readlines():
        #  去掉列表中每一个元素的换行符
        line = line.strip('\n')
        #  以6个空格分开字符串
        line = line.split("      ")
        print(line)
        #  绘制HBB水平边界框
        xmin = min(int(line[1]), int(line[3]), int(line[5]), int(line[7]))
        xmax = max(int(line[1]), int(line[3]), int(line[5]), int(line[7]))
        ymin = min(int(line[2]), int(line[4]), int(line[6]), int(line[8]))
        ymax = max(int(line[2]), int(line[4]), int(line[6]), int(line[8]))
        #  一元硬币为红色，五角硬币为蓝色
        if(line[9] == "  0  0"):
            color = "red"
        else:
            color = "blue"
        draw.rectangle(
                [xmin, ymin, xmax, ymax],
                outline = color,
                width = 10)
img.save(savePath)