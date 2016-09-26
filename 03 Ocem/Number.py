class Number:

    w = 0
    h = 0
    listx = 0

    def __init__(this, w, h, listx):
        this.w = w;
        this.h = h;
        this.listx = listx

    def DrawA(this, GUI, screen, n, colour, centre):
        listx = this.listx
        #if centre:
         #   w = tw = this.w-(n-(n-1)%8)-(listx[1][2]/2)
        #else:
         #   w = tw = this.w

        w = tw = this.w-(((n-(n-1)%8)*(listx[1][2]*0.0625))*centre)-((listx[1][2]/2)*centre)

        h = this.h

        counter = n
        x=0
        y=0

        while counter >= 0:
        
            GUI.draw.line(screen, (colour), (w+listx[x][0],h+listx[x][1]), (w+listx[x][2],h+listx[x][3]), listx[8])
            x = (x + 1) % 8

            if counter and not (counter + 32)  % 64:
                GUI.draw.line(screen, (colour), (tw,h), (tw+(listx[1][2]*4),h-(listx[1][2]/2)), listx[8])
                GUI.draw.line(screen, (colour), (tw+(listx[1][2]*4),h), (tw+(listx[1][2]*4),h-(listx[1][2]/2)), listx[8])
                tw += (listx[1][2]*8)*y
                y = (y + 1) % 2
            
            elif counter and not counter  % 64:
                GUI.draw.line(screen, (colour), (tw+(listx[1][2]*8),h), (tw+(listx[1][2]*4),h-(listx[1][2]/2)), listx[8])
                tw += (listx[1][2]*8)*y
                y = (y + 1) % 2
            
            if x == 0:
                w += listx[1][2]
            counter -= 1  


    def DrawB(this, GUI, screen, count, maxi):
        listbx = this.listx
        w = this.w+(maxi*(listbx[1][2]*0.0625))-listbx[1][2]
        tw = this.w+(maxi*(listbx[1][2]*0.0625))-(listbx[1][2]*8)
        h = this.h

        counter = maxi
        x=0
        y=0

        while counter >= 0:
            if counter > count:
                colour = (200,200,200)
            else:
                colour = (0,0,0)

            
            GUI.draw.line(screen, (colour), (w+listbx[x][0],h+listbx[x][1]), (w+listbx[x][2],h+listbx[x][3]), listbx[8])
            x = (x - 1) % 8

            if counter and not (counter + 32)  % 64:
                GUI.draw.line(screen, (colour), (tw,h), (tw+(listbx[1][2]*4),h-(listbx[1][2]/2)), listbx[8])
                GUI.draw.line(screen, (colour), (tw+(listbx[1][2]*4),h), (tw+(listbx[1][2]*4),h-(listbx[1][2]/2)), listbx[8])
                tw -= (listbx[1][2]*8)*y
                y = (y + 1) % 2
            
            elif counter and not counter  % 64:
                GUI.draw.line(screen, (colour), (tw+(listbx[1][2]*8),h), (tw+(listbx[1][2]*4),h-(listbx[1][2]/2)), listbx[8])
                tw -= (listbx[1][2]*8)*y
                y = (y + 1) % 2
            
            if x == 0:
                w -= listbx[1][2]
            counter -= 1


    def DrawC(this, GUI, screen, n, colour):
        w = tw = this.w
        h = this.h
        listx = this.listx

        counter = n
        x=0

        while counter >= 0:
            
            GUI.draw.line(screen, (colour), (w+listx[x][0],h+listx[x][1]), (w+listx[x][2],h+listx[x][3]), listx[8])
            x = (x + 1) % 8
            if x == 0:
                w += listx[1][2]
            counter -= 1


