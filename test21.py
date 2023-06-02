from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 600)

pac = sprite.add("pacman", 100, 100, "player1")
ghost = sprite.add("pacman", 500, 300,"enemy_yellow_right2", False)
time1=time.time()

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def visible(pos_x,pos_y):

    sprite.move_to(ghost,pos_x,pos_y)
    sprite.show(ghost)


@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def  visible_off():
    sprite.hide(ghost)


@wrap.on_mouse_move()
def dv_mouse(pos_x,pos_y):

    sprite.move_to(ghost,pos_x,pos_y)


@wrap.always(10)
def always():

    timer=time.time()-time1
    print(timer)
    x_ghost=sprite.get_x(ghost)
    y_ghost = sprite.get_y(ghost)
    visible = sprite.is_visible(ghost)
    if visible==True:
        sprite.set_angle_to_point(pac,x_ghost,y_ghost)
        sprite.move_at_angle_point(pac,x_ghost,y_ghost,5)

@wrap.on_close()
def remove():

    sprite.add_text("О нет!",sprite.get_x(pac),sprite.get_y(pac)-35,text_color=[255,255,255])
@wrap.on_key_always(wrap.K_RIGHT)
def pravo_dvighenie():
    angle = sprite.get_angle(pac)
    sprite.set_angle(pac, angle + 45)


@wrap.on_key_always(wrap.K_LEFT)
def left_dv():
    angle = sprite.get_angle(pac)
    sprite.set_angle(pac, angle - 45)


@wrap.on_key_always(wrap.K_UP)
def pramo():
    sprite.move_at_angle_dir(pac, 10)
