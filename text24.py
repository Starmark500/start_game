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
        sprite.move_at_angle_dir(mario, 10)
@wrap.on_key_always(wrap.K_SPACE)
def move_mario(keys,pos_x,pos_y):
   sprite.set_costume(mario,"swim3")
   sprite.move_at_angle_dir(mario,pos_x,pos_y)