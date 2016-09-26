import pygame as GUI
import Number
import Buttons
import Listx
import Butinp
import Test
import random

run = True
reset = False
gamemode = 0
count = 0
n1 = 0
n2 = 0
maxi = 0
inp = ''
disans = 0
level = 0
maxlevel = 3
numcorrect = 0
levelup = False
win = False
submit = 0

# Set base difficulty of problems
baserandpl = 020
baserandmn = 010
baserandmt = 04
baseranddv = 010

# Listx class
# (4,0) default (4,1) for listbx
listx = Listx.Listx()

NumA = Number.Number(450,150,listx.Listx(4,0))
NumB = Number.Number(750,150,listx.Listx(4,0))
NumInp = Number.Number(600,350,listx.Listx(6,1))
NumAns = Number.Number(928,500,listx.Listx(5,0))
NumLvl = Number.Number(100,12,listx.Listx(3,0))
NumCor = Number.Number(1164,20,listx.Listx(3,0))

#NumTest = Number.Number(0,0,listx)

Test = Test.Test(NumInp.w,NumInp.h,NumInp.listx[1][2]/4)

mode = 0
funct = ['+','-','*','/']

GUI.init()
Sfont = GUI.font.Font(None, 14)
font = GUI.font.Font(None, 24)
Bfont = GUI.font.Font(None, 34)
GTitle = Sfont.render('0.00.24', True, (0, 0, 0))

resolution = (1200,800)
screen = GUI.display.set_mode( resolution )

# Init buttons
button = [1,2,3,4,5,6,7,8]
x=0
for i in button:
    button[x] = Buttons.Buttons(GUI, 522,600,x, listx.Listx(4,0))
    x+=1

colourb = [(200,200,200),(100,100,100)]

Ebutton = GUI.Rect(694,600,28+15+28,44)
Cbutton = GUI.Rect(694,659,28+15+28,44)


