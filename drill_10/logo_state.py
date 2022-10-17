from pico2d import *
import game_framework
import title_state

# fill here
# running = True -> game_framework에서 다룸
image = None
logo_Time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')

def exit():
    global image
    del image

def update():
    # logo time을 계산하고 1초가 넘으면 running을 false로
    global logo_Time  # ,  running
    delay(0.01)
    logo_Time += 0.01
    if logo_Time >= 1.0:
        logo_Time = 0.0
        # running = False
        game_framework.change_state(title_state)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()



