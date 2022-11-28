import random
from pico2d import *
import game_world
import game_framework
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
            # Ball.image.clip_draw_to_origin()
        self.x, self.y= random.randint(0, server.background.w - 1),\
                        random.randint(0, server.background.h - 1)

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        # fill here
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def handle_collision(self, other, group):
        game_world.remove_object(self)
