from turtle import *

n = 3

for x in range(4):
    if x % 2 ==1:
        pencolor("Red")
    else:
        pencolor("Blue")
    for i in range(n):
        forward(100)
        left(360/n)
    n = n+1

mainloop()