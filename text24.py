from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 800)
world.set_back_color(100, 150, 100)
block=sprite.add("battle_city_items",400,795,"block_brick")
sprite.set_width(block,800)
mario=sprite.add("mario-1-big",400,0,"walk1")
block_top=sprite.get_top(block)
sprite.move_bottom_to(mario,block_top)

@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def move_mario(keys):
    if wrap.K_RIGHT in keys:
        sprite.set_reverse_x(mario,False)
        sprite.move_at_angle_dir(mario,5)
    else:
        sprite.set_reverse_x(mario,True)
        sprite.move_at_angle_dir(mario, 5)
@wrap.on_key_up(wrap.K_SPACE)
def move_mario(keys,pos_x,pos_y):
    global m_x,m_y,ang_mario
    ang_mario=sprite.get_angle(mario)
    m_x=sprite.get_x(mario)
    m_y=sprite.get_y(mario)
    sprite.set_costume(mario, "swim3")

@wrap.always(10)
def go_centr(keys,pos_x,pos_y):
    m_s=sprite.get_costume(mario)

    if m_s=="swim3":
        mouse_pos = sprite.calc_angle_by_point(mario, pos_x, pos_y)
        sprite.set_angle(mario,mouse_pos+90)
        sprite.move_at_angle_point(mario,pos_x,pos_y,7)

        # sprite.set_angle_to_point(mario, pos_x, pos_y)
        # sprite.move_at_angle_dir(mario, 2)


@wrap.on_key_up(wrap.K_DOWN)
def go_niz(keys,pos_x,pos_y):
    sprite.set_costume(mario,"stand")
    sprite.move_at_angle_dir(mario,5)
    sprite.set_angle_to_point(mario,m_x,m_y)
    sprite.set_angle(mario,ang_mario)
    sprite.move_bottom_to(mario, block_top)
