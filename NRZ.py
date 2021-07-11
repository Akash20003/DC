'NRZ-L, NRZ-M and NRZ-S'
#Imports Matplotlib to Plot
import matplotlib.pyplot as plt

#Accepts inputs from User
N = int(input("Number of Bits to be Transmitted : "))
y = []
y.append(0)
for n in range(0, N):
    x = int(input(""))
    y.append(x)

#This Function Returns NRZ-L Values
def nrz_l():
    y1 = []
    for i in y:
        i = (-1 if i == 0 else i)
        y1.append(i)
    return y1

#This Function Returns NRZ-M Values
def nrz_m():
    y2 = []
    y3 = []
    j = 0
    for i in y:
        j = j ^ i
        y2.append(j)
    for i in y2:
        i = (-1 if i == 0 else i)
        y3.append(i)
    return y3

#This Function Returns NRZ-S Values
def nrz_s():
    j = 0
    y4 = []
    y5 = []
    def xnor(a, b):
        return 1 if a == b else 0
    for i in y:
        j = xnor(i, j)
        y4.append(j)
    for i in y4:
        i = (1 if i == 0 else -1)
        y5.append(i)
    return y5

#This Function gives Titles n etc.,
def titles(m):
    a = {1 : "NRZ-L", 2 : "NRZ-M", 3 : "NRZ-S"}
    plt.subplot(3, 1, m)
    plt.title(a[m])
    plt.xlabel('Time')
    plt.ylabel('Amp')
    plt.tight_layout()
    plt.grid()
    plt.xticks(x)

#Plotting Starts :
#Figure 1 and x-axis
plt.figure(1)
x = range(0, N+1)

#Plots NRZ-L
titles(1)
plt.step(x, nrz_l(), color='g')

#Plots NRZ-M
titles(2)
plt.step(x, nrz_m(), color='b')

#Plots NRZ-S
titles(3)
plt.step(x, nrz_s(), color='k')

#Shows the Graph
plt.show()

print("Programmed by Akash U Kulkarni")