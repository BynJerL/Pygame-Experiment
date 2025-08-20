import pygame as pg

# SETUPS
WINDOW_CAPTION = "Hello Pygame"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

pg.init()

root = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(WINDOW_CAPTION)

isRunning = True

while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False

pg.quit()