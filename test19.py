from wrap import sprite, world, sprite_text, actions
import time

world.create_world(800, 600)
green_tank = sprite.add("battle_city_tanks", 100, 500, "tank_enemy_size1_green1", False)
white_tank = sprite.add("battle_city_tanks", 400, 350, "tank_enemy_size1_white1", False)
bullet = sprite.add("battle_city_items", 100, 100, "bullet", False)


def dvighenie_left(id, distanse):
    sprite.set_angle(id, -90)
    actions.move_at_angle_dir(id, distanse, 500)


def dvighenie_right(id, distance):
    sprite.set_angle(id, 90)
    actions.move_at_angle_dir(id, distance, 500)


def dvighenie_up(id, distance):
    sprite.set_angle(id, 0)
    actions.move_at_angle_dir(id, distance, 500)


def dvighenie_down(id, distance):
    sprite.set_angle(id, 180)
    actions.move_at_angle_dir(id, distance, 500)


def bullet_walk(id, bullet_distance):
    pos_1 = sprite.get_x(id)
    pos_2 = sprite.get_y(id)
    angle = sprite.get_angle(id)
    sprite.move_to(bullet, pos_1, pos_2)
    sprite.show(bullet)
    sprite.set_angle(bullet, angle)
    actions.move_at_angle_dir(bullet, bullet_distance, 2000)
    sprite.hide(bullet)


def hiide(id):
    pos_1 = sprite.get_x(id)
    pos_2 = sprite.get_y(id)
    explosion = sprite.add("battle_city_items", pos_1, pos_2, "effect_explosion1")
    sprite.hide(id)
    time.sleep(0.2)
    sprite.set_costume(explosion, "effect_explosion2")
    time.sleep(0.2)
    sprite.set_costume(explosion, "effect_explosion3")
    time.sleep(0.2)
    sprite.set_costume(explosion, "effect_explosion2")
    time.sleep(0.2)
    sprite.set_costume(explosion, "effect_explosion1")
    time.sleep(0.2)
    sprite.set_costume(explosion, "effect_explosion2")
    time.sleep(0.2)
    sprite.set_costume(explosion, "effect_explosion3")
    sprite.remove(explosion)


def poevlenie(id):
    pos_1 = sprite.get_x(id)
    pos_2 = sprite.get_y(id)
    effect = sprite.add("battle_city_items", pos_1, pos_2, "effect_appearance1")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance2")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance3")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance4")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance3")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance2")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance1")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance2")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance3")
    time.sleep(0.2)
    sprite.set_costume(effect, "effect_appearance4")
    sprite.remove(effect)
    sprite.show(id)


poevlenie(green_tank)
poevlenie(white_tank)
#
# dvighenie_left(green_tank, 200)
# bullet_walk(green_tank, 250)
# dvighenie_left(white_tank, 200)
# bullet_walk(white_tank, 250)
# dvighenie_up(green_tank, 200)
# bullet_walk(green_tank, 250)
# dvighenie_up(white_tank, 200)
# bullet_walk(white_tank, 250)
# dvighenie_right(green_tank, 200)
# bullet_walk(green_tank, 250)
# dvighenie_right(white_tank, 200)
# bullet_walk(white_tank, 250)
# dvighenie_down(white_tank, 200)
# bullet_walk(green_tank, 250)
# dvighenie_down(green_tank, 200)
# bullet_walk(white_tank, 250)
hiide(green_tank)
hiide(white_tank)