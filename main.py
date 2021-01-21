
##----------------------------------------------------------------------------Void™ OS---------------------------------------------------------------------------##
#                                                          (not to be confused with void linux)                                                                   #
#                                                          made by Cirilaron and BaguetteYeeter                                                                   #
##---------------------------------------------------------------------------------------------------------------------------------------------------------------##
import pygame
import random
import sys
import getopt

#Σ = Cirilaron (or vodka if you are from manwhosays)
#E = Egg AKA BaguetteYeeter

cells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Σ: neither of us knows what those numbers do lmao #E: Same lmao

#Σ: did you just remove the numbers
#E: yep
#Σ: y tho
#E: they were all wrong
#Σ: ok then

pack = "default"

try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:", ["pack="])
except getopt.GetoptError:
    print("you did something wrong. be ashamed of yourself.")
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-p", "--pack"):
        pack = arg
    if opt in ("-h"):
        print("You don't need help in the void™")

class textures:
    class font:
        A = pygame.image.load("textures/" + pack + "/font/A.png")
        B = pygame.image.load("textures/" + pack + "/font/B.png")
        C = pygame.image.load("textures/" + pack + "/font/C.png")
        D = pygame.image.load("textures/" + pack + "/font/D.png")
        E = pygame.image.load("textures/" + pack + "/font/E.png")
        F = pygame.image.load("textures/" + pack + "/font/F.png")
        G = pygame.image.load("textures/" + pack + "/font/G.png")
        H = pygame.image.load("textures/" + pack + "/font/H.png")
        I = pygame.image.load("textures/" + pack + "/font/I.png")
        J = pygame.image.load("textures/" + pack + "/font/J.png")
        K = pygame.image.load("textures/" + pack + "/font/K.png")
        L = pygame.image.load("textures/" + pack + "/font/L.png")
        M = pygame.image.load("textures/" + pack + "/font/M.png")
        N = pygame.image.load("textures/" + pack + "/font/N.png")
        O = pygame.image.load("textures/" + pack + "/font/O.png")
        P = pygame.image.load("textures/" + pack + "/font/P.png")
        Q = pygame.image.load("textures/" + pack + "/font/Q.png")
        R = pygame.image.load("textures/" + pack + "/font/R.png")
        S = pygame.image.load("textures/" + pack + "/font/S.png")
        T = pygame.image.load("textures/" + pack + "/font/T.png")
        U = pygame.image.load("textures/" + pack + "/font/U.png")
        V = pygame.image.load("textures/" + pack + "/font/V.png")
        W = pygame.image.load("textures/" + pack + "/font/W.png")
        X = pygame.image.load("textures/" + pack + "/font/X.png")
        Y = pygame.image.load("textures/" + pack + "/font/Y.png")
        Z = pygame.image.load("textures/" + pack + "/font/Z.png")
        cursor = pygame.image.load("textures/" + pack + "/font/cursor.png")
        fonts = [0, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]

pygame.init()
mainScreen = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Void™ OS")

i = 0
cursorCell = 1
keyPressed = 0
hotel = "Trivago"
command = ""

exec(open("bin/toNumber.py").read())
exec(open("bin/echo.py").read())

run = True
while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if keyPressed == 0:
            cells[cursorCell] = 1
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_b]:
        if keyPressed == 0:
            cells[cursorCell] = 2
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_c]:
        if keyPressed == 0:
            cells[cursorCell] = 3
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_d]:
        if keyPressed == 0:
            cells[cursorCell] = 4
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_e]:
        if keyPressed == 0:
            cells[cursorCell] = 5
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_f]:
        if keyPressed == 0:
            cells[cursorCell] = 6
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_g]:
        if keyPressed == 0:
            cells[cursorCell] = 7
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_h]:
        if keyPressed == 0:
            cells[cursorCell] = 8
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_i]:
        if keyPressed == 0:
            cells[cursorCell] = 9
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_j]:
        if keyPressed == 0:
            cells[cursorCell] = 10
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_k]:
        if keyPressed == 0:
            cells[cursorCell] = 11
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_l]:
        if keyPressed == 0:
            cells[cursorCell] = 12
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_m]:
        if keyPressed == 0:
            cells[cursorCell] = 13
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_n]:
        if keyPressed == 0:
            cells[cursorCell] = 14
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_o]:
        if keyPressed == 0:
            cells[cursorCell] = 15
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_p]:
        if keyPressed == 0:
            cells[cursorCell] = 16
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_q]:
        if keyPressed == 0:
            cells[cursorCell] = 17
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_r]:
        if keyPressed == 0:
            cells[cursorCell] = 18
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_s]:
        if keyPressed == 0:
            cells[cursorCell] = 19
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_t]:
        if keyPressed == 0:
            cells[cursorCell] = 20
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_u]:
        if keyPressed == 0:
            cells[cursorCell] = 21
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_v]:
        if keyPressed == 0:
            cells[cursorCell] = 22
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_w]:
        if keyPressed == 0:
            cells[cursorCell] = 23
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_x]:
        if keyPressed == 0:
            cells[cursorCell] = 24
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_y]:
        if keyPressed == 0:
            cells[cursorCell] = 25
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_z]:
        if keyPressed == 0:
            cells[cursorCell] = 26
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_BACKSPACE]:
        if keyPressed == 0:
            if cursorCell != 1:
                cursorCell -= 1
            cells[cursorCell] = 0
            keyPressed = 2
        else:
            keyPressed -= 1
    elif keys[pygame.K_SPACE]:
        if keyPressed == 0:
            cells[cursorCell] = 0
            cursorCell += 1
            keyPressed = 2
        else:
            keyPressed -= 1
    else:
        keyPressed = 1



    mainScreen.fill((0, 0, 0))
    for y in range(0, 25):
        for x in range(0, 40):
            i += 1
            if cells[i] != 0:
                mainScreen.blit(textures.font.fonts[cells[i]], (x*16, y*16))
            if cursorCell == i:
                mainScreen.blit(textures.font.cursor, (x*16, y*16))
    i = 0
    #Σ: i have no fucking idea what this does but i think it draws a rectangle somewhere
    #E: not just somewhere, EVERYWHERE
    #Σ: im dumb
    #E: I need to make a font pack now
    #Σ: what
    pygame.display.update()
pygame.quit()
