import wrap, random

wrap.world.create_world(600, 800)

a = random.randint(10, 590)
b = random.randint(390, 790)
c = random.randint(10, 590)
d = random.randint(90, 390)
e = random.randint(20, 120)
run=random.randint(100,300)



pacman = wrap.sprite.add("pacman", a, b, "player2")
wrap.sprite.set_size(pacman, e, e)

wrap.sprite.add("pacman", c, d, "dot")

text = wrap.sprite.add_text("О еда!", a, b - 50, text_color=[255, 255, 255])
wrap.actions.set_angle_to_point(pacman, c, d)
wrap.sprite.remove(text)
wrap.actions.move_to(pacman, c, d)

pacmanx=wrap.sprite.get_x(pacman)

top = wrap.sprite.get_top(pacman)
print(top)
wrap.sprite.add("pacman",pacmanx, top - 20, "enemy_blue_down1")
wrap.sprite.add_text("Ага,попался!",pacmanx,top-50,text_color=[255,255,255])
wrap.sprite.add("pacman",650,300)

pacmanangle=wrap.sprite.get_angle(pacman)
wrap.sprite.set_angle(pacman,pacmanangle-180)
wrap.actions.move_at_angle_dir(pacman,run)
