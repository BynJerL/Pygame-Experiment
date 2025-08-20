import pygame as pg

# SETUPS
WINDOW_CAPTION = "Hello Pygame"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
FPS = 60
ICON_ADDRESS = "assets/icon/icon.png"

# COLORS
BASE_BG_COLOR = (16, 16, 16)
BASE_TEXT_COLOR = (240, 240, 240)

# INITIALIZATION
pg.init()

root = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(WINDOW_CAPTION)
pg_icon = pg.image.load(ICON_ADDRESS)
pg.display.set_icon(pg_icon)

root.fill(BASE_BG_COLOR)

clock = pg.time.Clock()

# OBJECT DRAW
pg.draw.rect(root, (240, 0, 0), pg.Rect(30, 30, 30, 30))

# fonts = pg.font.get_fonts()
# for f in fonts:
#     print(f)

font = pg.font.SysFont("consolas", 30)
text = font.render("Hello, Pygame!", True, BASE_TEXT_COLOR)
root.blit(text, (75, 30))

# FLIP
pg.display.flip()

# LOOP
isRunning = True
while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False

    clock.tick(FPS)
pg.quit()