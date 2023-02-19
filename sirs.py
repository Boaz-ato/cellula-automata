import matplotlib
matplotlib.use('TKAgg')
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def sirs_rules(state):
    
    
    i_update = np.random.randint(0,lx)
    j_update = np.random.randint(0,ly)
    cell_state = state[i_update,j_update]
    
    
    if cell_state == 1:
        
        n_n =[]
        
        i_up = i_update-1
        if i_up == -1:
            i_up = lx - 1 
           
            
        i_down = i_update + 1
        if i_down == ly:
            i_down = 0
          
            
        j_left = j_update -1
        if j_left == -1:
            j_left = lx -1
            
            
        j_right = j_update + 1
        if j_right == lx:
            j_right = 0
        
        n_n.append(state[i_up,j_update])
        n_n.append(state[i_down,j_update])
        n_n.append(state[i_update,j_left])
        n_n.append(state[i_update,j_right])
            
            
            
        infected = n_n.count(0)
        if infected >= 1:
            r  =random.random()
            if r <= p1:
                state[i_update,j_update] = 0
            else:
                pass
    
    elif cell_state == 0:
         r  =random.random()
         if r <= p2:
             state[i_update,j_update] = -1
         else:
            pass
    
    else:
         r  =random.random()
         if r <= p3:
             state[i_update,j_update] = 1
         else:
            pass
    

    return state
                


                    
size = input(" Enter the size of the system:  ")
p1 = input ("Enter p1: ")
p2 = input("Enter p2: ")
p3 = input("Enter p3: ")


    


    

while True:
    
    try:
        size = int(size)
        p1= float(p1)
        p2 = float(p2)
        p3=float(p3) 

    except ValueError:
        size = input(" Enter the size of the system:  ")
        p1 = input ("Enter p1: ")
        p2 = input("Enter p2: ")
        p3 = input("Enter p3: ")
        continue
        
    
    
    if type(size) == int and p1 <= 1 and p1 >= 0 and p2 <= 1 and p2 >= 0 and p3 <= 1 and p3 >= 0  :
        break
    else:
        size = input(" Enter the size of the system:  ")
        p1 = input ("Enter p1: ")
        p2 = input("Enter p2: ")
        p3 = input("Enter p3: ")
        
                    
            
# s = 1 , I = 0 , R =-1

lx= size
ly=lx 
nsteps = 10000


state =np.zeros((lx,ly),dtype=float)
#state = np.full((lx, ly), -1 , dtype=float)
             

for i in range(lx):
    for j in range(ly):
        r=random.random()
        if(r<0.3): state[i,j]=1
        if(r>=0.3 and r < 0.6 ): state[i,j]= 0
        if(r >=  0.6): state[i,j] = -1 



fig = plt.figure()
im=plt.imshow(state, animated=True)





for n in range(nsteps):
    for t_step in range (lx*ly): # lx*ly iterations is one sweep!
        state = sirs_rules(state) 
   
    
    #show animation
    
    plt.cla()
    im=plt.imshow(state, animated=True, vmin = -1, vmax = 1)
    plt.draw()
    plt.pause(0.0001)
     




