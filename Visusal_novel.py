import pygame
import sys

pygame.init()
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visual Novel")

shad_of_button = (20, 136, 159)
col_of_button = (55, 179, 203)

f = pygame.font.SysFont('Arial Black', 50)
f2 = pygame.font.SysFont('Arial Black', 80)
text1 = f.render('НАЧАТЬ', True, (213, 250, 249))
text2 = f.render('ВЫХОД', True, (213, 250, 249))

pos = (0, 0)

def dialog1(c):
    dialogs = [('Наконец-то настал этот день!', 'Сегодня мой день рождения! (Амелия)'),
                      ('Мне исполняется 14 лет', 'А это значит, что сегодня мне передадут', 'семейную ценность (Амелия)'),
                      'Жду не дождусь! (Амелия)',
                      ('*стук в дверь*', 'Амелия, ты уже проснулась? Могу я войти?', '(Мама)'),
                      'Да мама, заходи (Амелия)',
                      ('Поздравляю тебя с Днем Рождения, Амелия!', 'Вот твой подарок (Мама)'),
                      ('Эта шкатулка передавалась в нашей семье', 'из поколения в поколение (Мама)'),
                      ('В ней находится особый Рубин, ', 'с помощью которого открывается', 'портал в мир Айндел (Мама)'),
                      ('После того как откроешь шкатулку,', 'с помощью кода, возьми и потри Рубин,', 'остальное тебе расскажут (Мама)' ),
                      'Хорошо! (Амелия)',
               ('Хм...Посмотрим какой тут код... (Амелия)', '(Откройте инвентарь чтобы посмотреть', 'записку)'),
               'Я думаю что код это...124243! (Амелия)',
               ('Это правильный код! Ого, это тот самый рубин!', '(Амелия) (Откройте инвентарь чтобы', 'посмотреть Рубин)')]
    pygame.display.update()
    if 8 >= c >= 5:
        im4 = pygame.image.load('Mom.png')
        screen.blit(im4, (900, 50))
        if 8 >= c >= 6:
            im4 = pygame.image.load('Box.png')
            screen.blit(im4, (650, 300))
    elif c == 9:
        im2 = pygame.image.load('Room.jpg')
        screen.blit(im2, (0, 0))
        im2 = pygame.image.load('Girl.png')
        screen.blit(im2, (100, 150))

    pygame.display.update()
    im4 = pygame.image.load('Dialogueleft.png')
    screen.blit(im4, (300, 250))
    pygame.display.update()
    f4 = pygame.font.SysFont('Arial Black', 40)
    if type(dialogs[c]) == str:
        text3 = f4.render(dialogs[c], True, (3, 22, 84))
        screen.blit(text3, (400, 700))
    elif len(dialogs[c]) == 2:
        text3 = f4.render(dialogs[c][0], True, (3, 22, 84))
        screen.blit(text3, (400, 700))
        text3 = f4.render(dialogs[c][1], True, (3, 22, 84))
        screen.blit(text3, (400, 750))
    elif len(dialogs[c]) == 3:
        text3 = f4.render(dialogs[c][0], True, (3, 22, 84))
        screen.blit(text3, (400, 700))
        text3 = f4.render(dialogs[c][1], True, (3, 22, 84))
        screen.blit(text3, (400, 750))
        text3 = f4.render(dialogs[c][2], True, (3, 22, 84))
        screen.blit(text3, (400, 800))
    else:
        text3 = f4.render(dialogs[c][0], True, (3, 22, 84))
        screen.blit(text3, (400, 700))
    pygame.display.update()

    c += 1
    return c

def invent(item):
    inv = {}
    if item == 'Записка с кодом':
        inv['Записка с кодом'] = 'Записка от мамы с кодом от шкатулки'
    elif item == 'Рубин':
        inv['Рубин'] = 'Средство перемещения в мир Айндел'
    return inv

