from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x= 400
y= 90
direct = 'right'
state = 'circle'
angle = 0
while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if state == 'rect':
        if direct == 'right':
            x = x+2
            if(x == 800):
                direct = 'up'
            if(x==400):
                state = 'circle'
        elif direct == 'up':
            y = y+2
            if(y == 600):
                direct = 'left'
        elif direct == 'left':
            x = x-2
            if( x == 0):
                direct = 'down'
        elif direct == 'down':
            y = y-2
            if(y == 90):
                direct = 'right'
    elif state == 'circle':
            #400,190 중점
            x = 400 - math.sin(angle/ 180 * 2 * math.pi)*200
            y = 290 - math.cos(angle/ 180 * 2 * math.pi)*200
            angle = angle + 2
            if(angle == 180):
                state = 'rect'
                x= 400
                y= 90
                angle = 0
    delay(0.01)

close_canvas()
