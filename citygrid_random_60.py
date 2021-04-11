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
    if 0<=Token<(1/6):
        turtle.fd(10)
    elif (1/6)<=Token<(2/6):
        turtle.rt(60)
        turtle.fd(10)
    elif (2/6)<=Token<(3/6):
        turtle.rt(120)
        turtle.fd(10)
    elif (3/6)<=Token<(4/6):
        turtle.rt(180)
        turtle.fd(10)
    elif (4/6)<=Token<(5/6):
        turtle.rt(240)
        turtle.fd(10)
    else:
        turtle.rt(300)
        turtle.fd(10)

turtle.pu()
print('Operation complete.')
