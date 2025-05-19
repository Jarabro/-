import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score

dachshund_length = np.random.randint(60, 80, size= 200) # 닥스훈트 길이 200개 생성
dachshund_height = np.random.randint(20, 40, size= 200) # 닥스훈트 높이 200개 생성

samoyd_length = np.random.randint(70, 90, size= 200) # 사모예드 길이 200개 생성
samoyd_height = np.random.randint(50, 60, size= 200) # 사모예드 높이 200개 생성

dachshund_length_mean = np.mean(dachshund_length) #닥스훈트의 평균 길이 저장
dachshund_height_mean = np.mean(dachshund_height) #닥스훈트의 평균 높이 저장

samoyd_length_mean = np.mean(samoyd_length) #사모예드의 평균 길이 저장
samoyd_height_mean = np.mean(samoyd_height) #사모예드의 평균 높이 저장

new_dachshund_length_data = np.random.normal(dachshund_length_mean, 10.0, 200) #닥스훈트의 평균 길이에 좌우 10.0씩 늘려서 랜덤 200개 생성
new_dachshund_height_data = np.random.normal(dachshund_height_mean, 10.0, 200) #닥스훈트의 평균 높이에 좌우 10.0씩 늘려서 랜덤 200개 생성

new_samoyd_length_data = np.random.normal(samoyd_length_mean, 10.0, 200) #사모예드의 평균 길이에 좌우 10.0씩 늘려서 랜덤 200개 생성
new_samoyd_height_data = np.random.normal(samoyd_height_mean, 10.0, 200) #시모예드의 평균 길이에 좌우 10.0씩 늘려서 랜덤 200개 생성

new_dachshund_data = np.column_stack((new_dachshund_length_data, new_dachshund_height_data)) #닥스훈트의 길이 높이 2차원배열로 합치기
new_samoyd_data = np.column_stack((new_samoyd_length_data, new_samoyd_height_data)) #사모예드의 길이 높이 2차원배열로 합치기

dachshund_label = np.zeros(len(new_dachshund_data)) #닥스훈트는 0으로표시
samoyd_label = np.ones(len(new_samoyd_data)) #사모예드는 1으로표시

unknown_dog_length = np.random.normal((dachshund_length_mean + samoyd_length_mean) / 2, 10.0, size=5) #개 5마리의 길이 5개 생성
unknown_dog_height = np.random.normal((dachshund_height_mean + samoyd_height_mean) / 2, 10.0, size=5)#개 5마리의 높이 5개 생성

new_unknown_dog_data = np.column_stack((unknown_dog_length, unknown_dog_height)) # 높이와 길이 배열 합치기

dogs = np.concat((new_dachshund_data, new_samoyd_data), axis=0)
labels = np.concat((dachshund_label, samoyd_label), axis=0)
dog_classes = {0:"닥스훈트", 1:"사모예드"}

plt.scatter(new_dachshund_length_data,new_dachshund_height_data, c= 'c', marker='o')
plt.scatter(new_samoyd_length_data,new_samoyd_height_data, c= 'b', marker='*')
plt.scatter(unknown_dog_length,unknown_dog_height, c= 'r', marker='p')
plt.xlabel("Height")
plt.ylabel("Length")
plt.legend(["dachshund","samoyd","Unknown_Dog"],loc="upper right")
plt.show()

from sklearn.neighbors import KNeighborsClassifier
k = 3
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(X=dogs, y=labels)
print(knn.classes_)
y_predict = knn.predict(new_unknown_dog_data)
print(y_predict)
print(f"이 강아지는 : {dog_classes[y_predict[0]]},{dog_classes[y_predict[1]]},"
      f"{dog_classes[y_predict[2]]},{dog_classes[y_predict[3]]},{dog_classes[y_predict[4]]}")
print(dogs.shape)
print(labels.shape)

print(f'훈련 정확도 : {knn.score(X=dogs, y=labels)}')
print(f'예측 정확도 : {accuracy_score(labels, knn.predict(dogs))}')