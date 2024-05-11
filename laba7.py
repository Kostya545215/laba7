from random import randint
import time
import csv
import math

import numpy as np
import matplotlib.pyplot as plt

#task 1

a = [randint(-100000, 100000) for x in range(1000000)]
b = [randint(-100000, 100000) for x in range(1000000)]

st = time.perf_counter()
c = np.multiply(a, b)
print( time.perf_counter() - st)

st = time.perf_counter()
c = []
for i in range(1000000):
    c.append(a[i]*b[i]) 
print(time.perf_counter() - st)

#task 2 (либо блок 1, либо блок 2 нужно комментировать для корректного выведения графиков)


# with open('laba_python/data1.csv', 'r') as f:
#     next(f)
#     reader = csv.reader(f, delimiter= ';')
#     x = [float(row[0]) for row in reader]
#     f.seek(0)
#     next(f)
#     y1 = [ float(row[9]) for row in reader]
#     f.seek(0)
#     next(f)
#     y2 = [ float(row[15]) for row in reader]

#блок1 - построения двух графиков

###
# fig, ax = plt.subplots()  
# ax.plot(x,y2, label = 'Массовый расход воздуха')  
# ax.plot(x,y1, label = 'Угол опережения зажигания')
# ax.set_xlabel('Время')
# ax.set_ylabel('y label')
# ax.set_title('y(x)')
# plt.legend()
# plt.show()
###

#блок2 - построения графика корреляции 

###

# corr_coef = np.corrcoef(y1, y2)

# k = float(corr_coef[0][1])

# x = np.linspace(0, 34, 2)

# plt.xlim(0, 1) 
# plt.ylim(-1, 1)  

# plt.plot(x, k*x)
# plt.title('correlation graph')
# plt.xlabel('Угол опережения зажигания')
# plt.ylabel('Массовый расход воздуха')
# plt.show()

###

#task 3

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# x = np.linspace(-5 * math.pi, 5*math.pi, 100)
# y = np.linspace(-5 * math.pi, 5*math.pi, 100)
# X, Y = np.meshgrid(x, y)

# z = Y * np.cos(X)

# ax.plot_surface(X, Y, z)
# plt.show()


