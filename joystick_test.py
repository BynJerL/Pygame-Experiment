import pygame

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
joysticks = []
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)
    print(f"Initialized joystick: {joystick.get_name()}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed on joystick {event.joy}")
        elif event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value} on joystick {event.joy}")
        elif event.type == pygame.JOYHATMOTION:
            print(f"Hat {event.hat} moved to {event.value} on joystick {event.joy}")
    # Your game logic goes here