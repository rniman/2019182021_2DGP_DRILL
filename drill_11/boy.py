from pico2d import *

#2. 이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, AD = range(6)

# 키 입력 확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT)  : LD,
    (SDL_KEYDOWN, SDLK_a) : AD,
    (SDL_KEYUP, SDLK_RIGHT)   : RU,
    (SDL_KEYUP, SDLK_LEFT)    : LU,

}


# 1. 상태 정의
class IDLE:  # 그룹핑 -> 변수와 함수의 묶음
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.dir = 0  # 들어오는 객체는 멈춰야한다
        self.timer = 1000
    @staticmethod
    def exit(self, event):  # 상태를 나올 때 행하는 액션
        print('EXIT IDLE')
        pass

    @staticmethod
    def do(self):  # 상태에 있을때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            # self.q.insert(0. TIMER)
            self.add_event(TIMER) # 조금더 객체 지향적

    @staticmethod
    def draw(self): # self는 IDLE객체를 뜻하는 것이 아니다
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod  # 이 함수는 객체용이 아니다
    def enter(self, event):
        print('ENTER RUN')
        # 방향을 결정 해야하는데, 어떤키가 눌렸는지에 따라
        # 키 이벤트 정보가 필요
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

        if self.dir >= 2:
            self.dir = 1
        elif self.dir <=-2:
            self.dir = -1
    @staticmethod
    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)  # clamp pico2d함수 x를 제한

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


class SLEEP:  # 그룹핑 -> 변수와 함수의 묶음
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        # self.dir = 0  # 어차피 IDLE상태에서 넘어옴

    @staticmethod
    def exit(self, event):  # 상태를 나올 때 행하는 액션
        print('EXIT IDLE')
        pass

    @staticmethod
    def do(self):  # 상태에 있을때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self): # self는 IDLE객체를 뜻하는 것이 아니다
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2, '', self.x + 25, self.y - 25, 100, 100)
        else: # 오른쪽 높이
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592/2, '', self.x + 25, self.y - 25, 100, 100)


class AUTO_RUN:
    @staticmethod  # 이 함수는 객체용이 아니다
    def enter(self, event):
        print('ENTER RUN')
        # 방향을 결정 해야하는데, 어떤키가 눌렸는지에 따라
        # 키 이벤트 정보가 필요

        if self.dir == 0:
            self.dir = self.face_dir

    @staticmethod
    def exit(self, event):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir

        self.dir = 0

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)  # clamp pico2d함수 x를 제한
        if self.x == 0 or self.x == 800:
            self.dir = self.dir * -1

    @staticmethod
    def draw(self):
        if self.dir <= -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 25, 200, 200)
        elif self.dir >= 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 25, 200, 200)



#3. 상태 변환 기술
#SLEEP 상태 추가
next_state = {
    SLEEP:{RD: RUN, LD: RUN, RU: RUN, LU: RUN, TIMER: SLEEP, AD: SLEEP},
    IDLE:{RU:RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU:IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AD: AUTO_RUN},
    AUTO_RUN: {RD: RUN, LD: RUN, RU: AUTO_RUN, LU: AUTO_RUN, AD: IDLE}
}


class Boy:
    def add_event(self, event):
        self.q.insert(0, event)

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.q = []  # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None)  # 초기 상태의 entry 액션 수행

    def update(self):
        self.cur_state.do(self)  # 현재 상태의 do 액션 수행

        # 이벤트를 확인하여 이벤트가 있으면 이벤트 변환 처리
        if self.q:  # 큐에 이벤트가 있다면 -> 이벤트 발생
            event = self.q.pop()
            self.cur_state.exit(self, event)  # 현재 상태 나가기
            self.cur_state = next_state[self.cur_state][event]  # 다음 상태 들어가기
            self.cur_state.enter(self, event)  # 다음 상태의 entry action 수행

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)  # 객체를 매게뱐수로 전달


    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            # self.q.insert(0, key_event)
            self.add_event(key_event)
        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir += 1
        #             boy.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir -= 1
        #             boy.face_dir = 1

