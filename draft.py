# USAGE
# python train_vgg.py --dataset animals --model output/smallvggnet.model --label-bin output/smallvggnet_lb.pickle --plot output/smallvggnet_plot.png
# --dataset train --model output/smallvggnet.model --label-bin output/smallvggnet_lb.pickle --plot output/smallvggnet_plot.png
# импортируем бэкенд Agg из matplotlib для сохранения графиков на диск
import matplotlib
matplotlib.use("Agg")

# подключаем необходимые пакеты
from pyimagesearch.smallvggnet import SmallVGGNet
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2
import os

import sys
print(sys.version)

import tensorflow as tf
print(tf.__version__)

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# print(sess.run(c))



# On CPU/GPU placement
config = tf.compat.v1.ConfigProto(allow_soft_placement=True, log_device_placement=True)
config.gpu_options.allow_growth = True
tf.compat.v1.Session(config=config)




from tensorflow.python.client import device_lib
def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]
print(get_available_devices())


# создаём парсер аргументов и передаём их
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset of images")
ap.add_argument("-m", "--model", required=True,
	help="path to output trained model")
ap.add_argument("-l", "--label-bin", required=True,
	help="path to output label binarizer")
ap.add_argument("-p", "--plot", required=True,
	help="path to output accuracy/loss plot")
args = vars(ap.parse_args())

# инициализируем данные и метки
print("[INFO] loading images...")
data = []
labels = []

# берём пути к изображениям и рандомно перемешиваем
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

# цикл по изображениям
for imagePath in imagePaths:
	# загружаем изображение, меняем размер на 64x64 пикселей
	# (требуемые размеры для SmallVGGNet), изменённое изображение
	# добавляем в список
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (18, 60))
	data.append(image)

	# извлекаем метку класса из пути к изображению и обновляем
	# список меток
	label = imagePath.split(os.path.sep)[-2]
	labels.append(label)

# масштабируем интенсивности пикселей в диапазон [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

# разбиваем данные на обучающую и тестовую выборки, используя 75%
# данных для обучения и оставшиеся 25% для тестирования
(trainX, testX, trainY, testY) = train_test_split(data,
	labels, test_size=0.25, random_state=42)

# конвертируем метки из целых чисел в векторы (для 2х классов при
# бинарной классификации вам следует использовать функцию Keras
# “to_categorical” вместо “LabelBinarizer” из scikit-learn, которая
# не возвращает вектор)
lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)

# создаём генератор для добавления изображений
aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest")

# инициализируем нашу VGG-подобную сверточную нейросеть
model = SmallVGGNet.build(width=18, height=60, depth=3,
	classes=len(lb.classes_))

# инициализируем скорость обучения, общее число эпох
# и размер пакета
INIT_LR = 0.01
EPOCHS = 75
BS = 32

# компилируем модель с помощью SGD (для бинарной классификации
# следует использовать binary_crossentropy)
print("[INFO] training network...")
opt = SGD(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# обучаем нейросеть
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
	validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
	epochs=EPOCHS)

# оцениваем нейросеть
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1), target_names=lb.classes_))

# строим графики потерь и точности
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, H.history["accuracy"], label="train_acc")
plt.plot(N, H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy (SmallVGGNet)")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig(args["plot"])

# сохраняем модель и бинаризатор меток на диск
print("[INFO] serializing network and label binarizer...")
model.save(args["model"])
f = open(args["label_bin"], "wb")
f.write(pickle.dumps(lb))
f.close()


