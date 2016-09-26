class Butinp:

    ID = 0
    buttona = 0
    buttonb = 0

    def __init__(this, GUI, w, h, s, maxi, ID):
        w = w - (((maxi/16)-(ID/8))*(s*4)) - (s/2)  #w = middle of#inp - (tiental/2 * 4*fontsize - 3)
        h = h + 5
        #s = s
        this.ID = ID

        if ID % 8 < 1:
            this.buttona = GUI.Rect(w,h,int(s*1.334),int(s*6.667))
            this.buttonb = GUI.Rect(0,0,0,0)
        elif ID % 8 < 2:
            this.buttona = GUI.Rect(w+int(s*0.667),h+int(s*6.667),(s*4),int(s*1.334))
            this.buttonb = GUI.Rect(0,0,0,0)
        elif ID % 8 < 3:
            this.buttona = GUI.Rect(w+int(s*1.334),h+(s*4),int(s*1.334),int(s*1.334))
            this.buttonb = GUI.Rect(w+int(s*2.667),h+int(s*5.334),int(s*1.334),int(s*1.334))
        elif ID % 8 < 4:
            this.buttona = GUI.Rect(w+int(s*2.667),h,int(s*1.334),int(s*1.334))
            this.buttonb = GUI.Rect(w+int(s*1.334),h+int(s*1.334),int(s*1.334),int(s*1.334))
        elif ID % 8 < 5:
            this.buttona = GUI.Rect(w+int(s*0.667),h-int(s*1.334),(s*4),int(s*1.334))
            this.buttonb = GUI.Rect(0,0,0,0)
        elif ID % 8 < 6:
            this.buttona = GUI.Rect(w+int(s*1.334),h,int(s*1.334),int(s*1.334))
            this.buttonb = GUI.Rect(w+int(s*2.667),h+int(s*1.334),int(s*1.334),int(s*1.334))
        elif ID % 8 < 7:
            this.buttona = GUI.Rect(w+int(s*1.334),h+int(s*2.667),int(s*2.667),int(s*1.334))
            this.buttonb = GUI.Rect(0,0,0,0)
        elif ID % 8 < 8:
            this.buttona = GUI.Rect(w+int(s*2.667),h+(s*4),int(s*1.334),int(s*1.334))
            this.buttonb = GUI.Rect(w+int(s*1.334),h+int(s*5.334),int(s*1.334),int(s*1.334))
