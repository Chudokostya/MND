#Generation of x
import random
X_1 = []
X_2 = []
X_3 = []
for i in range(8):
    X_1.append(random.randint(1,20))
    X_2.append(random.randint(1,20))
    X_3.append(random.randint(1,20))


#Generation of a
A = []
for i in range(4):
    A.append(random.randint(1,20))
print(X_1)
print(X_2)
print(X_3)
print(A)



Y = []
for i in range(8):
    Yx = A[0] + X_1[i]*A[1] + X_2[i]*A[2] + X_3[i]*A[3]
    Y.append(Yx)
print(Y)



#Дякую за зауваження, побачив що можна оптімізувати!

X_0 = []

X_0.append((max(X_1) + min(X_1)) / 2)
X_0.append((max(X_2) + min(X_2)) / 2)
X_0.append((max(X_3) + min(X_3)) / 2)
print(X_0)

Y_0 = A[0] + X_0[0]*A[1] + X_0[1]*A[2] + X_0[2]*A[3]
print(Y_0)


#Дякую за зауваження, побачив що можна оптімізувати!

Dx = []

Dx.append(X_0[0] - min(X_1))
Dx.append(X_0[1] - min(X_2))
Dx.append(X_0[2] - min(X_3))
print(Dx)


Norm_X_1 = []
Norm_X_2 = []
Norm_X_3 = []
for i in range(8):
    Norm_X1 = (X_1[i] - X_0[0]) / Dx[0]
    Norm_X2 = (X_1[i] - X_0[1]) / Dx[1]
    Norm_X3 = (X_1[i] - X_0[2]) / Dx[2]
    Norm_X_1.append(Norm_X1)
    Norm_X_2.append(Norm_X2)
    Norm_X_2.append(Norm_X3)
print(Norm_X_1)




Q = []
for i in range(8):
        Qx = (Y[i] - Y_0)*(Y[i] - Y_0)
        Q.append(Qx)
print(Q)
print("Variant number 227 Ultimate result(min((Y-Y0)^2):",min(Q))
