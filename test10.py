import wrap,random,math

x_9=random.randint(100,750)
y_9=random.randint(300,550)

wrap.world.create_world(800,600)
wrap.world.set_back_color(255,255,255)

wrap.sprite.add("pacman",50,50,costume="dot")
mario=wrap.sprite.add("mario-1-big",50,50,costume="stand")
princess=wrap.sprite.add("mario-princess",x_9,y_9,visible=False)

s=math.dist([50,50],[x_9,y_9])
s=int(s)
l="клад "+str(s)+" px"

wrap.sprite.add_text(l,50,70)

wrap.actions.set_angle_to_point(mario,x_9,y_9)

x_people1=input("какой x")
x_people1=int(x_people1)
y_people1=input("какой y")
y_people1=int(y_people1)

wrap.actions.move_to(mario,x_people1,y_people1)
wrap.actions.set_angle_to_point(mario,x_9,y_9)


wrap.sprite.add("pacman",x_people1,y_people1,costume="dot")
s=math.dist([x_people1,y_people1],[x_9,y_9])
s=int(s)
l="клад "+str(s)+" px"
wrap.sprite.add_text(l,x_people1,y_people1-50)

x_people1=input("какой x")
x_people1=int(x_people1)
y_people1=input("какой y")
y_people1=int(y_people1)

wrap.actions.move_to(mario,x_people1,y_people1)
wrap.actions.set_angle_to_point(mario,x_9,y_9)

wrap.sprite.add("pacman",x_people1,y_people1,costume="dot")
s=math.dist([x_people1,y_people1],[x_9,y_9])
s=int(s)
l="клад "+str(s)+" px"
wrap.sprite.add_text(l,x_people1,y_people1-50)

x_people1=input("какой x")
x_people1=int(x_people1)
y_people1=input("какой y")
y_people1=int(y_people1)

wrap.actions.move_to(mario,x_people1,y_people1)
wrap.actions.set_angle_to_point(mario,x_9,y_9)

wrap.sprite.add("pacman",x_people1,y_people1,costume="dot")
s=math.dist([x_people1,y_people1],[x_9,y_9])
s=int(s)
l="клад "+str(s)+" px"
wrap.sprite.add_text(l,x_people1,y_people1-50)

wrap.sprite.show(princess)



