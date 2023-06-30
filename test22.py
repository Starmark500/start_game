import math

from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 600)

bali = 0
timer_death = 3
tp_tank_sec=2


chet = sprite.add_text(str(bali), 50, 50, text_color=[255, 255, 255])
timers = sprite.add_text(str(timer_death), 750, 550, text_color=[255, 255, 255])

width = 20
height = 20

aim = sprite.add("pacman", 100, 100, "player2", False)
sprite.set_angle(aim, 0)
size = sprite.set_size(aim, width, height)
green_tank = sprite.add("battle_city_tanks", 100, 100, "tank_enemy_size1_green1")

@wrap.on_key_down(wrap.K_UP)
def aims():
    global height, width
    sprite.set_size(aim, width, height)
    sprite.show(aim)

    if width == 20 and height == 20:
        width = width + 20
        height = height + 20
    elif width == 40 and height == 40:
        width = width + 20
        height = height + 20
    elif width == 60 and height == 60:
        width = width + 20
        height = height + 20

    elif width == 80 and height == 80:
        sprite.hide(aim)
        width = 20
        height = 20


@wrap.on_mouse_move
def dv_aim(pos_x, pos_y):
    sprite.move_to(aim, pos_x, pos_y)


@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def new_skin(pos_x, pos_y):
    global bali, chet, timer_death

    if (sprite.is_collide_sprite(aim, green_tank) and sprite.is_visible(aim)) or \
            (sprite.is_visible(aim) == False and sprite.is_collide_point(green_tank, pos_x, pos_y)):
        sprite.set_costume_next(green_tank)
        bali += 1
        sprite_text.set_text(chet, str(bali))
        timer_death = 3
        sprite_text.set_text(timers, str(timer_death))


@wrap.always(100)
def timer():
    global timer_death
    timer_death2 = round(timer_death, 2)
    timer_death -= 0.1
    sprite_text.set_text(timers, str(timer_death2))

    if timer_death < 0:
        sprite.add_text("GAME OVER!", 400, 300, font_size=100, text_color=[255, 0, 10])
        timer_death = 99


@wrap.always(100)
def yskorenie():
    global tp_tank_sec
    tp_tank_sec -= 0.1

    if tp_tank_sec < 0:
        y_r = random.randint(100, 500)
        x_r = random.randint(100, 700)
        sprite.move_to(green_tank, x_r, y_r)
        tp_tank_sec = 2

