import time, wrap
wrap.world.set_back_color(250,200,255)
wrap.world.create_world(650,700)
wrap.sprite.add("mario-princess",400,350)
time.sleep(0.5)
wrap.sprite.add_text("Кто тут?",400,400)
time.sleep(1.5)
wrap.sprite.add("pacman",200,300,costume="enemy_blue_down1")
time.sleep(1)
wrap.sprite.add_text("я тут!",200,350)
time.sleep(1.5)
wrap.sprite.add("pacman",200,450,costume="enemy_ill_white1")
time.sleep(1)
wrap.sprite.add_text("Кажись ты что-то перепутала",200,400)
time.sleep(1)
wrap.sprite.add_text("Нет,Я жду своего Марио!",400,450)
time.sleep(1.5)
wrap.sprite.add_text("Чтож,его тут точно нету",200,500)
time.sleep(1)
wrap.sprite.add_text("Да!Его тут нет!",200,250)
time.sleep(1.5)
wrap.sprite.add("mario-1-big",500,450,costume="walk3")
wrap.actions.move_top_to(9,300)
wrap.actions.set_angle(9,300)
time.sleep(0.5)
wrap.sprite.add_text("Я ТУТ!!!",500,400)

