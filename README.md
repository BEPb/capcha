## Распознавание чисел капчи Wmail.ru от 0 до 9 на изображениях с помощью сверточной нейронной сети 

Для распознавания используется сверточная нейронная сеть.

Перед использованием необходимо скачать и подготовить данные для обучения, проверки и тестирования.

# Каталог с данными для обучения
'train'
# Каталог с данными для проверки
'images'

# Размеры изображения
img_width, img_height = 18, 60

# Количество эпох
epochs = 75
# Размер мини-выборки
batch_size = 320
# Количество изображений для обучения
nb_train_samples = 13691
# Количество изображений для проверки
nb_validation_samples = 3490
# Количество изображений для тестирования
nb_test_samples = 3490

# используем VGG-подобную сверточную нейросеть
компилируем модель с помощью SGD

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