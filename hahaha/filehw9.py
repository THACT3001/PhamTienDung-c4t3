from turtle import *

speed(-1)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
begin_fill()
for x in range(3):
    for i in range(4):
        forward(100)
        right(90)
    backward(50)
forward(50)
right(90)
forward(50)
forward(50)
right(90)
forward(50)
right(90)
forward(100)
end_fill()





mainloop()