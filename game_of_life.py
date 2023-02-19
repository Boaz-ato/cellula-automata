import matplotlib
matplotlib.use('TKAgg')
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



lx= 50
ly=lx 


#state =np.zeros((lx,ly),dtype=float)
state = np.full((lx, ly), -1 , dtype=float)

def dead_or_alive(state):
    
    
    # we are running through the whole lattice checking if each cell is alive or dead
    new_state = np.zeros((lx,ly), dtype =float)
    for i in range(lx):
        for j in range(ly):
            neighbours = []
            
            i_up = i-1
            if i_up == -1:
                i_up = lx - 1 
               
                
            i_down = i + 1
            if i_down == ly:
                i_down = 0
              
                
            j_left = j -1
            if j_left == -1:
                j_left = lx -1
                
                
            j_right = j + 1
            if j_right == lx:
                j_right = 0
            
            
            neighbours.append(state[i_up,j])
            neighbours.append(state[i_down,j])
            neighbours.append(state[i,j_left])
            neighbours.append(state[i,j_right])
            neighbours.append(state[i_up,j_left])
            neighbours.append(state[i_up,j_right])
            neighbours.append(state[i_down,j_left])
            neighbours.append(state[i_down, j_right])
            
            if state[i,j] == 1:  # if the cell is alive
                live_cells = neighbours.count(1)  # returns the number of live neighbours
                if live_cells < 2 or live_cells > 3:
                    new_state[i,j] = -1 # live cell is now dead
                if live_cells == 2 or live_cells ==3:
                    new_state[i,j] = 1 #live cell is still alive
            
            if state[i,j] == -1: #if cell is dead
                live_cells = neighbours.count(1) # count the number of live cells
                if live_cells == 3 :
                    new_state[i,j] = 1 #dead cell is now alive
                
                else:
                    new_state[i,j] = -1 #dead cell remains dead
    
    return new_state
                
               
                    
initial_cond = input("Please enter the initial condition to start the Game of life." + "\n" + "Enter 'r' for a random initial condition , enter 'o' for oscillating initial condition and 'g' for a glider: ")
initial_cond = initial_cond.capitalize()
while True:
    if initial_cond == "R" or initial_cond ==  "O" or initial_cond == "G":
        break
    else:
        initial_cond = input(" Please enter the initial condition to start the Game of life." + "\n" + "Enter 'r' for a random initial condition , enter 'o' for oscillating initial condition and 'g' for a glider: ")
        initial_cond = initial_cond.capitalize()
                    
            
# 1 is alive and  -1 is dead

if initial_cond == "R":
    #random initial condition
    for i in range(lx):
        for j in range(ly):
            r=random.random()
            if(r<0.5): state[i,j]=-1
            if(r>=0.5): state[i,j]=1


if initial_cond == "O":
    #oscillating initial condition
    i_osc=np.random.randint(0,lx)
    j_osc=np.random.randint(0,ly)
    state[i_osc,j_osc] = 1
    
    i_osc_up = i_osc-1
    if i_osc_up == -1:
        i_osc_up = lx - 1 
               
                
    i_osc_down = i_osc + 1
    if i_osc_down == ly:
        i__osc_down = 0
    
    state[i_osc_up,j_osc] = 1
    state[i_osc_down, j_osc] = 1


if  initial_cond == "G":
    i_glid=np.random.randint(0,lx)
    j_glid=np.random.randint(0,ly)
    state[i_glid,j_glid] = 1
    
    i_glid_down = i_glid + 1
    if i_glid_down == ly:
        i_glid_down = 0
              
    j_glid_right = j_glid + 1
    if j_glid_right == lx:
        j_glid_right = 0
    
    state[i_glid_down, j_glid_right] =1
    
    i_glid_down1 = i_glid_down + 1
    if i_glid_down1 == ly:
        i_glid_down1 = 0
    
    state[i_glid_down1, j_glid_right] =1
    
    
    j_glid_left = j_glid_right -1
    if j_glid_left == -1:
        j_glid_left = lx -1
    
    state[i_glid_down1 , j_glid_left] = 1
    
    
    j_glid_left1 = j_glid_left - 1
    if j_glid_left1 == -1:
        j_glid_left1 == lx -1
    
    
    state[i_glid_down1, j_glid_left1] = 1
    
    
    
    
    
    
    
                
    
    
    
    
    
    
    
    
    


fig = plt.figure()
im=plt.imshow(state, animated=True)

old_state = state



while True:
    new_state = dead_or_alive(old_state) 
    old_state = new_state
    #show animation
    plt.cla()
    im=plt.imshow(new_state, animated=True, vmin = -1, vmax = 1)
    plt.draw()
    plt.pause(0.0001)
     


