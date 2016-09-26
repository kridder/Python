import pygame as GUI

def key(run):
    
    while run:
        GUI.event.pump()
        keys = GUI.key.get_pressed()

        if keys[GUI.K_z]:
            while keys[GUI.K_z]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'z'
            #time.sleep(0.15)
            break

        if keys[GUI.K_a]:
            while keys[GUI.K_a]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'a'
            break

        if keys[GUI.K_b]:
            while keys[GUI.K_b]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'b'
            break
                
        if keys[GUI.K_c]:
            while keys[GUI.K_c]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'c'
            break

        if keys[GUI.K_d]:
            while keys[GUI.K_d]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'd'
            break

        if keys[GUI.K_e]:
            while keys[GUI.K_e]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'e'
            break
        
        if keys[GUI.K_f]:
            while keys[GUI.K_f]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'f'
            break

        if keys[GUI.K_g]:
            while keys[GUI.K_g]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'g'
            break

        if keys[GUI.K_r]:
            while keys[GUI.K_r]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'r'
            break

        if keys[GUI.K_s]:
            while keys[GUI.K_s]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 's'
            break

        if keys[GUI.K_y]:
            while keys[GUI.K_y]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'y'
            break

        if keys[GUI.K_SPACE]:
            while keys[GUI.K_SPACE]:
                GUI.event.pump()
                keys = GUI.key.get_pressed()              

            return 'SPACE'
            break
                
        if keys[GUI.K_ESCAPE]:
            #time.sleep(0.15)
            return 'ESCAPE'
            break
