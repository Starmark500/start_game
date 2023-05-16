import time

from wrap import world, sprite, sprite_text, actions

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 300, 100, "player2")
hunter = sprite.add("pacman", 100, 100, "enemy_blue_right1")
def text(words,who_speak):
    text = sprite.add_text(words,sprite.get_x(who_speak),sprite.get_top(who_speak) - 20)

    time.sleep(0.5)
    sprite.remove(text)



def escape(disstans,hoj):
#побег
    text("Бежим!",victim)
    actions.set_size_percent(victim, 30, 30, 500)
    actions.set_angle(victim, disstans, 500)
    actions.move_at_angle_dir(victim,hoj, 600)

    actions.set_size_percent(victim, 100, 100, 500)


def funal(distance_ghost):
#погоня
    text("В погоню!",hunter)
    actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), distance_ghost, 500)


escape(-135,100)

funal(20)
escape(180,150)
funal(109)
escape(-57,40)
funal(240)
text("Ты меня поймал!",victim)






