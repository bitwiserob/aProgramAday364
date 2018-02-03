import pyglet
import random
import load
game_window = pyglet.window.Window()
pyglet.resource.path = ['./imgs']
pyglet.resource.reindex()

tank_image = pyglet.resource.image('car_img.png')
good_zone = pyglet.resource.image('good_zone.png')
bad_zone = pyglet.resource.image('bad_zone.png')

player_spr = pyglet.sprite.Sprite(img=tank_image, x=400, y=300)
bad_spr = pyglet.sprite.Sprite(img=bad_zone)
good_spr = pyglet.sprite.Sprite(img=good_zone)


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
center_image(tank_image)
center_image(good_zone)
center_image(bad_zone)
bad_zones = load.load_bad_zones(3)

@game_window.event
def on_draw():
    game_window.clear()
    player_spr.draw()
    for zone in bad_zones:
    	zone.draw()
if __name__ == '__main__':
    pyglet.app.run()
