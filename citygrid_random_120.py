import turtle
import random

while True:
    try:
        Num=int(input('Number of random movements: '))
    except ValueError:
        print('Enter a valid integer.\n')
    if Num<=0:
        print('Enter a valid integer larger than 0.\n')
    else:
        break

turtle.title("Random Grid Generation of "+str(Num)+" steps")
turtle.ht()
turtle.pd()
for i in range(Num):
    print('Operation '+str(i+1)+' of '+str(Num))
    Token=random.uniform(0, 1)
    if 0<=Token<(1/3):
        turtle.fd(10)
    elif (1/3)<=Token<(2/3):
        turtle.rt(60)
        turtle.fd(10)
    else:
        turtle.lt(60)
        turtle.fd(10)

turtle.pu()
print('Operation complete.')
