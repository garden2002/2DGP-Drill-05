from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('character.png')


def handle_events():
    global running, Xdir , Ydir , direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
           running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                Xdir += 1
                direction = 2
            elif event.key == SDLK_LEFT:
                Xdir -= 1
                direction = 3
            elif event.key == SDLK_UP:
                Ydir += 1
                direction = 1
            elif event.key == SDLK_DOWN:
                Ydir -= 1
                direction = 4
        elif event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                Xdir -= 1
            elif event.key == SDLK_LEFT:
                Xdir += 1
            if event.key == SDLK_UP:
                Ydir -= 1
            elif event.key == SDLK_DOWN:
                Ydir += 1


running = True
x = 800 // 2
y = 600 // 2
frame = 0
direction = 0
Xdir = 0
Ydir = 0
while running:
    clear_canvas()
    ground.draw(400, 300)
    character.clip_draw(frame * 46, 50 * direction , 46, 50, x, y , 69, 75)
    update_canvas()
    handle_events()
    if not running:
        break
    if Xdir == 0 and Ydir == 0:
        direction = 0
    frame = (frame + 1) % 4
    x += Xdir * 5
    if x > 800:
        x = 800
    if x < 0:
        x = 0
    y += Ydir * 5
    if y > 600:
        y = 600
    if y < 0:
        y = 0
    delay(0.05)

close_canvas()