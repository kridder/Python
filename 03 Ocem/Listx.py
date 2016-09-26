class Listx:

    def Listx(this, z, b):

        x=4*z
        y=8*z

        # Width
        w = max(int(0.75*z),1)

        # Create list of draw co-ordinates
        lista=(0,0,0,y) #0
        listaa=(x,0,x,y) #0 for counting backwards
        listb=(0,y,x,y) #1
        listc=(x,y,0,x) #2
        listd=(0,x,x,0) #3
        liste=(x,0,0,0) #4
        listf=(0,0,x,x) #5
        listg=(x,x,0,x) #6
        listh=(0,y,x,x) #7
        listx=(lista,listb,listc,listd,liste,listf,listg,listh,w)
        listbx=(listaa,listb,listc,listd,liste,listf,listg,listh,w)

        if b:
            return listbx
        else:
            return listx
