import random
from numpy import linalg
from math import sqrt



min_x1 = -40
min_x2 = 30
max_x1 = 20
max_x2 = 80



m = 5

min_y = (30 - 227) * 10
max_y = (20 - 227) * 10

X = [[-1, -1],
     [1, -1],
     [-1, 1]]


print("Variant 227 - X1({0};{1}) X2({2};{3}) Y({4};{5})".format(min_x1, max_x1, min_x1, max_x2, max_y, min_y))


array1_of_y = []
array2_of_y = []
array3_of_y = []


for i in range(m):
    array1_of_y.append(random.randint(max_y, min_y))
    array2_of_y.append(random.randint(max_y, min_y))
    array3_of_y.append(random.randint(max_y, min_y))

print("Матриця планування експерименту:\n{0}\n{1}\n{2}".format(array1_of_y,array2_of_y,array3_of_y))

average_array1_of_y = sum(array1_of_y) / m
average_array2_of_y = sum(array2_of_y) / m
average_array3_of_y = sum(array3_of_y) / m

print("Середнє значення:\n{0}\n{1}\n{2}".format(average_array1_of_y, average_array2_of_y, average_array3_of_y))

dispersion = []

dispersion.append(sum([(array1_of_y[i] - average_array1_of_y)**2 for i in range(m)]) / m)
dispersion.append(sum([(array2_of_y[i] - average_array2_of_y)**2 for i in range(m)]) / m)
dispersion.append(sum([(array3_of_y[i] - average_array3_of_y)**2 for i in range(m)]) / m)

print("Дисперсія першого рядка: {0}\nДисперсія другого рядка: {1}\nДипсперсія третього рядка: {2}".format(dispersion[0], dispersion[1], dispersion[2]))

deviation = (sqrt((2 * (2 * m - 2)) / (m * (m - 4))))

print("Відхилення: ", deviation)

F_uv1 = dispersion[0] / dispersion[1]
F_uv2 = dispersion[2] / dispersion[0]
F_uv3 = dispersion[2] / dispersion[1]

T_uv1 = ((m - 2) / m) * F_uv1
T_uv2 = ((m - 2) / m) * F_uv2
T_uv3 = ((m - 2) / m) * F_uv3

R_uv1 = abs(T_uv1 - 1) / deviation
R_uv2 = abs(T_uv2 - 1) / deviation
R_uv3 = abs(T_uv3 - 1) / deviation


if R_uv1 < 2 or R_uv2 < 2 or R_uv3 < 2:
    print('Дисперсія однорідна')



X = [[-1, -1],
     [1, -1],
     [-1, 1]]


M_x1 = (X[0][0] + X[1][0] + X[2][0]) / 3
M_x2 = (X[0][1] + X[1][1] + X[2][1]) / 3
M_y = (average_array1_of_y+average_array2_of_y+average_array3_of_y)/3

a1 = ((X[0][0])**2+(X[1][0])**2+(X[2][0])**2)/3
a2 = (X[0][0]*X[0][1]+X[1][0]*X[1][1]+X[2][0]*X[2][1])/3
a3 = ((X[0][1])**2+(X[1][1])**2+(X[2][1])**2)/3

a11 = (X[0][0] * average_array1_of_y + X[1][0] * average_array2_of_y + X[2][0] * average_array3_of_y) / 3
a22 = (X[0][1] * average_array1_of_y + X[1][1] * average_array2_of_y + X[2][1] * average_array3_of_y) / 3

b0 = (linalg.det([[M_y, M_x1, M_x2],
                  [a11, a1, a2],
                  [a22, a2, a3]])) / (linalg.det([[1, M_x1, M_x2],
                                                  [M_x1, a1, a2],
                                                  [M_x2, a2, a3]]))

b1 = (linalg.det([[1, M_y, M_x2],
                  [M_x1, a11, a2],
                  [M_x2, a22, a3]])) / (linalg.det([[1, M_x1, M_x2],
                                                [M_x1, a1, a2],
                                                [M_x2, a2, a3]]))

b2 = (linalg.det([[1, M_x1, M_y],
                  [M_x1, a1, a11],
                  [M_x2, a2, a22]])) / (linalg.det([[1, M_x1, M_x2],
                                                [M_x1, a1, a2],
                                                [M_x2, a2, a3]]))

print('Нормоване рівняння регресії:\ny = {0} + {1} * x1 + {2} * x2\n'.format(b0, b1, b2))

delta_x1 = abs(max_x1 - min_x1) / 2
delta_x2 = abs(max_x2-min_x2) / 2
x10 = (max_x1+min_x1) / 2
x20 = (max_x2+min_x2) / 2

a0 = b0 - b1*x10 / delta_x1-b2*x20 / delta_x2
a1 = b1 / delta_x1
a2 = b2 / delta_x2

print('Натуралізоване рівняння регресії:\ny = {0} + {1} * x1 + {2} * x2\n'.format(a0, a1, a2))

print('Перевірка:\n'
      'a0 + a1 * min_x1 + a2 * min_x2 = {0}\n'
      'b0 + b1 * X[0][0] + b2 * X[0][1] = {1}\n'
      'a0 + a1 * max_x1 + a2 * max_x2 = {2}\n'
      'b0 + b1 * X[1][0] + b2 * X[1][1] = {3}\n'
      'a0 + a1 * min_x1 + a2 * min_x2 = {4}\n'
      'b0 + b1 * X[2][0] + b2 * X[2][1] = {5}'.format((a0 + a1 * min_x1 + a2 * min_x2),
                                            (b0 + b1 * X[0][0] + b2 * X[0][1]),
                                            (a0 + a1 * max_x1 + a2 * min_x2),
                                            (b0 + b1 * X[1][0] + b2 * X[1][1]),
                                            (a0 + a1 * min_x1 + a2 * max_x2),
                                            (b0 + b1 * X[2][0] + b2 * X[2][1])))