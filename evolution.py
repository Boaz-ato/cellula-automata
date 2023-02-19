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
    # returns the new state of the latttice after applying the rules of game of life
    
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
            
            if state[i,j] == 1:
                live_cells = neighbours.count(1)
                if live_cells < 2 or live_cells > 3:
                    new_state[i,j] = -1
                if live_cells == 2 or live_cells ==3:
                    new_state[i,j] = 1
            
            if state[i,j] == -1:
                live_cells = neighbours.count(1)
                if live_cells == 3 :
                    new_state[i,j] = 1
                
                else:
                    new_state[i,j] = -1
    
    return new_state
                
               
                    

                    
            
# 1 is alive and  -1 is dead
equilibrium =[]
for simu in range(101):
#random initial condition
    for i in range(lx):
        for j in range(ly):
            r=random.random()
            if(r<0.5): state[i,j]=-1
            if(r>=0.5): state[i,j]=1
    
    old_state = state
    
    active_sites =[]
    counter = 0 
    
    active_counting = []
    
    sum_active =[]
    
    while True:
        
        
        new_state = dead_or_alive(old_state) # returns the new state of the lattice after applying the rules of the game of life
        active_count = np.count_nonzero(new_state == 1) # counts the number of live cells
        active_sites.append(active_count) # the array "active_sites" contains the number of live cells at each time step
        
        # I want to compare the last 10 elements in the active sites array
        # if they are all the same , the system have reach eqilibrium, as the number of live cells is not changing
        # However, there are cases, where the equilibrium is reached but the number number of live cells keeps changing in a pattern
        # In this case, I have an array that stores the sum of the live cells in the last 10 time steps. 
        #if the last 5 values of this array are the same, then we have reach an eqilibrium
        
        if counter > 10:
            #old_active_counting = active_counting
            
            active_counting = active_sites[-10:] # storing the number of live cells in the last 10 time steps
            sum_active.append(np.sum(active_counting)) # storing the sum of the number of live cells in the last 10 time steps.
            if len(sum_active) > 10:
                sum_active1 = sum_active[-10:] # keeping the lenght of the array to just 10 elements
                #print(sum_active1)
                reach0 = sum_active1.count(sum_active1[0]) == len(sum_active1) # checking if elements of the array are all the same
              
                #print((sum_active1))
                if sum_active1.count(sum_active1[0]) == len(sum_active1) :
                    equilibrium.append(counter - 10)
                    
                    
                    break
                
            
            
            
                
            #print(active_counting)
            reach = active_counting.count(active_counting[0]) == len(active_counting) # checking if the number of live cells in the last 10 time steps are all the same
            if reach : 
                #print("reach")
                equilibrium.append(counter-10)
                break 
                
        old_state = new_state
        counter = counter + 1
        
        
        
        
        
        """
        if counter > 10 :
            if  np.sum(active_counting) == np.sum(old_active_counting) :
                equilibrium.append(counter-1)
                break
        """


e_mean = np.mean(equilibrium)
e_std = np.std(equilibrium)        
n, bins, patches = plt.hist(equilibrium, 50, density=True, facecolor='g', alpha=0.75)
plt.xlabel("Time needed to equilibrate")
plt.ylabel("Probability")
plt.grid(True)
plt.text(2, 0.8 , r'$\mu =$' +str(e_mean) +  " ," + "  " +  r'$\sigma =$' + str(e_std) , horizontalalignment='center',verticalalignment='center')


f=open('equlibrium_time.dat','w')   
for eqi in equilibrium:
    f.write( str(eqi) + "\n")
f.close()
plt.show()




