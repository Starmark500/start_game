import wrap, time

wrap.world.create_world(300, 800)
mario = wrap.sprite.add("mario-1-big", 50, 500, "walk1")
dragon = wrap.sprite.add("mario-enemies", 250, 400, "dragon_stand1")

speed_fire_x = 2

speed_mario = -21
speed_dragon = -15
no_time = time.time()
clock = 0
stem = wrap.sprite.add_text(str(clock), 25, 50, text_color=[255, 255, 255], font_size=35)
bullet_1 = 0


while True:
    x_dragon = wrap.sprite.get_x(dragon)
    y_dragon = wrap.sprite.get_y(dragon)
    clock = time.time() - no_time
    clock = int(clock)
    print(clock)
    wrap.sprite_text.set_text(stem, str(clock))
    bullet = time.time() - bullet_1
    if bullet >=5:

        x_mario = wrap.sprite.get_x(mario)
        y_mario = wrap.sprite.get_y(mario)
        print("Бум!прошло" + str(bullet))
        bullet_1 = time.time()
        fire_ball = wrap.sprite.add("mario-enemies", x_mario + 50, y_mario, "fire_stream")
    wrap.sprite.move_at_angle_point(fire_ball, x_dragon,y_dragon,10)
    wrap.sprite.set_angle_to_point(fire_ball,x_dragon,y_dragon)
    wrap.sprite.is_collide_sprite(fire_ball,dragon)
    wrap.sprite.move(mario, 0, speed_mario)
    mario_y_top = wrap.sprite.get_top(mario)
    mario_bottom = wrap.sprite.get_bottom(mario)

    if mario_y_top <= 0:
        wrap.sprite.move_top_to(mario, 0)

        speed_mario = 5
    if mario_bottom >= 800:
        wrap.sprite.move_bottom_to(mario, 800)
        speed_mario = -5

    wrap.sprite.move(dragon, 0, speed_dragon)
    dragon_y_top = wrap.sprite.get_top(dragon)
    dragon_bottom = wrap.sprite.get_bottom(dragon)

    if dragon_y_top <= 0:
        wrap.sprite.move_top_to(dragon, 0)
        speed_dragon = 7
    if dragon_bottom >= 800:
        wrap.sprite.move_bottom_to(dragon, 800)
        speed_dragon = -15
