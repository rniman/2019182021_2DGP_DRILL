from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def Handle_Events():
    global Program_Run
    global running
    global dir_x
    global dir_y
    global old_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Program_Run = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                Program_Run = False
            elif event.key == SDLK_LEFT:
                running = True
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                running = True
                dir_x += 1
            elif event.key == SDLK_UP:
                running = True
                dir_y += 1
            elif event.key == SDLK_DOWN:
                running = True
                dir_y -= 1

            if dir_x == 0 and dir_y == 0:
                running = False
            if dir_x < 0:
                old_dir = -1
            elif dir_x > 0:
                old_dir = 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            if dir_x == 0 and dir_y == 0:
                running = False
            if dir_x < 0:
                old_dir = -1
            elif dir_x > 0:
                old_dir = 1

def Character_Draw():
    if running and old_dir == 1:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif running and old_dir == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif running == False and old_dir == 1:
        character.clip_draw(frame * 100, 300, 100, 100, x, y)
    elif running == False and old_dir == -1:
        character.clip_draw(frame * 100, 200, 100, 100, x, y)

def frame_update():
    global frame
    frame = (frame + 1) % 8

def Move_Character():
    global x, y
    x += dir_x * 5
    y += dir_y * 5
    if x >= TUK_WIDTH - 30:
        x = TUK_WIDTH - 30
    elif x <= 0 + 30:
        x = 30

    if y + 50 >= TUK_HEIGHT:
        y = TUK_HEIGHT - 50
    elif y - 50 <= 0:
        y = 50

Program_Run = True
running = False
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x, dir_y = 0, 0
old_dir = 1

while Program_Run:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    Character_Draw()
    Handle_Events()
    frame_update()
    Move_Character()
    update_canvas()
    delay(0.01)

close_canvas()
