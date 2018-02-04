import pyglet
import random
import math
pyglet.resource.path = ['./imgs']
pyglet.resource.reindex()
bad_zone = pyglet.resource.image('bad_zone.png')
tank_image = pyglet.resource.image('car_img.png')

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def load_bad_zones(num_zones, player_pos,batch=None):
    zones = []
    for i in range(num_zones):
        zone_red_x = random.randint(0, 800)
        zone_red_y = random.randint(0, 600)
        if (zone_red_y, zone_red_x) == player_pos:
            while(zone_red_y, zone_red_x):
                zone_red_x = random.randint(0, 800)
                zone_red_y = random.randint(0, 600)
        new_red_zone = pyglet.sprite.Sprite(
            img=bad_zone, x=zone_red_x, y=zone_red_y,batch=batch)
        zones.append(new_red_zone)
    return zones

def player_lives(num_icons, batch=None):
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=tank_image,x=785-i*30,y=585, batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives