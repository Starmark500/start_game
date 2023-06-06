from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 600)

v = False
sze1 = 20
sze2 = 20
aim = sprite.add("pacman", 100, 100, "player2", v)
sprite.set_angle(aim, 0)
size = sprite.set_size(aim, sze1, sze2)
green_tank = sprite.add("battle_city_tanks", 100, 100, "tank_enemy_size1_green1")


@wrap.always(500)
def tp_tank():
    y_r = random.randint(100, 500)
    x_r = random.randint(100, 700)
    sprite.move_to(green_tank, x_r, y_r)


@wrap.on_key_down(wrap.K_UP)
def aims(pos_x, pos_y):
    global sze1, sze2
    sprite.move_to(aim, pos_x, pos_y)
    sprite.show(aim)
    if v == True:
        sprite.hide(aim)
    if v == False:
        sprite.set_size(aim, sze1, sze2)
        sprite.show(aim)
    if sze1 == 20 and sze2 == 20:
        sze1 = sze1 + 20
        sze2 = sze2 + 20
    if sze1 == 40 and sze2 == 40:
        sze1 = sze1 + 20
        sze2 = sze2 + 20
    if sze1 == 60 and sze2 == 60:
        sze1 = sze1 + 20
        sze2 = sze2 + 20
    if sze1 == 80 and sze2 == 80:
        sze1 = sze1 + 20
        sze2 = sze2 + 20
