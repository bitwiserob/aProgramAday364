import pyglet
import random
import load
game_window = pyglet.window.Window(800,600)
pyglet.resource.path = ['./imgs']
pyglet.resource.reindex()

tank_image = pyglet.resource.image('car_img.png')
good_zone = pyglet.resource.image('good_zone.png')
bad_zone = pyglet.resource.image('bad_zone.png')

main_batch = pyglet.graphics.Batch()
score_label = pyglet.text.Label(text='score: 0', x=10, y=575, batch=main_batch)

player_spr = pyglet.sprite.Sprite(
    img=tank_image, x=400, y=300, batch=main_batch)
bad_spr = pyglet.sprite.Sprite(img=bad_zone)
good_spr = pyglet.sprite.Sprite(img=good_zone)


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
center_image(tank_image)
center_image(good_zone)
center_image(bad_zone)
bad_zones = load.load_bad_zones(2, player_spr.position, main_batch)
player_lives = load.player_lives(3,main_batch)
print(player_spr.position)
game_objects = [player_spr] + bad_zones 

def update(dt):
    for obj in game_objects:
        obj.update(dt)

@game_window.event
def on_draw():
    main_batch.draw()
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
