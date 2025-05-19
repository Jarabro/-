import tensorflow as tf
import keras
from keras.src.datasets.mnist import load_data

(X_train, y_train), (X_test, y_test) =load_data()
print(X_train.shape)
print(X_test.shape)

X_test = X_test.reshape((-1, 28, 28, 1))
print(X_train.shape)
print(X_test.shape)

X_train =X_train/255.0
X_test = X_test/255.0
# print(X_test[0])
#
#
# model = keras.Sequential([], name="CNN")
# input_layer = keras.Input(shape=(28,28,1), name="InputLayer")
# model.add(input_layer)
# model.add(keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', name="Conv2D_1"))
# model.add(keras.layers.MaxPooling2D(pool_size=(2,2), name="MAaxPool2D_1"))
# model.add(keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', name="Conv2D_2"))
# model.add(keras.layers.MaxPooling2D(pool_size=(2,2), name="MAaxPool2D_2"))
# model.add(keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', name="Conv2D_3"))
# model.add(keras.layers.MaxPooling2D(pool_size=(2,2), name="MAaxPool2D_3"))
#
# model.add(keras.layers.Flatten()) #DNN
# model.add(keras.layers.Dense(units=64, activation='relu', name="HiddenLayer1"))
# model.add(keras.layers.Dense(units=10, activation='softmax', name="OutputLayer"))
# model.summary()
#
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#
# model.fit(x=X_train, y=y_train, epochs=10, verbose='auto')
# print(f'예측 정확도 : {model.evaluate(x=X_test, y=y_test)}')
#
# model.save("2025-03-27_CNN.keras")

good_model = keras.models.load_model('2025-03-27_CNN.keras')

import matplotlib.pyplot as plt

# 학습 및 기록 저장
history = good_model.fit(x=X_train, y=y_train, epochs=10, validation_data=(X_test, y_test), verbose=1)

# 정확도 그래프 출력
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Epoch -> Accuracy')
plt.show()

import cv2 as cv
Original = cv.imread('test3.png', cv.IMREAD_GRAYSCALE)
image = cv.resize(Original, (28,28))
image = 255 - image
image = image.astype('float32')
image = image.reshape(-1, 28, 28, 1)
image = image / 255.0

predict_image = good_model.predict(image)
print(f'그림 이미지 값은 : {predict_image} ')
print(f"추정된 숫자 : {predict_image.argmax()}")