def start(w, h):
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    screen.fill((255, 255, 255))
    im = pygame.image.load('Room.jpg')
    screen.blit(im, (0, 0))
    im2 = pygame.image.load('Girl.png')
    screen.blit(im2, (100, 150))
    a = 0
    p = 1
    c = 0
    while True:
        f3 = pygame.font.SysFont('Arial', 30)
        text3 = f3.render('Выход - [ESC]', True, (78, 54, 11))
        screen.blit(text3, (1500, 300))
        text3 = f3.render('Далее - [SPACE]', True, (78, 54, 11))
        screen.blit(text3, (1500, 350))
        text3 = f3.render('Инвентарь - [E]', True, (78, 54, 11))
        screen.blit(text3, (1500, 400))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_SPACE:
                    c = dialog1(c)
                elif event.key == pygame.K_e and p == 1:
                    im2 = pygame.image.load('Fon invent.png')
                    screen.blit(im2, (0, 0))
                    im2 = pygame.image.load('Invent.png')
                    screen.blit(im2, (700, 100))
                    f3 = pygame.font.SysFont('Arial Black', 30)
                    text3 = f3.render('ИНВЕНТАРЬ', True, (165, 127, 89))
                    screen.blit(text3, (950, 150))
                    if c == 11:
                        inv = invent('Записка с кодом')
                        f3 = pygame.font.SysFont('Arial Black', 20)
                        text3 = f3.render('Записка с кодом' + ' - ' + inv.get('Записка с кодом'), True, (0, 0, 0))
                        screen.blit(text3, (800, 150))
                        im2 = pygame.image.load('Cod.png')
                        screen.blit(im2, (1400, 150))
                    if c >= 12:
                        inv = invent('Записка с кодом')
                        f3 = pygame.font.SysFont('Arial Black', 15)
                        text3 = f3.render('Записка с кодом' + ' - ' + inv.get('Записка с кодом'), True, (0, 0, 0))
                        screen.blit(text3, (800, 200))
                        im2 = pygame.image.load('Cod.png')
                        screen.blit(im2, (800, 200))
                        inv = invent('Рубин')
                        f3 = pygame.font.SysFont('Arial Black', 15)
                        text3 = f3.render('Рубин' + ' - ' + inv.get('Рубин'), True, (0, 0, 0))
                        screen.blit(text3, (800, 230))
                        im2 = pygame.image.load('Ruby.png')
                        screen.blit(im2, (950, 150))
                    p += 1
                elif event.key == pygame.K_e and p == 2:
                    im = pygame.image.load('Room.jpg')
                    screen.blit(im, (0, 0))
                    im2 = pygame.image.load('Girl.png')
                    screen.blit(im2, (100, 150))
                    p = 1

            else:
                pygame.time.delay(300)

        pygame.display.update()

    pass

while True:
    im = pygame.image.load('Sky1.jpg')
    screen.blit(im, (0, 0))

    imf2 = f2.render('Visual Novel', True, (213, 250, 249))
    screen.blit(imf2, (690, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 710 <= mouse[0] <= 710+500 and 340 <= mouse[1] <= 500+100:
                pygame.quit()
            elif 710 <= mouse[0] <= 710+500 and 540 <= mouse[1] <= 700+100:
                start(width, height)

    mouse = pygame.mouse.get_pos()

    if 710 <= mouse[0] <= 710+500 and 340 <= mouse[1] <= 500+100:
        pygame.draw.rect(screen, shad_of_button, [710, 500, 500, 100])
    else:
        pygame.draw.rect(screen, col_of_button, [710, 500, 500, 100])

    if 710 <= mouse[0] <= 710 + 500 and 540 <= mouse[1] <= 700 + 100:
        pygame.draw.rect(screen, shad_of_button, [710, 700, 500, 100])
    else:
        pygame.draw.rect(screen, col_of_button, [710, 700, 500, 100])

    screen.blit(text1, (850, 710))
    screen.blit(text2, (850, 510))
    pygame.display.update()

