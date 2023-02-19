import matplotlib
matplotlib.use('TKAgg')
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def sirs_rules(state, p1,p2, p3):
    
    
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



    


    

while True:
    
    try:
        size = int(size)
      

    except ValueError:
        size = input(" Enter the size of the system:  ")
        continue
        
    
    
    if type(size) == int:
        break
    else:
        size = input(" Enter the size of the system:  ")
    
        
                    
            
# s = 1 , I = 0 , R =-1

lx= size
ly=lx 
nsteps = 1000


state =np.zeros((lx,ly),dtype=float)
#state = np.full((lx, ly), -1 , dtype=float)
             


p2= 0.5
p1s = np.linspace(start =0, stop =1 , num = 21)
p3s = np. linspace(start = 0, stop= 1 , num =21)



average_infected_allprobs = np.zeros((len(p1s),len(p3s)),dtype=float)
var_infected_allprobs = np.zeros((len(p1s),len(p3s)),dtype=float)

for p1 in p1s:
    for p3 in p3s:   
        sum_infected_sweep = 0
        sum_infected_sweep_sqr = 0
        counter = 0 
        
        for i in range(lx):
            for j in range(ly):
                r=random.random()
                if(r<0.3): state[i,j]=1
                if(r>=0.3 and r < 0.6 ): state[i,j]= 0
                if(r >=  0.6): state[i,j] = -1 
        


        for n in range(nsteps):
           
            if n < 100:
                for t_step in range (lx*ly):
                    state = sirs_rules(state,p1,p2, p3) 
                   
            if n >= 100:
                for t_step in range (lx*ly):
                    state = sirs_rules(state,p1,p2,p3) 
                    sum_infected_sweep += (np.count_nonzero(state == 0)) # count the number of infected sites and add them
                    
                    sum_infected_sweep_sqr  += (np.count_nonzero(state == 0))**2 # count the number of infected sites, square them and add them
                    counter += 1
                    
                    if np.count_nonzero(state == 0) == 0:
                        break
                
               
               
        
                else:
                    continue
                break
                
                
        average_infected_allprobs[int(np.where(p1s == p1)[0][0]),int(np.where(p3s == p3)[0][0])] = ((sum_infected_sweep/counter)/ (lx*ly))
        var_infected_allprobs[int(np.where(p1s == p1)[0][0]),int(np.where(p3s == p3)[0][0])] = ((sum_infected_sweep_sqr/counter)/ (lx*ly)) - ((sum_infected_sweep/counter)**2/ (lx*ly))
       
                    
                

#plt.contourf(average_infected_allprobs )   
plt.contourf(var_infected_allprobs)     
plt.colorbar()
plt.show()
  
     

f=open('infected_sites.dat','w')   
for site in (average_infected_allprobs):
    f.write( str(site) +  "\n")
f.close()


f=open('infected_sites_variance.dat','w')   
for site in (var_infected_allprobs):
    f.write( str(site) +  "\n")
f.close()

