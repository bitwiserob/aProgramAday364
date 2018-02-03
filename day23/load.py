import pyglet
import random
pyglet.resource.path = ['./imgs']
pyglet.resource.reindex()
bad_zone = pyglet.resource.image('bad_zone.png')
def load_bad_zones(num_zones):
	zones = []
	for i in range(num_zones):
		zone_red_x = random.randint(0,800)
		zone_red_y = random.randint(0,600)
		new_red_zone = pyglet.sprite.Sprite(img=bad_zone,x=zone_red_x,y=zone_red_y)
		zones.append(new_red_zone)
	return zones