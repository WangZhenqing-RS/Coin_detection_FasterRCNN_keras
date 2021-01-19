from shutil import copyfile
import os

imageFolder = r"D:\WangZhenqing\Coin_detection_FasterRCNN\coin_data\images"
labelFolder = r"D:\WangZhenqing\Coin_detection_FasterRCNN\coin_data\labels"

testImageFolder = r"D:\WangZhenqing\Coin_detection_FasterRCNN\coin_data\testImages"
testLabelFolder = r"D:\WangZhenqing\Coin_detection_FasterRCNN\coin_data\testLabels"

if not os.path.exists(testImageFolder):
    os.makedirs(testImageFolder)
if not os.path.exists(testLabelFolder):
    os.makedirs(testLabelFolder)

imageNameList = os.listdir(imageFolder)
print(imageNameList)
for imageName in imageNameList:
    imageSource = imageFolder + "/" + imageName
    labelSource = labelFolder + "/" + imageName[:-4] + ".txt"
    #  末尾为1的图像为测试集
    if(int(imageName[:-4])%10 == 1):
        imageTarget = testImageFolder + "/" + imageName
        copyfile(imageSource, imageTarget)
        os.remove(imageSource)
        labelTarget = testLabelFolder + "/" + imageName[:-4] + ".txt"
        copyfile(labelSource, labelTarget)
        os.remove(labelSource)