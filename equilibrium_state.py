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
                


                    
equi_state = input("What equilibrium state do you want to observe? " + "\n" + " Enter(a) for an absorbing state , (w) for a wave state and (d) for a dynamic state: ")


    

equi_state = equi_state.capitalize()
    

while True:
    
 
        
    
    
    if   equi_state == "A" or equi_state == "W" or equi_state == "D":
        break
    else:
        equi_state = input("What equilibrium state do you want to observe? " + "\n" + " Enter(a) for an absorbing state , (w) for a wave state and (d) for a dynamic state: ")
        equi_state = equi_state.capitalize()
      
        
                    
            
# s = 1 , I = 0 , R =-1




if equi_state == "A":
    lx= 50
    ly=lx 
    nsteps = 10000
    p1 = 0.5
    p2 = 0.6
    p3 = 0.1
    
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
        for t_step in range (lx*ly):
            state = sirs_rules(state) 
       
        
        #show animation
        
        plt.cla()
        im=plt.imshow(state, animated=True, vmin = -1, vmax = 1)
        plt.draw()
        plt.pause(0.0001)
     

if equi_state == "D":
    lx= 50
    ly=lx 
    nsteps = 10000
    p1 = 0.7
    p2 = 0.7
    p3 = 0.7
    
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
        for t_step in range (lx*ly):
            state = sirs_rules(state) 
       
        
        #show animation
        
        plt.cla()
        im=plt.imshow(state, animated=True, vmin = -1, vmax = 1)
        plt.draw()
        plt.pause(0.0001)


if equi_state == "W":
    lx= 100
    ly=lx 
    nsteps = 10000
    p1 = 0.8
    p2 = 0.1
    p3 = 0.01
    
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
        for t_step in range (lx*ly):
            state = sirs_rules(state) 
       
        
        #show animation
        
        plt.cla()
        im=plt.imshow(state, animated=True, vmin = -1, vmax = 1)
        plt.draw()
        plt.pause(0.0001)


