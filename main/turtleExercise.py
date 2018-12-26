# coding=utf-8
import turtle


turtle.speed(2)
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.forward(100)
turtle.right(30)
turtle.forward(100)
turtle.goto(0, 0)       # 画到指定坐标点
turtle.up()     # 抬笔
turtle.goto(0, 110)
turtle.down()   # 落笔
turtle.goto(-100, 0)
turtle.goto(0, 0)
turtle.left(30)
turtle.backward(200)
turtle.setheading(90)   # 调整小海龟朝向

turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(100, steps=5)
turtle.end_fill()

# turtle.reset()          # 清空窗口，重置turtle状态

turtle.done()
'''
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150, -120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))

turtle.mainloop()

'''
