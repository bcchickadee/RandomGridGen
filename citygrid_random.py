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
    if 0<=Token<0.25:
        turtle.fd(10)
    elif 0.24<=Token<0.5:
        turtle.rt(90)
        turtle.fd(10)
    elif 0.5<=Token<0.75:
        turtle.rt(180)
        turtle.fd(10)
    else:
        turtle.rt(270)
        turtle.fd(10)

turtle.pu()
print('Operation complete.')
