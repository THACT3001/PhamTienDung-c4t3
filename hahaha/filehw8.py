from turtle import *

speed(-1)

n = 3

for x in range(5):
    if n == 3:
        pencolor("Red")
    elif n == 4:
        pencolor("Blue")
    elif n == 5:
        pencolor("Brown")
    elif n == 6:
        pencolor("Yellow")
    else:
        pencolor("Grey")
    for i in range(n):
        forward(100)
        left(360/n)
    n = n+1

mainloop()