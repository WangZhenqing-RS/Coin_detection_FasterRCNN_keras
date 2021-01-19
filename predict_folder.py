from keras.layers import Input
from frcnn import FRCNN 
from PIL import Image
import os
import matplotlib.pyplot as plt

frcnn = FRCNN()

#  测试图像文件夹
testImageFolder = r"coin_data\testImages"
#  预测结果保存文件夹
predictFolder = r"coin_data\testPredict_flip"
#  测试图像文件名链表
testImageList = os.listdir(testImageFolder)

coin_number_sum = 0
money_total_sum = 0
#  遍历图像文件并预测保存
for i in range(len(testImageList)):
    imgPath = testImageFolder + "//" + testImageList[i]
    image = Image.open(imgPath)
    r_image, coin_number, money_total = frcnn.detect_image(image)
    r_image.save(predictFolder + "//" + testImageList[i])
    plt.imshow(r_image)
    plt.ion()
    plt.pause(0.1)
    # plt.close()
    coin_number_sum += coin_number
    money_total_sum += money_total

print("硬币个数：%s枚"%str(coin_number_sum))
print("价值总量：%s元"%str(money_total_sum))
frcnn.close_session()