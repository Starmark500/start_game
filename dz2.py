from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 600)

mario1=sprite.add("mario-1-big", 100, 100, "stand")
mario2=sprite.add("mario-1-small", 200, 100, "climb2")


@wrap.on_key_always(wrap.K_RIGHT)
def right():
    angle=sprite.get_angle(mario1)

    sprite.move_at_angle_dir(mario1,1)

@wrap.on_key_always(wrap.K_LEFT)
def left():
    angle = sprite.get_angle(mario1)
    if angle==90:




