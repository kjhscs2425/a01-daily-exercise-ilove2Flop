import turtle

turtle.shape("turtle")

for i in range(0,2):
 turtle.forward(100)
 turtle.backward(200)
 turtle.forward(100)
 turtle.right(60)
turtle.forward(100)
turtle.backward(200)
turtle.left(60)
for j in range(0,6):
 turtle.forward(100)
 turtle.right(60)
 
turtle.exitonclick()