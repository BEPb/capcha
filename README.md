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

Epoch 1/75
320/320 [==============================] - 45s 138ms/step - loss: 3.0718 - accuracy: 0.1586 - val_loss: 2.8747 - val_accuracy: 0.2039
Epoch 2/75
320/320 [==============================] - 45s 141ms/step - loss: 2.0340 - accuracy: 0.3405 - val_loss: 1.5463 - val_accuracy: 0.4949
Epoch 3/75
320/320 [==============================] - 45s 141ms/step - loss: 1.6661 - accuracy: 0.4304 - val_loss: 1.8066 - val_accuracy: 0.3734
Epoch 4/75
320/320 [==============================] - 46s 143ms/step - loss: 1.4168 - accuracy: 0.5179 - val_loss: 5.4259 - val_accuracy: 0.2612
Epoch 5/75
320/320 [==============================] - 47s 148ms/step - loss: 1.3071 - accuracy: 0.5456 - val_loss: 4.1710 - val_accuracy: 0.2384
Epoch 6/75
320/320 [==============================] - 46s 144ms/step - loss: 1.1419 - accuracy: 0.6007 - val_loss: 2.4280 - val_accuracy: 0.3731
Epoch 7/75
320/320 [==============================] - 52s 162ms/step - loss: 1.0775 - accuracy: 0.6175 - val_loss: 1.3217 - val_accuracy: 0.5463
Epoch 8/75
320/320 [==============================] - 50s 154ms/step - loss: 1.0251 - accuracy: 0.6398 - val_loss: 2.0804 - val_accuracy: 0.4455
Epoch 9/75
320/320 [==============================] - 49s 152ms/step - loss: 0.9256 - accuracy: 0.6727 - val_loss: 2.0043 - val_accuracy: 0.4657
Epoch 10/75
320/320 [==============================] - 49s 154ms/step - loss: 0.8982 - accuracy: 0.6898 - val_loss: 0.5300 - val_accuracy: 0.8057
Epoch 11/75
320/320 [==============================] - 49s 154ms/step - loss: 0.8588 - accuracy: 0.6939 - val_loss: 0.8826 - val_accuracy: 0.6892
Epoch 12/75
320/320 [==============================] - 49s 153ms/step - loss: 0.7952 - accuracy: 0.7281 - val_loss: 1.3459 - val_accuracy: 0.5805
Epoch 13/75
320/320 [==============================] - 49s 153ms/step - loss: 0.8165 - accuracy: 0.7150 - val_loss: 0.2727 - val_accuracy: 0.9115
Epoch 14/75
320/320 [==============================] - 50s 156ms/step - loss: 0.7523 - accuracy: 0.7351 - val_loss: 0.4619 - val_accuracy: 0.8349
Epoch 15/75
320/320 [==============================] - 49s 154ms/step - loss: 0.7059 - accuracy: 0.7493 - val_loss: 0.2661 - val_accuracy: 0.9094
Epoch 16/75
320/320 [==============================] - 51s 160ms/step - loss: 0.6947 - accuracy: 0.7590 - val_loss: 0.5004 - val_accuracy: 0.8133
Epoch 17/75
320/320 [==============================] - 51s 158ms/step - loss: 0.6710 - accuracy: 0.7668 - val_loss: 0.4021 - val_accuracy: 0.8522
Epoch 18/75
320/320 [==============================] - 51s 161ms/step - loss: 0.6725 - accuracy: 0.7706 - val_loss: 0.4330 - val_accuracy: 0.8498
Epoch 19/75
320/320 [==============================] - 51s 158ms/step - loss: 0.6192 - accuracy: 0.7829 - val_loss: 1.1799 - val_accuracy: 0.6544
Epoch 20/75
320/320 [==============================] - 49s 153ms/step - loss: 0.6304 - accuracy: 0.7818 - val_loss: 0.5104 - val_accuracy: 0.8127
Epoch 21/75
320/320 [==============================] - 49s 154ms/step - loss: 0.6187 - accuracy: 0.7840 - val_loss: 0.2027 - val_accuracy: 0.9375
Epoch 22/75
320/320 [==============================] - 49s 154ms/step - loss: 0.5515 - accuracy: 0.8119 - val_loss: 0.2799 - val_accuracy: 0.8986
Epoch 23/75
320/320 [==============================] - 50s 157ms/step - loss: 0.5742 - accuracy: 0.7989 - val_loss: 3.6793 - val_accuracy: 0.3012
Epoch 24/75
320/320 [==============================] - 51s 160ms/step - loss: 0.5306 - accuracy: 0.8096 - val_loss: 0.1548 - val_accuracy: 0.9480
Epoch 25/75
320/320 [==============================] - 52s 162ms/step - loss: 0.5399 - accuracy: 0.8171 - val_loss: 0.1523 - val_accuracy: 0.9477
Epoch 26/75
320/320 [==============================] - 51s 158ms/step - loss: 0.5281 - accuracy: 0.8157 - val_loss: 0.8797 - val_accuracy: 0.7076
Epoch 27/75
320/320 [==============================] - 52s 161ms/step - loss: 0.5107 - accuracy: 0.8269 - val_loss: 0.3116 - val_accuracy: 0.8934
Epoch 28/75
320/320 [==============================] - 53s 166ms/step - loss: 0.4681 - accuracy: 0.8397 - val_loss: 0.1853 - val_accuracy: 0.9366
Epoch 29/75
320/320 [==============================] - 52s 162ms/step - loss: 0.5115 - accuracy: 0.8284 - val_loss: 0.4041 - val_accuracy: 0.8604
Epoch 30/75
320/320 [==============================] - 53s 165ms/step - loss: 0.4654 - accuracy: 0.8332 - val_loss: 0.1272 - val_accuracy: 0.9559
Epoch 31/75
320/320 [==============================] - 52s 161ms/step - loss: 0.4699 - accuracy: 0.8364 - val_loss: 0.5959 - val_accuracy: 0.7905
Epoch 32/75
320/320 [==============================] - 50s 157ms/step - loss: 0.4488 - accuracy: 0.8444 - val_loss: 0.1304 - val_accuracy: 0.9588
Epoch 33/75
320/320 [==============================] - 50s 155ms/step - loss: 0.4422 - accuracy: 0.8481 - val_loss: 1.6404 - val_accuracy: 0.5732
Epoch 34/75
320/320 [==============================] - 50s 155ms/step - loss: 0.4337 - accuracy: 0.8500 - val_loss: 0.0986 - val_accuracy: 0.9673
Epoch 35/75
320/320 [==============================] - 52s 162ms/step - loss: 0.4061 - accuracy: 0.8590 - val_loss: 1.2640 - val_accuracy: 0.6339
Epoch 36/75
320/320 [==============================] - 51s 160ms/step - loss: 0.3999 - accuracy: 0.8570 - val_loss: 0.2862 - val_accuracy: 0.8989
Epoch 37/75
320/320 [==============================] - 49s 153ms/step - loss: 0.3947 - accuracy: 0.8643 - val_loss: 0.1509 - val_accuracy: 0.9480
Epoch 38/75
320/320 [==============================] - 51s 158ms/step - loss: 0.3789 - accuracy: 0.8676 - val_loss: 0.5706 - val_accuracy: 0.8092
Epoch 39/75
320/320 [==============================] - 50s 155ms/step - loss: 0.4204 - accuracy: 0.8613 - val_loss: 0.1649 - val_accuracy: 0.9404
Epoch 40/75
320/320 [==============================] - 49s 152ms/step - loss: 0.3780 - accuracy: 0.8704 - val_loss: 0.4611 - val_accuracy: 0.8472
Epoch 41/75
320/320 [==============================] - 48s 151ms/step - loss: 0.3882 - accuracy: 0.8667 - val_loss: 0.0660 - val_accuracy: 0.9804
Epoch 42/75
320/320 [==============================] - 49s 155ms/step - loss: 0.3687 - accuracy: 0.8701 - val_loss: 0.3412 - val_accuracy: 0.8837
Epoch 43/75
320/320 [==============================] - 50s 156ms/step - loss: 0.3591 - accuracy: 0.8837 - val_loss: 0.3206 - val_accuracy: 0.8899
Epoch 44/75
320/320 [==============================] - 50s 157ms/step - loss: 0.3750 - accuracy: 0.8766 - val_loss: 0.0612 - val_accuracy: 0.9796
Epoch 45/75
320/320 [==============================] - 50s 156ms/step - loss: 0.3528 - accuracy: 0.8804 - val_loss: 0.9149 - val_accuracy: 0.7476
Epoch 46/75
320/320 [==============================] - 50s 156ms/step - loss: 0.3478 - accuracy: 0.8804 - val_loss: 0.0685 - val_accuracy: 0.9804
Epoch 47/75
320/320 [==============================] - 51s 159ms/step - loss: 0.3290 - accuracy: 0.8878 - val_loss: 0.1138 - val_accuracy: 0.9571
Epoch 48/75
320/320 [==============================] - 52s 162ms/step - loss: 0.3594 - accuracy: 0.8716 - val_loss: 0.1523 - val_accuracy: 0.9436
Epoch 49/75
320/320 [==============================] - 50s 155ms/step - loss: 0.3354 - accuracy: 0.8867 - val_loss: 0.2443 - val_accuracy: 0.9135
Epoch 50/75
320/320 [==============================] - 50s 155ms/step - loss: 0.3262 - accuracy: 0.8859 - val_loss: 0.1149 - val_accuracy: 0.9571
Epoch 51/75
320/320 [==============================] - 50s 155ms/step - loss: 0.3373 - accuracy: 0.8873 - val_loss: 0.0711 - val_accuracy: 0.9772
Epoch 52/75
320/320 [==============================] - 51s 159ms/step - loss: 0.3326 - accuracy: 0.8867 - val_loss: 1.8877 - val_accuracy: 0.5349
Epoch 53/75
320/320 [==============================] - 51s 159ms/step - loss: 0.3179 - accuracy: 0.8933 - val_loss: 0.1751 - val_accuracy: 0.9401
Epoch 54/75
320/320 [==============================] - 52s 163ms/step - loss: 0.3258 - accuracy: 0.8939 - val_loss: 0.1542 - val_accuracy: 0.9454
Epoch 55/75
320/320 [==============================] - 52s 162ms/step - loss: 0.3072 - accuracy: 0.8929 - val_loss: 0.6961 - val_accuracy: 0.7742
Epoch 56/75
320/320 [==============================] - 52s 163ms/step - loss: 0.3246 - accuracy: 0.8920 - val_loss: 0.1306 - val_accuracy: 0.9535
Epoch 57/75
320/320 [==============================] - 52s 164ms/step - loss: 0.2910 - accuracy: 0.9028 - val_loss: 0.2006 - val_accuracy: 0.9360
Epoch 58/75
320/320 [==============================] - 52s 163ms/step - loss: 0.3061 - accuracy: 0.8957 - val_loss: 0.1173 - val_accuracy: 0.9597
Epoch 59/75
320/320 [==============================] - 53s 165ms/step - loss: 0.2842 - accuracy: 0.9022 - val_loss: 0.0547 - val_accuracy: 0.9842
Epoch 60/75
320/320 [==============================] - 51s 159ms/step - loss: 0.2968 - accuracy: 0.8941 - val_loss: 0.0429 - val_accuracy: 0.9871
Epoch 61/75
320/320 [==============================] - 54s 170ms/step - loss: 0.2732 - accuracy: 0.9094 - val_loss: 0.7990 - val_accuracy: 0.7441
Epoch 62/75
320/320 [==============================] - 54s 168ms/step - loss: 0.2783 - accuracy: 0.9033 - val_loss: 0.1100 - val_accuracy: 0.9609
Epoch 63/75
320/320 [==============================] - 54s 168ms/step - loss: 0.2693 - accuracy: 0.9058 - val_loss: 0.3150 - val_accuracy: 0.8916
Epoch 64/75
320/320 [==============================] - 52s 162ms/step - loss: 0.2852 - accuracy: 0.9018 - val_loss: 0.1812 - val_accuracy: 0.9363
Epoch 65/75
320/320 [==============================] - 51s 160ms/step - loss: 0.2904 - accuracy: 0.8992 - val_loss: 0.2737 - val_accuracy: 0.9024
Epoch 66/75
320/320 [==============================] - 52s 162ms/step - loss: 0.2670 - accuracy: 0.9089 - val_loss: 1.3612 - val_accuracy: 0.6415
Epoch 67/75
320/320 [==============================] - 49s 152ms/step - loss: 0.2740 - accuracy: 0.9065 - val_loss: 0.0618 - val_accuracy: 0.9810
Epoch 68/75
320/320 [==============================] - 49s 152ms/step - loss: 0.2846 - accuracy: 0.9000 - val_loss: 0.0780 - val_accuracy: 0.9760
Epoch 69/75
320/320 [==============================] - 49s 152ms/step - loss: 0.2704 - accuracy: 0.9121 - val_loss: 0.0647 - val_accuracy: 0.9769
Epoch 70/75
320/320 [==============================] - 49s 153ms/step - loss: 0.2710 - accuracy: 0.9077 - val_loss: 0.0791 - val_accuracy: 0.9758
Epoch 71/75
320/320 [==============================] - 50s 155ms/step - loss: 0.2744 - accuracy: 0.9017 - val_loss: 0.3773 - val_accuracy: 0.8744
Epoch 72/75
320/320 [==============================] - 49s 154ms/step - loss: 0.2684 - accuracy: 0.9076 - val_loss: 0.0712 - val_accuracy: 0.9749
Epoch 73/75
320/320 [==============================] - 49s 153ms/step - loss: 0.2570 - accuracy: 0.9126 - val_loss: 0.0327 - val_accuracy: 0.9901
Epoch 74/75
320/320 [==============================] - 49s 153ms/step - loss: 0.2493 - accuracy: 0.9140 - val_loss: 0.0797 - val_accuracy: 0.9714
Epoch 75/75
320/320 [==============================] - 49s 153ms/step - loss: 0.2645 - accuracy: 0.9102 - val_loss: 0.0379 - val_accuracy: 0.9901
[INFO] evaluating network...
              precision    recall  f1-score   support

           0       0.98      1.00      0.99       142
           1       1.00      0.99      0.99       695
           2       0.98      0.99      0.99       268
           3       0.99      0.97      0.98       289
           4       1.00      1.00      1.00       338
           5       1.00      0.98      0.99       290
           6       0.96      0.99      0.98       278
           7       0.98      1.00      0.99       321
           8       0.98      0.99      0.99       266
           9       1.00      1.00      1.00       536

    accuracy                           0.99      3423
   macro avg       0.99      0.99      0.99      3423
weighted avg       0.99      0.99      0.99      3423

[INFO] serializing network and label binarizer...
2021-06-13 20:38:35.692934: W tensorflow/python/util/util.cc:348] Sets are not currently considered sequences, but this may change in the future, so consider avoiding using them.

Process finished with exit code 0


# оцениваем нейросеть
Итоговая точность 99% из 3423 файлов