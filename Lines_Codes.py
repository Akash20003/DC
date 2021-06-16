'Line Codes'
'Uni-Polar, Bi-Polar, Polar NRZ and RZ'
#Imports Matplotlib to plot the Graph
import matplotlib.pyplot as plt
#Imports Numpy Lib
import numpy as np

#Accepts Inputs from User
N = int(input("Number of Bits to be Transmitted : "))
y = []
y.append(0)
for n in range(0, N):
    x = int(input(""))
    y.append(x)

#This Function returns Polar NRZ Values
def pol():
    y1 = []
    for i in y:
        i = (-1 if i == 0 else i)
        y1.append(i)
    return y1

#This Function returns Bi-Polar NRZ Values
def bi():
    y2 = []
    a = 0
    for i in y:
        if i == 1:
            a += 1
            b = range(0, N, 2)
            i = (-1 if a in b else i)
        y2.append(i)
    return y2

#This Function returns Uni-Polar RZ Values
def uni_rz():
    y3 = []
    for i in y:
        i = (0 if i == 0 else i)
        j = 0
        y3.append(i)
        y3.append(j)
    y3.pop(0)
    return y3

#This Function returns Polar RZ Values
def pol_rz():
    y4 = []
    for i in y:
        i = (-1 if i == 0 in range(0, N, 2) else i)
        y4.append(i)
    y5 = []
    for i in y4:
        i = (1 if i == 1 else -1)
        j = 0
        y5.append(i)
        y5.append(j)
    y5.pop(0)
    return y5

#This Function returns Bi-Polar RZ Values
def bi_rz():
    y6 = []
    a = 0
    for i in y:
        if i == 1:
            a += 1
            b = range(0, N, 2)
            i = (-1 if a in b else i)
        y6.append(i)
    y7 = []
    for i in y6:
        i = {i == 1: 1, i == -1: -1}.get(True, 0)
        j = 0
        y7.append(i)
        y7.append(j)
    y7.pop(0)
    return y7

#This Function returns Titles and etc to plot the Graph
def titles(m):
    plt.subplot(3, 1, m)
    plt.xlabel('Time')
    plt.ylabel('Amp')
    plt.tight_layout()
    plt.grid()

#Plotting Starts :

#Figure 1 with x-axis
plt.figure(1)
x = range(0, N+1)

#Plots Uni-Polar NRZ
titles(1)
plt.step(x, y)
plt.title('Uni-Polar NRZ')
plt.xticks(x)

#Plots Polar NRZ
titles(2)
plt.step(x, pol(), color='g')
plt.title('Polar NRZ')
plt.xticks(x)

#Plots Bi-Polar NRZ
titles(3)
plt.step(x, bi(), color='r')
plt.title('Bi-Polar NRZ')
plt.xticks(x)

#Figure 2 with Change in x-axis
plt.figure(2)
x1 = np.arange(0, (N+2)-1.5, 0.5)

#Plots Uni-Polar RZ
titles(1)
plt.step(x1, uni_rz(), color='purple')
plt.xticks(x1)
plt.title('Uni-Polar RZ')

#Plots Polar RZ
titles(2)
plt.step(x1, pol_rz(), color='c')
plt.xticks(x1)
plt.title('Polar RZ')

#Plots Bi-Polar RZ
titles(3)
plt.step(x1, bi_rz(), color='m')
plt.xticks(x1)
plt.title('Bi-Polar RZ')

#Shows the Graph
plt.show()

print("Programmed by Akash U Kulkarni")
