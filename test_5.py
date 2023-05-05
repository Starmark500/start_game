width=900
height=700
p1=350
p2=200
py=300





import wrap
wrap.world.create_world(width,height)
wrap.sprite.add("mario-items",p1,py,costume="cloud_platform")
wrap.sprite.add("mario-items",p2,py,costume="cloud_platform")
wrap.sprite.add("mario-items",width-50,py,"cloud_platform")
wrap.sprite.add("mario-items",50,py,"cloud_platform")
wrap.sprite.add("mario-1-big",50,py-40,"stand")
wrap.actions.move_to(4,(p1-50)/2+50,py-120)
wrap.actions.move_to(4,p1,py-40)
wrap.actions.move_to(4,p1+(p2-p1)/2,py-60)
wrap.actions.move_to(4,p2,py-40)
wrap.actions.move_to(4,p2+(width-50-p2)/2,py-60)
wrap.actions.move_to(4,width-40,py-40)
