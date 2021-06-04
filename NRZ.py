import matplotlib.pyplot as plt

N = int(input("Number of Bits to be Transmitted : "))
y = []
y.append(0)
for n in range(0, N):
    x = int(input(""))
    y.append(x)

def nrz_l():
    y1 = []
    for i in y:
        i = (-1 if i == 0 else i)
        y1.append(i)
    return y1

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

def titles(m):
    plt.subplot(3, 1, m)
    plt.xlabel('Time')
    plt.ylabel('Amp')
    plt.tight_layout()
    plt.grid()

plt.figure(1)
x = range(0, N+1)

titles(1)
plt.step(x, nrz_l(), color='g')
plt.title('NRZ-L')
plt.xticks(x)

titles(2)
plt.step(x, nrz_m(), color='b')
plt.title('NRZ-M')
plt.xticks(x)

titles(3)
plt.step(x, nrz_s(), color='k')
plt.title('NRZ-S')
plt.xticks(x)

plt.show()

print("Programmed by Akash U Kulkarni")
