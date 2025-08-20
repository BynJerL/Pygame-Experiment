import pygame as pg

# SETUPS
WINDOW_CAPTION = "Hello Pygame"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
FPS = 60

# COLORS
BASE_BG_COLOR = (16, 16, 16)
BASE_TEXT_COLOR = (240, 240, 240)

pg.init()

root = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(WINDOW_CAPTION)

root.fill(BASE_BG_COLOR)
pg.display.flip()

clock = pg.time.Clock()

isRunning = True

while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False

    clock.tick(FPS)
pg.quit()