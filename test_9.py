import wrap
width=600
height=600
x1=200
y1=100
x2=520
y2=300
x3=140
y3=400
wrap.world.create_world(width,height)
wrap.world.set_back_color(255,183,65)
wrap.sprite.add("pacman",20,20,costume="enemy_blue_down1")
wrap.sprite.add("pacman",20,height-20,"enemy_pink_down1")
wrap.sprite.add("pacman",width-20,20,"enemy_red_down1")
wrap.sprite.add("pacman",width-20,height-20,"enemy_yellow_down1")
wrap.sprite.add("pacman",width/2,height/2,"player2")
wrap.sprite.add("pacman",x1,y1)
wrap.sprite.add("pacman",x2,y2)
wrap.sprite.add("pacman",x3,y3)
wrap.sprite.add_text("1 fullstop",x1,y1-30)
wrap.sprite.add_text("2 fullstop",x2,y2-30)
wrap.sprite.add_text("3 fullstop",x3,y3-30)
wrap.actions.move_to(4,width/2,y1)
wrap.actions.move_to(4,x1,y1)
wrap.actions.move_to(4,x1,y2)
wrap.actions.move_to(4,x2,y2)
wrap.actions.move_to(4,x2,y3)
wrap.actions.move_to(4,x3,y3)