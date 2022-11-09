from pico2d import *
import game_world
import game_framework

# 10픽셀당 18cm
# 30km/h

PIXEL_PER_METER = (10.0/ 0.18)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class FLY:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1500:
            self.dir = -1
        elif self.x < 50:
            self.dir = 1
        # self.x = clamp(0, self.x, 1600)

    @staticmethod
    def draw(self):
        if self.dir == 1:
            if (int(self.frame)) >= 0 and (int(self.frame)) <= 4:
                self.image.clip_draw(int(self.frame) * 182, 168 * 2, 182, 168,
                                     self.x + 25, self.y - 25, 100, 100)
            elif (int(self.frame)) >= 5 and (int(self.frame)) <= 9:
                self.image.clip_draw((int(self.frame) - 5) * 182, 168 * 1, 182, 168,
                                     self.x + 25, self.y - 25, 100, 100)
            elif (int(self.frame)) >= 10 and (int(self.frame)) <= 13:
                self.image.clip_draw((int(self.frame) - 10) * 182, 0, 182, 168,
                                     self.x + 25, self.y - 25, 100, 100)
        elif self.dir == -1:
            if (int(self.frame)) >= 0 and (int(self.frame)) <= 4:
                self.image.clip_composite_draw(int(self.frame) * 182, 168 * 2, 182, 168, 0, 'h',
                                     self.x + 25, self.y - 25, 100, 100)
            elif (int(self.frame)) >= 5 and (int(self.frame)) <= 9:
                self.image.clip_composite_draw((int(self.frame) - 5) * 182, 168 * 1, 182, 168, 0, 'h',
                                     self.x + 25, self.y - 25, 100, 100)
            elif (int(self.frame)) >= 10 and (int(self.frame)) <= 13:
                self.image.clip_composite_draw((int(self.frame) - 10) * 182, 0, 182, 168, 0, 'h',
                                     self.x + 25, self.y - 25, 100, 100)

class Bird:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dir, self.face_dir = 1, 1
        self.frame = 0
        if Bird.image == None:
            self.image = load_image('bird_animation.png')

        self.event_que = []
        self.cur_state = FLY
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)
