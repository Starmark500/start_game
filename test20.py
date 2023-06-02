from wrap import sprite, world, sprite_text, actions
import time,random

world.create_world(800, 600)

sec=random.randint(20,150)

ball=sprite.add("mario-enemies",400,300,"armadillo_egg")
sprite.set_size_percent(ball,sec,sec)
footballer1=sprite.add("mario-1-big",200,175,"stand")
footballer2=sprite.add("mario-2-big",500,300,"stand")
footballer3=sprite.add("mario-1-small",600,150,"walk2")
sprite.set_reverse_x(footballer3,True)
sprite.set_reverse_x(footballer2,True)

def perekat_ball(id):
    width_ball = sprite.get_width(ball)
    height_ball = sprite.get_height(ball)
    right1_sprite = sprite.get_right(id)
    right_sprite = sprite.get_bottom(id)
    left = sprite.get_left(id)
    angle=sprite.get_angle(id)
    if angle == 90:
        width_ball=sprite.get_width(ball)
        height_ball=sprite.get_height(ball)
        right1_sprite=sprite.get_right(id)
        right_sprite=sprite.get_bottom(id)
        actions.move_to(ball, right1_sprite+width_ball/2,right_sprite -(height_ball/2), 1000)
    if angle == -90:
        actions.move_to(ball,left-width_ball/2,right_sprite-height_ball/2)




perekat_ball(footballer1)
perekat_ball(footballer2)
perekat_ball(footballer3)
