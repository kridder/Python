import Butinp

class Test:

    w=0
    h=0
    s=0

    def __init__(this, w, h, s):
        this.w = w - (4*24) - 3  #w = middle of#inp - (tiental/2 * 4*fontsize - 3)
        this.h = h + 5
        this.s = s

    def Test(this, GUI, screen, butinp):
        x=0
        for i in butinp:
            GUI.draw.rect(screen, (0,0,255), (butinp[x].buttona), 1)
            if butinp[x].buttonb:
                GUI.draw.rect(screen, (0,0,255), (butinp[x].buttonb), 1)
            x+=1

            

        #run = 8
        #r=0
        #x=0
        #while run:

            #w = this.w + r
            #h = this.h
            
            # for 0, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (501,355,8,40), 1)
            #GUI.draw.rect(screen, (0,0,255), (w,h,8,40), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x].buttona), 1)

            # for 1, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (509,395,16,8), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+1].buttona), 1)
            
            # for 2, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (509,379,8,8), 1)
            #GUI.draw.rect(screen, (0,0,255), (517,387,8,8), 1)

            #GUI.draw.rect(screen, (0,0,255), (butinp[x+2].buttona), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+2].buttonb), 1)

            # for 3, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (517,355,8,8), 1)
            #GUI.draw.rect(screen, (0,0,255), (509,363,8,8), 1)

            #GUI.draw.rect(screen, (0,0,255), (butinp[x+3].buttona), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+3].buttonb), 1)

            # for 4, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (509,347,16,8), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+4].buttona), 1)

            # for 5, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (509,355,8,8), 1)
            #GUI.draw.rect(screen, (0,0,255), (517,363,8,8), 1)

            #GUI.draw.rect(screen, (0,0,255), (butinp[x+5].buttona), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+5].buttonb), 1)

            # for 6, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (509,371,16,8), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+6].buttona), 1)

            # for 7, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (517,379,8,8), 1)
            #GUI.draw.rect(screen, (0,0,255), (509,387,8,8), 1)
            
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+7].buttona), 1)
            #GUI.draw.rect(screen, (0,0,255), (butinp[x+7].buttonb), 1)

            # for 10, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (525,355,8,40), 1)

            # for 11, (600,350, 4) 600 - 4*24 = 504(-3)   350 + 48(+3)
            #GUI.draw.rect(screen, (0,0,255), (533,395,16,8), 1)

            #run -= 1
            #r += 24
            #x += 8

            #if not run:
                #w += 24
                #GUI.draw.rect(screen, (0,0,255), (butinp[x].buttona), 1)
