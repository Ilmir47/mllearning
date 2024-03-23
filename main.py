import numpy as np
import matplotlib.pyplot as plt

dt = np.dtype("f8, f8, f8, f8, U30")
data = np.genfromtxt("iris.data", delimiter=",", dtype=dt)
# print(data)

sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
i_s = 0
i_vir = 0
for dot in data:
    sepal_length.append(dot[0])
    sepal_width.append(dot[1])
    petal_length.append(dot[2])
    petal_width.append(dot[3])
    if dot[4] == 'Iris-setosa':
        i_s += 1
    elif dot[4] == 'Iris-virginica':
        i_vir += 1

# Вывод максимального, минимального, среднего значений и дисперсии для каждого из параметров.
# print(max(sepal_length),min(sepal_length), round(np.mean(sepal_length),2), round(np.std(sepal_length), 2))
# print(max(sepal_width),min(sepal_width), round(np.mean(sepal_width),2), round(np.std(sepal_width), 2))
# print(max(petal_length),min(petal_length), round(np.mean(petal_length),2), round(np.std(petal_length), 2))
# print(max(petal_width),min(petal_width), round(np.mean(petal_width),2), round(np.std(petal_width), 2))
# print(i_s, i_vir, 150 - i_s - i_vir)

for dot in data:
    sepal_length.append(dot[0])
    sepal_width.append(dot[1])
    petal_length.append(dot[2])
    petal_width.append(dot[3])

#Посторение графиков зависимости от каждого параметра
plt.figure(1)
setosa, = plt.plot(sepal_length[:50], sepal_width[:50], 'ro', label='Setosa')
versicolor, = plt.plot(sepal_length[50:100], sepal_width[50:100], 'g^', label='Versicolor')
virginica, = plt.plot(sepal_length[100:150], sepal_width[100:150], 'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.figure(2)
setosa, = plt.plot(sepal_length[:50], petal_length[:50], 'ro', label='Setosa')
versicolor, = plt.plot(sepal_length[50:100], petal_length[50:100], 'g^', label='Versicolor')
virginica, = plt.plot(sepal_length[100:150], petal_length[100:150], 'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.figure(3)
setosa, = plt.plot(sepal_width[:50], petal_width[:50], 'ro', label='Setosa')
versicolor, = plt.plot(sepal_length[50:100], petal_width[50:100], 'g^', label='Versicolor')
virginica, = plt.plot(sepal_length[100:150], petal_width[100:150], 'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')

plt.figure(4)
setosa, = plt.plot(sepal_width[:50], petal_length[:50], 'ro', label='Setosa')
versicolor, = plt.plot(sepal_width[50:100], petal_length[50:100], 'g^', label='Versicolor')
virginica, = plt.plot(sepal_width[100:150], petal_length[100:150], 'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Sepal Width')
plt.ylabel('Petal Length')

plt.figure(5)
setosa, = plt.plot(sepal_width[:50], petal_width[:50], 'ro', label='Setosa')
versicolor, = plt.plot(sepal_width[50:100], petal_width[50:100], 'g^', label='Versicolor')
virginica, = plt.plot(sepal_width[100:150], petal_width[100:150], 'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Sepal Width')
plt.ylabel('Petal Width')

plt.figure(6)
setosa, = plt.plot(petal_length[:50], petal_width[:50], 'ro', label='Setosa')
versicolor, = plt.plot(petal_length[50:100], petal_width[50:100], 'g^', label='Versicolor')
virginica, = plt.plot(petal_length[100:150], petal_width[100:150], 'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.show()