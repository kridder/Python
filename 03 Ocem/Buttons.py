import Number

class Buttons:

    width = 2
    coloura = (0,0,0)
    colourb = [(200,200,200),(100,100,100)]

    x = 0
    button = 0
    Num = 0

    def __init__(this, GUI, w, h, x, listx):
        this.x = x + 1
        a = w + ((x*(28+15)) - (172 * (x/4)))
        b = h + ((44+15)*(x/4))
        this.button = GUI.Rect(a,b,28,44)
        this.Num = Number.Number(a+6,b+6,listx)


    def Draw(this, GUI, screen, mo,):
        GUI.draw.rect(screen, (this.coloura), this.button, this.width)
        this.Num.DrawC(GUI, screen, this.x, this.colourb[mo])
            
