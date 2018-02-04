from pyglet import *
import physicalobject
pyglet.resource.path = ['./imgs']
pyglet.resource.reindex()

tank_image = pyglet.resource.image('car_img.png')
class Player(physicalobject.PhysicalObject):
    def __init__(self,*args, **kwargs):
        super().__init__(img=tank_image,*args,**kwargs)
        self.thrust=300.0
        self.rotate=200.0
        self.key_handler = key.KeyStateHandler()
    def update(self, dt):
        super(Player, self).update(dt)