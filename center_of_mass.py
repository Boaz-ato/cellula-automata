import matplotlib
matplotlib.use('TKAgg')
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.optimize import curve_fit



lx= 50
ly=lx 


#state =np.zeros((lx,ly),dtype=float)
state = np.full((lx, ly), -1 , dtype=float)

def dead_or_alive(state):
    
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

    
old_state = state





nstep = 1000
position = []
for n in range(nstep):
    new_state = dead_or_alive(old_state) 
    
    live_indices = np.transpose(np.nonzero(new_state == 1)) # returns the index of the live cells
    #print(live_indices)
    
    x_pos = []
    y_pos = []
    r_com = 0 
    
    

    for i in range(len(live_indices)):
        x_pos.append(live_indices[i][0])
        y_pos.append(live_indices[i][1])
        
    """    
    if((lx-1 in x_pos) and (0 in x_pos)) == False or ((ly-1 in y_pos) and (0 in y_pos)) == False or ((lx-1 in x_pos) and (1 in x_pos)) ((ly-1 in y_pos) and (1 in y_pos)) == False:
        for i,j in zip(x_pos,y_pos):
            r_com = r_com + np.sqrt(i**2 + j**2)
    """  
 
    for i,j in zip(x_pos,y_pos):
         r_com = r_com + np.sqrt(i**2 + j**2)
    
    if((lx-1 in x_pos) and (0 in x_pos)) == True or ((ly-1 in y_pos) and (0 in y_pos)) == True or ((lx-1 in x_pos) and (1 in x_pos)) == True or ((ly-1 in y_pos) and (1 in y_pos)) == True:
        break
 

    position.append(r_com/len(x_pos))
    #print(position)
    
   
    
    
    old_state = new_state

times  = np.linspace(0,len(position), num = len(position))


def linerase1(x, a , b):
    return a*x + b



popt, pcov = curve_fit(linerase1,times, position)

print(np.sqrt(np.diag(pcov)))

print("Speed of glider is: " + str(popt[0]))
plt.scatter(times, position)
plt.plot(times, popt[0]*times + popt[1], color ="r")
plt.xlabel("Time")
plt.ylabel("Center of mass")
plt.show()     

f=open('com_vs_time.dat','w')   
f.write("Time" + " " + "Position" + "\n")
for com ,frame  in zip( position, times):
    f.write( str(frame) + " "  + str(com) +  "\n")
f.close()




