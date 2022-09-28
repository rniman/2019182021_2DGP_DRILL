from pico2d import *

# 애니메이션 내용
# idle, running, long range attack
# special attack sequence, special attack
# death, victory

open_canvas()

sprite = load_image('sprite_sheet.png')

#스프라이트 시트 크기
img_width = 944
img_height = 3556

#애니메이션 딜레이 시간 설정
delay_time = 0.05

def idle_ani():
    idle_width = 44
    idle_height = 49
    for idle_frame in range(0, 6):
        clear_canvas()
        sprite.clip_draw(30 + idle_frame * 50, img_height - 50 - idle_height, idle_width,
                         idle_height, 400, 300, idle_width*2, idle_height*2)
        update_canvas()
        delay(delay_time)

def runnig_ani():
    run_width = 45
    run_height = 39
    run_frame = 0

    for pos_x in range(600, 200, -10):
        clear_canvas()
        if run_frame < 6: #달리기 애니메이션 첫줄
            sprite.clip_draw(30 + run_frame * 50, img_height - 129 - run_height,
                         run_width, run_height, pos_x, 300, run_width*2, run_height*2)
        else: #달리기 애니메이션 두번째 줄
            sprite.clip_draw(30 + (run_frame - 6) * 50, img_height - 169 - run_height,
                             run_width, run_height, pos_x, 300, run_width * 2, run_height * 2)
        update_canvas()
        run_frame = (run_frame+1) % 8
        delay(delay_time)

def long_range_att_ani():
    lrAtt_width = 197
    lrAtt_height = 118

    #long range attack 그림 26개 루프
    for lrAtt_frame_y in range(1, 13 + 1):
        for lrAtt_frame_x in range(0, 2):
            clear_canvas()
            sprite.clip_draw(30 + lrAtt_frame_x * 200,
                         img_height - 238 - lrAtt_height * lrAtt_frame_y - 2 * (lrAtt_frame_y-1),
                         lrAtt_width, lrAtt_height, 400, 300, lrAtt_width * 2, lrAtt_height * 2)
            update_canvas()
            delay(delay_time)

def speical_att_seq_ani():
    spAtt_seq_width = 42
    spAtt_seq_height = 38

    spAtt_seq_frame = 0
    y = 400
    for x in range(500, 399, -10):
        clear_canvas()
        sprite.clip_draw(30 + spAtt_seq_frame * 50, img_height - 2242 - spAtt_seq_height,
                         spAtt_seq_width, spAtt_seq_height, x, y, spAtt_seq_width * 2, spAtt_seq_height * 2)
        update_canvas()
        y = y - 10
        spAtt_seq_frame = (spAtt_seq_frame + 1) % 4
        delay(delay_time)

def special_att_ani():
    spAtt_width = 76
    spAtt_height = 65

    for spAtt_frame in range(0, 6):
        clear_canvas()
        if spAtt_frame < 5:
            sprite.clip_draw(30 + spAtt_frame * 80, img_height - 1826 - spAtt_height,
                    spAtt_width, spAtt_height, 400, 300, spAtt_width * 2, spAtt_height * 2)
        else:
            sprite.clip_draw(30 , img_height - 1896 - spAtt_height,
                    spAtt_width, spAtt_height, 400, 300, spAtt_width * 2, spAtt_height * 2)
        update_canvas()
        delay(delay_time)

def death_ani():
    death_width = 52
    death_seq_1_height = 45
    death_seq_2_height = 37
    y = 300
    x = 400

    #death 17개
    for death_frame_y in range(1, 4):
        for death_frame_x in range(0, 7):
            clear_canvas()
            if death_frame_y == 1:
                sprite.clip_draw(30 + death_frame_x * 60, img_height - 2060 - death_seq_1_height,
                                 death_width, death_seq_1_height, x, y, death_width * 2, death_seq_1_height * 2)
                y = y - 10
                x = x + 15
            elif death_frame_y == 2:
                sprite.clip_draw(30 + death_frame_x * 60, img_height - 2135 - death_seq_2_height,
                                 death_width, death_seq_2_height, x, y, death_width * 2, death_seq_2_height * 2)

            elif death_frame_y == 3:
                if death_frame_x == 3:
                    break
                sprite.clip_draw(30 + death_frame_x * 60, img_height - 2175 - death_seq_2_height,
                                 death_width, death_seq_2_height, x, y, death_width * 2, death_seq_2_height * 2)

            update_canvas()
            delay(delay_time)

def victory_ani():
    victory_width = 46
    victory_height = 49
    for victory_frame in range(0, 5):
        clear_canvas()
        sprite.clip_draw(30 + victory_frame * 50, img_height - 2310 - victory_height,
                         victory_width, victory_height, 400, 300, victory_width * 2, victory_height * 2)
        update_canvas()
        delay(delay_time)


while True:
    idle_ani()
    idle_ani()
    runnig_ani()
    long_range_att_ani()
    speical_att_seq_ani()
    special_att_ani()
    death_ani()
    victory_ani()
    victory_ani()

close_canvas()
