from wrap import sprite, world, sprite_text, actions
import time, random, wrap
world.create_world(400,500)
a=True
x=100
y=100
@wrap.always(1000)
def iuygfv():
    global a,x,y
    if a==True:
        world.change_world(x,y)
        x+=100
        y+=100
    if x==800 and y==800:
        world.change_world(400,500)
        x=100
        y=100
