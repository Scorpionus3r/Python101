Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> for i in range(36):
...     tao.penup()
...     tao.forward(200)
...     tao.left(90)
...     tao.pendown()
...     tao.forward(200)
...     tao.left(90)
...     tao.forward(200)
...     tao.left(90)
...     tao.penup()
...     tao.forward(200)
...     tao.left(90)
...     tao.pendown()
...     tao.left(10)
... 
...     
