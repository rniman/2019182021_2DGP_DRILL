from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image

def update():
    play_state.update()

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()  # 이전 상태로 복귀
                case pico2d.SDLK_i:
                    # boy 추가
                    play_state.team.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    # boy 삭제
                    # boy 검사
                    if len(play_state.team) == 1:
                        game_framework.pop_state()
                    else:
                        del play_state.team[len(play_state.team) - 1]
                        game_framework.pop_state()




