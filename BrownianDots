import matplotlib.pyplot as plt
import random
import math

while True:
    try:
        Num=int(input('Number of dots: '))
    except ValueError:
        print('Enter a valid integer.\n')
    if Num<=0:
        print('Enter a valid integer larger than 0.\n')
    else:
        break

while True:
    try:
        Trials=int(input('Number of trials: '))
    except ValueError:
        print('Enter a valid integer.\n')
    if Num<=0:
        print('Enter a valid integer larger than 0.\n')
    else:
        break

for i in range(Num):
    x=0
    y=0
    for j in range(Trials):
        theta=random.uniform(0, 2*math.pi)
        x=x+math.cos(theta)
        y=y+math.sin(theta)
    plt.plot(x, y, 'bo')

plt.title('Brownian Motion Visualized: '+str(Num)+' Dots with '+str(Trials)+' Trials')
plt.show()
