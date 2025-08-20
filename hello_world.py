import pygame as pg

pg.init()

root = pg.display.set_mode((400, 300))
pg.display.set_caption("Hello Pygame")

isRunning = True

while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False

pg.quit()