"""
    Example from Professor Fernando Masanori, a great pythonist, a giver of the community
"""

import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# indexes   0       1        2        3        4         5
turtle.bgcolor('black')
t = turtle.Pen()
for x in range(360):
    print('o valor do x é: ', x)
    # Esse loop vai ser repetido 360 vezes.
    t.color(colors[x % 6])
    t.width(x / 100 + 1)
    # Adaptação da velocidade por sugestão do Bruno
    t.speed(x + 1)
    # print(x / 100 + 1)
    t.forward(x)
    t.left(59)
# t.pu()
# t.home()
# t.pd()
# for x in range(360):
#    t.color('white')
#    t.width((x / 100 + 1)/3)
#    t.speed(1000)
#    t.forward(x)
#    t.left(59)
# colors2 = ['chartreuse', 'yellow2', 'dark orange', 'firebrick', 'HotPink1', 'SkyBlue1']
v = 360
for x in range(360):
    # t.color(colors[x % 6])
    t.color('white')
    t.width((v / 100 + 1) / 2)
    t.speed(10000)
    t.left(-59)
    t.backward(v)
    v -= 1
