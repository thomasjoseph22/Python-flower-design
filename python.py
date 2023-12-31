from turtle import*
import colorsys
bgcolor("black")
tracer(10)
speed(0)
pensize(8)
h=0
for i in range(400):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.2
    color(c)
    circle(90+i,100)
    for j in range(10):
        circle(7,10)
done()    