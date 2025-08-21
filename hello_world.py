import pygame as pg

class Player:
    def __init__(self, width: int = 20, height:int = 20):
        self.width = width
        self.height = height
        self.posX = 75 - width // 2
        self.posY = 75 - height // 2
        self.lastX = self.posX
        self.lastY = self.posY

        self.isMoving = False
        self.direction = None
    
    def getSprite(self):
        leftLimit = WINDOW_WIDTH // 2 - 75
        rightLimit = WINDOW_WIDTH // 2 + 75 - self.width
        topLimit = 115
        bottomLimit = topLimit + 150 - self.height
        absX = min(rightLimit, max(leftLimit, self.posX + leftLimit))
        absY = min(bottomLimit, max(topLimit, self.posY + topLimit))
        return pg.Rect(int(absX), int(absY), self.width, self.height)

    def draw(self):
        leftLimit = WINDOW_WIDTH // 2 - 75
        rightLimit = WINDOW_WIDTH // 2 + 75
        topLimit = 115
        bottomLimit = 265
        absX = min(rightLimit, max(leftLimit, self.posX + leftLimit))
        absY = min(bottomLimit, max(topLimit, self.posY + topLimit))
        sprite = pg.Rect(int(absX), int(absY), self.width, self.height)
        pg.draw.rect(root, (240, 0, 0), sprite)
    
    def moveLeft(self):
        self.posX = max(0, self.posX - 1)
        self.isMoving = True
    
    def moveRight(self):
        self.posX = min(150 - self.width, self.posX + 1)
        self.isMoving = True
    
    def moveTop(self):
        self.posY = max(0, self.posY - 1)
        self.isMoving = True
    
    def moveBottom(self):
        self.posY = min(150 - self.height, self.posY + 1)
        self.isMoving = True
    
    def getLastCoor(self):
        self.lastX = self.posX
        self.lastY = self.posY

    def getDirection(self):
        dx = self.posX - self.lastX
        dy = self.posY - self.lastY

        if dx == 0 and dy == 0:
            self.direction = None
        elif dx == 1 and dy == 0:
            self.direction = "E"
        elif dx == 1 and dy == 1:
            self.direction = "SE"
        elif dx == 0 and dy == 1:
            self.direction = "S"
        elif dx == -1 and dy == 1:
            self.direction = "SW"
        elif dx == -1 and dy == 0:
            self.direction = "W"
        elif dx == -1 and dy == -1:
            self.direction = "NW"
        elif dx == 0 and dy == -1:
            self.direction = "N"
        elif dx == 1 and dy == -1:
            self.direction = "NE"

    def idling(self):
        self.isMoving = False
        self.direction = None

class Follower:
    def __init__(self, width: int = 15, height: int = 15, speed: float = 1.0):
        self.width = width
        self.height = height
        self.speed = speed
        self.posX = 10
        self.posY = 10
    
    def _arenaLimits(self):
        return (WINDOW_WIDTH // 2 - 75, 115) # (x, y)
    
    def getSprite(self):
        leftLimit, topLimit = self._arenaLimits()
        rightLimit, bottomLimit = (leftLimit + 150 - self.width, topLimit + 150 - self.height)
        absX = min(rightLimit, max(leftLimit, leftLimit + self.posX))
        absY = min(bottomLimit, max(topLimit, topLimit + self.posY))
        return pg.Rect(int(absX), int(absY), self.width, self.height)
    
    def update(self, player: "Player"):
        if self.getSprite().colliderect(player.getSprite()):
            return
        
        tX = player.posX + player.width // 2
        tY = player.posY + player.height // 2
        rX = self.posX + self.width // 2
        rY = self.posY + self.height // 2

        dx = tX - rX
        dy = tY - rY
        drSq = dx ** 2 + dy ** 2
        if drSq == 0:
            return
        
        dr = drSq ** 0.5
        stepX = (dx / dr) * self.speed
        stepY = (dy / dr) * self.speed

        self.posX += stepX
        self.posY += stepY

        self.posX = min(150 - self.width, max(0, self.posX))
        self.posY = min(150 - self.height, max(0, self.posX))
    
    def draw(self):
        pg.draw.rect(root, (240, 240, 0), self.getSprite())

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
player = Player()
follower = Follower()
arena = pg.Rect(WINDOW_WIDTH // 2 - 75, 115, 150, 150)
pg.draw.rect(root, (240, 0, 0), pg.Rect(30, 30, 30, 30))
pg.draw.rect(root, BASE_TEXT_COLOR, arena, 3)
player.draw()
# fonts = pg.font.get_fonts()
# for f in fonts:
#     print(f)

heading1 = pg.font.SysFont("consolas", 30, bold=True, italic=True)
normalText = pg.font.SysFont("arial", 20, bold=False, italic=False)
subText = pg.font.SysFont("consolas", 12, bold=True)
text1 = heading1.render("Hello, Pygame!", True, BASE_TEXT_COLOR)
text2 = normalText.render("Hello, World! This is only a template.", True, BASE_TEXT_COLOR)
root.blit(text1, (75, 30))
root.blit(text2, (30, 65))

# FLIP
pg.display.flip()

# LOOP
isRunning = True
while isRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
    
    player.getLastCoor()

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        player.moveTop()
    if keys[pg.K_DOWN]:
        player.moveBottom()
    if keys[pg.K_LEFT]:
        player.moveLeft()
    if keys[pg.K_RIGHT]:
        player.moveRight()
    
    player.getDirection()
    follower.update(player)

    if player.direction == None:
        player.isMoving = False

    root.blit(subText.render(f"is_moving: {player.isMoving}  ", True, BASE_TEXT_COLOR, BASE_BG_COLOR),  (5, WINDOW_HEIGHT - 54))
    root.blit(subText.render(f"dir: {player.direction}   ", True, BASE_TEXT_COLOR, BASE_BG_COLOR),  (5, WINDOW_HEIGHT - 40))
    root.blit(subText.render(f"coor: (x={player.posX},y={player.posY})      ", True, BASE_TEXT_COLOR, BASE_BG_COLOR), (5, WINDOW_HEIGHT - 28))
    
    root.fill(BASE_BG_COLOR, arena)
    pg.draw.rect(root, BASE_TEXT_COLOR, arena, 3)
    follower.draw()
    player.draw()

    clock.tick(FPS)
    currentfps = round(clock.get_fps(), 2)

    root.blit(subText.render(f"fps: {currentfps} ", True, BASE_TEXT_COLOR, BASE_BG_COLOR), (5, WINDOW_HEIGHT - 15))

    pg.display.flip()
pg.quit()