import turtle

def square(side):
  for _ in range(4):
    turtle.forward(side)
    turtle.left(90)

for _ in range(8):
  turtle.left(45)
  square(120)