while run:

    GUI.event.pump()
    keys = GUI.key.get_pressed()

    # Test mouse
    for event in GUI.event.get():
        if event.type == GUI.QUIT:
            run = False
        if event.type == GUI.MOUSEBUTTONDOWN:
            mouse = event.button
        else:
            mouse = 0

    m = GUI.mouse.get_pos()

    screen.fill((255,255,255))

    # Keep random list up to date
    randnumpl = [01,baserandpl*2**level]
    randnummn = [01,baserandmn*2**level]
    randnummt = [01,baserandmt*2**level]
    randnumdv = [01,baseranddv*2**level]
    randnum = [randnumpl,randnummn,randnummt,randnumdv]

    # Maxi based on level
    oldmaxi = maxi
    
    if level < 2:
        maxi = 0100
    else:
        maxi = 0400

    if not maxi == oldmaxi:
        # Init Butinp
        butinp = []
        
        cycle = maxi + 1
        ID = 0
        while cycle:
            butinp.append(Butinp.Butinp(GUI,NumInp.w,NumInp.h,NumInp.listx[1][2]/4,maxi,ID))
            cycle -= 1
            ID += 1
        

    # Count can't exceed maxi
    count = min(max(0,count),maxi)

    # GUI
    function = Bfont.render(funct[mode], True, (0,0,0))
    screen.blit(function, (600, 150))
    screen.blit(GTitle, (1155, 782))

    # Win
    if level == maxlevel:
        win = True
        level = maxlevel - 1

    if win:
        Win = Bfont.render('YOU WIN', True, (0,155,0))
        screen.blit(Win, (600, 300))

    # Display Difficulty level
    dlevel = Bfont.render('Level:', True, (0,0,0))
    screen.blit(dlevel, (20, 20))
    NumLvl.DrawC(GUI, screen, level+1, (0,0,0))

    # Display gamemode
    Gmode = font.render(str(gamemode), True, (200,200,200))
    screen.blit(Gmode, (20, 60))

    # Display numcorrect
    #Numcorr = font.render(str(numcorrect), True, (200,200,200))
    #screen.blit(Numcorr, (1160, 70))

    NumCor.w = (1180-NumCor.listx[1][2]) - (NumCor.listx[1][2] * (max(0,numcorrect-1)/8))
    NumCor.DrawA(GUI, screen, numcorrect, (200,200,200), 0)

    # Draw & Check Buttons
    
    #GUI.draw.line(screen, (0,0,0), (600,0),(600,800), 1)
    #GUI.draw.line(screen, (0,0,0), (450,0),(450,800), 1)
    #GUI.draw.line(screen, (0,0,0), (750,0),(750,800), 1)

    # Number Input Button
    x=0
    bimo=0 # Input button mouse over
    for i in butinp:
        if butinp[x].buttona.collidepoint(m) or butinp[x].buttonb.collidepoint(m):
            dcount = butinp[x].ID
            if mouse == 1 and not disans:
                count = dcount
            bimo = 1
        x+=1

    # Number Buttons
    x=0
    for i in button:
        if button[x].button.collidepoint(m):
            mo = 1
            if mouse == 1 and not disans:
                #count += button[x].x
                count += button[x].x - (count%8)
                mouse = 0
        else:
            mo = 0
        button[x].Draw(GUI, screen, mo)
        x+=1

    # Enter Button
    GUI.draw.rect(screen, (0,0,0), Ebutton, 2)
    if Ebutton.collidepoint(m):
        mo = 1
        if mouse == 1:
            submit = 1
            mouse = 0
    else:
        mo = 0
    Enter = Bfont.render('Enter', True, colourb[mo])
    screen.blit(Enter, (699,612))

    # Clear Button
    GUI.draw.rect(screen, (0,0,0), Cbutton, 2)
    if Cbutton.collidepoint(m):
        mo = 1
        if mouse == 1 and not disans:
            count = 0
            mouse = 0
    else:
        mo = 0
    Clear = Bfont.render('Clear', True, colourb[mo])
    screen.blit(Clear, (699,671))
        

    # Number 1

    NumA.DrawA(GUI, screen, n1, (0,0,0), 1)

    
    # Number 2

    NumB.DrawA(GUI, screen, n2, (0,0,0), 1)


    # Input Number
    if bimo:
        countx = dcount
    else:
        countx = count
    
    NumInp.DrawB(GUI, screen, countx, maxi)
    

    # Display Input

    if not inp == '':
        CCount = font.render(inp, True, (0,0,255))
        screen.blit(CCount, (600, 700))
    

    # Calculate answer (in decimal for further calculations)
    if mode == 0:
        ans = n1 + n2
    elif mode == 1:
        ans = n1 - n2
    elif mode == 2:
        ans = n1 * n2
    elif mode == 3:
        ans = n1 / n2
        

    # Display answer
    if disans == 1:
        if count == ans:
            colour = (0,155,0)            
        else:
            colour = (155,0,0)

        NumAns.w = 1200-(17 * NumAns.listx[1][2])
        NumAns.DrawA(GUI, screen, ans, colour, 1)

    #Test (Displays mouse over input buttons)
    #Test.Test(GUI, screen, butinp)

    # Draw Display
    GUI.display.flip()

    # Input numbers
    if keys[GUI.K_KP0] and not disans:
        while keys[GUI.K_KP0]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '0'

    if keys[GUI.K_KP1] and not disans:
        while keys[GUI.K_KP1]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '1'

    if keys[GUI.K_KP2] and not disans:
        while keys[GUI.K_KP2]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '2'

    if keys[GUI.K_KP3] and not disans:
        while keys[GUI.K_KP3]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '3'

    if keys[GUI.K_KP4] and not disans:
        while keys[GUI.K_KP4]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '4'

    if keys[GUI.K_KP5] and not disans:
        while keys[GUI.K_KP5]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '5'

    if keys[GUI.K_KP6] and not disans:
        while keys[GUI.K_KP6]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '6'

    if keys[GUI.K_KP7] and not disans:
        while keys[GUI.K_KP7]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        inp += '7'

    #Enter numbers
    if keys[GUI.K_RETURN]  and not disans or keys[GUI.K_KP_ENTER] and not disans:
        while keys[GUI.K_RETURN] or keys[GUI.K_KP_ENTER]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        if not inp == '':
            count = int(inp, 8)
            inp = ''

    # Space submits answer
    if (keys[GUI.K_SPACE] or submit) and gamemode and not win:
        while keys[GUI.K_SPACE]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

            
        disans = (disans + 1) % 2
        if disans:
            if count == ans:
                if gamemode:
                    numcorrect += 1
                if not (numcorrect+1)%(12*(level+1)+1):
                    level += 1
            else:
                if gamemode:
                    numcorrect = max(0, numcorrect - numcorrect%12 - 12)
                    level = max(0,level-1)
        else:
            reset = True
        submit = 0

    # add 1
    if keys[GUI.K_KP_PLUS] and not disans:
        while keys[GUI.K_KP_PLUS]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

            
        count += 1


    # subtract 1
    if keys[GUI.K_KP_MINUS] and not disans:
        while keys[GUI.K_KP_MINUS]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

            
        count -= 1


    # add 10
    if keys[GUI.K_KP_MULTIPLY] and not disans:
        while keys[GUI.K_KP_MULTIPLY]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

            
        count += 010

    # subtract 10
    if keys[GUI.K_KP_DIVIDE] and not disans:
        while keys[GUI.K_KP_DIVIDE]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

            
        count -= 010

    # Clear
    if keys[GUI.K_BACKSPACE] and not disans:
        while keys[GUI.K_BACKSPACE]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

            
        count = 0

    # Debug
    if keys[GUI.K_c]:
        while keys[GUI.K_c]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        numcorrect += 1
        if not (numcorrect+1)%(12*(level+1)+1):
            level += 1

    # Toggle gamemode
    if keys[GUI.K_p]:
        while keys[GUI.K_p]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        gamemode = (gamemode + 1) % 2
        reset = True


    # Toggle Function
    if keys[GUI.K_m] and not gamemode:
        while keys[GUI.K_m]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()
    
        mode = (mode + 1) % 3
        reset = True

        if mode == 1 and n2 > n1:
            mem = n1
            n1 = n2
            n2 = mem


    # Toggle Answer
    if keys[GUI.K_s] or keys[GUI.K_a] and not gamemode:
        while keys[GUI.K_s] or keys[GUI.K_a]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        disans = (disans + 1) % 2


    # Toggle Difficulty
    if keys[GUI.K_d] and not gamemode or levelup:
        while keys[GUI.K_d]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        level = (level + 1) % maxlevel
        levelup = False

    if keys[GUI.K_f] and not gamemode:
        while keys[GUI.K_f]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        level = (level - 1) % maxlevel


    # Reset
    if keys[GUI.K_r]  and not gamemode or reset and not win:
        while keys[GUI.K_r]:
            GUI.event.pump()
            keys = GUI.key.get_pressed()

        # Give random function while playing.
        if gamemode:
            mode = random.randint(0,2)

        n1 = random.randint(randnum[mode][0],randnum[mode][1])
        n2 = random.randint(randnum[mode][0],randnum[mode][1])
        count = 0
        inp =  ''
        disans = 0
        reset = False
        win = False

        if mode == 1 and n2 > n1:
            mem = n1
            n1 = n2
            n2 = mem
    

    if keys[GUI.K_ESCAPE]:
        break

GUI.quit()
