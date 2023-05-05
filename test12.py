import wrap,random
x_mario=random.randint(20,680)
y_mario=random.randint(20,780)
x_player=random.randint(20,680)
y_player=random.randint(20,780)

wrap.world.create_world(700,800)
wrap.world.set_back_color(109,45,37)

ghost=wrap.sprite.add("pacman",x_mario,y_mario,"enemy_blue_down1")
numplayer=wrap.sprite.add("pacman",x_player,y_player,"player2")
wrap.actions.set_size(numplayer,20,20)


if y_player <=y_mario:
    wrap.sprite.set_costume(ghost,"enemy_blue_up1")
else:
    wrap.sprite.set_costume(ghost, "enemy_blue_down2")
wrap.actions.move_to(ghost,x_mario,y_player)


if x_player >= x_mario:
    wrap.sprite.set_costume(ghost,"enemy_blue_right1")
else:
    wrap.sprite.set_costume(ghost,"enemy_blue_left1")
wrap.actions.move_to(ghost,x_player,y_player)

