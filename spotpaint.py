# import colorgram
# rgb = []
# colors = colorgram.extract('projects/hirst.jpg', 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new = (r, g, b)
#     rgb.append(new)
# print(rgb)
import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
cl_list = [(227, 229, 81), (100, 242, 167), (224, 56, 146), (176, 9, 88), (218, 125, 181), (215, 156, 92), (42, 13, 180), (35, 203, 70), (114, 157, 217), (80, 213, 109), (182, 41, 133), (42, 99, 170), (239, 155, 208), (88, 97, 223), (35, 135, 61), (143, 89, 45), 
(85, 8, 44), (20, 21, 89), (177, 162, 20), (171, 172, 242), (231, 62, 55), (81, 239, 246), (49, 21, 248), (72, 32, 15), (199, 11, 7), (15, 103, 45)]

tim.setheading(215)
tim.forward(330)
tim.setheading(0)

dots = 100

for i in range(1, dots+1):
    tim.dot(23, random.choice(cl_list))
    tim.forward(50)

    if i % 10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()