import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os

#  翻转
#  img:图像
#  bboxes:该图像包含的所有bbox,一个list,每个元素为[x_min, y_min, x_max, y_max, class]
#  HorV:1水平翻转还是0垂直翻转
def filp(image, bboxes, HorV, flip_image_path, flip_label_path):
    #  翻转图像
    w,h = image.size
    #  HorV == 1代表水平翻转
    if HorV == 1:
        flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        flip_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    flip_image.save(flip_image_path)
    drowBbox = flip_image.copy()
    draw =ImageDraw.Draw(drowBbox)
    #  调整Bbox
    flip_bboxes = []
    flip_label_file = open(flip_label_path, 'a')
    for box in bboxes:
        x_min = box[0]
        y_min = box[1]
        x_max = box[2]
        y_max = box[3]
        if HorV == 1:
            #  和原标签保持一致
            flip_bboxes.append([w-x_max, y_min, w-x_min, y_max, box[4]])
            flip_label_file.write('      %s'%(w-x_max))
            flip_label_file.write('      %s'%(y_min))
            flip_label_file.write('      %s'%(w-x_min))
            flip_label_file.write('      %s'%(y_min))
            flip_label_file.write('      %s'%(w-x_min))
            flip_label_file.write('      %s'%(y_max))
            flip_label_file.write('      %s'%(w-x_max))
            flip_label_file.write('      %s'%(y_max))
            if(box[4] == 0):
                flip_label_file.write('      %s\n'%('  0  0'))
            else:
                flip_label_file.write('      %s\n'%('  0  1'))
        else:
            flip_bboxes.append([x_min, h-y_max, x_max, h-y_min, box[4]])
            flip_label_file.write('      %s'%(x_min))
            flip_label_file.write('      %s'%(h-y_max))
            flip_label_file.write('      %s'%(x_max))
            flip_label_file.write('      %s'%(h-y_max))
            flip_label_file.write('      %s'%(x_max))
            flip_label_file.write('      %s'%(h-y_min))
            flip_label_file.write('      %s'%(x_min))
            flip_label_file.write('      %s'%(h-y_min))
            if(box[4] == 0):
                flip_label_file.write('      %s\n'%('  0  0'))
            else:
                flip_label_file.write('      %s\n'%('  0  1'))
        if box[4] == 0:
            draw.rectangle(
                    [w-x_max, y_min, w-x_min, y_max],
                    outline = "red",
                    width = 10)
        else:
            draw.rectangle(
                    [w-x_max, y_min, w-x_min, y_max],
                    outline = "blue",
                    width = 10)
    return flip_image, flip_bboxes, drowBbox

image_folder = r"..\images"
label_folder = r"..\labels"
image_name_list = os.listdir(image_folder)
flip_number = 101
for image_name in image_name_list:
    image_path = image_folder + "\\" + image_name
    label_path = label_folder + "\\" + image_name[:-4] + ".txt"
    flip_image_path = image_folder + "\\" + str(flip_number) + ".jpg"
    flip_label_path = label_folder + "\\" + str(flip_number) + ".txt"
    image = Image.open(image_path)
    bboxes = []
    with open(label_path, "r") as f_in:
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
                bboxes.append([xmin, ymin, xmax, ymax, 0])
            else:
                bboxes.append([xmin, ymin, xmax, ymax, 1])
    flip_image, flip_bboxes, drowBbox = filp(image, bboxes, 1, flip_image_path, flip_label_path)
    flip_number += 1
    flip_image_path = image_folder + "\\" + str(flip_number) + ".jpg"
    flip_label_path = label_folder + "\\" + str(flip_number) + ".txt"
    flip_image, flip_bboxes, drowBbox = filp(image, bboxes, 0, flip_image_path, flip_label_path)
    flip_number += 1