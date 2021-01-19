from keras.layers import Input
from frcnn import FRCNN 
from PIL import Image
import os
import matplotlib.pyplot as plt

frcnn = FRCNN()

imgPath = r"D:\WangZhenqing\Coin_detection_FasterRCNN\coin_data\images\2.jpg"
predictPath = r"2.jpg"
image = Image.open(imgPath)
plt.imshow(image)
plt.show()
r_image, coin_number, money_total = frcnn.detect_image(image)
r_image.save(predictPath)
plt.imshow(r_image)
plt.show()
print("硬币个数：%s枚"%str(coin_number))
print("价值总量：%s元"%str(money_total))
frcnn.close_session()