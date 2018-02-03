import pyglet

window = pyglet.window.Window(512,512)
back_img = pyglet.image.load('./imgs/back.png')
car_img = pyglet.sprite.Sprite(pyglet.image.load('./imgs/car_img.png'),x=50,y=50)
label = pyglet.text.Label('hello, world',
						 font_name='Times New Roman',
						 font_size = 36,
						 x=window.width//2, y=window.height//2,
						 anchor_x='center', anchor_y='center')

@window.event
def on_draw():
	window.clear()
	back_img.blit(0,0)
	car_img.draw()
	
pyglet.app.run()