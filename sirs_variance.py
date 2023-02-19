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
nsteps = 10000


state =np.zeros((lx,ly),dtype=float)
#state = np.full((lx, ly), -1 , dtype=float)
             








p2= 0.5
p1s = np.linspace(start =0.2, stop =0.5 , num = 21)
p3 = 0.5
var_errors =[]




var_infected_allprobs = []

for p1 in p1s:
    
    sum_infected_sweep = []
    sum_infected_sweep_sqr = []
    
    
    for i in range(lx):
        for j in range(ly):
            r=random.random()
            if(r<0.3): state[i,j]=1
            if(r>=0.3 and r < 0.6 ): state[i,j]= 0
            if(r >=  0.6): state[i,j] = -1 
    


    for n in range(nsteps):
       
        if n < 100:
            for t_step in range (lx*ly):
                state = sirs_rules(state,p1,p2,p3) 
               
        if n >= 100:
            for t_step in range (lx*ly):
                state = sirs_rules(state,p1,p2,p3) 
                sum_infected_sweep.append((np.count_nonzero(state == 0)))
                
                sum_infected_sweep_sqr.append((np.count_nonzero(state == 0)**2))
                
                
                if np.count_nonzero(state == 0) == 0:
                    break
            
           
           
    
            else:
                continue
            break
            
            
    
    var_infected_allprobs.append(((np.mean(sum_infected_sweep_sqr))/ (lx*ly)) - (((np.mean(sum_infected_sweep))**2)/ (lx*ly)))

                    
    
 
    # using bootstrap method to get error in variance.
    bootstrap_var =[]
    num_measure = len(sum_infected_sweep)
    
    #print(sum_infected_sweep)
    for k in range (100):
        
        infected = 0 
        infected_sqr = 0
        #selecting 100 random energy values to compute the specific heat capacity
        if len(sum_infected_sweep) < 100 :
            
            for n in range(len(sum_infected_sweep)):
                r = np.random.random()
                chosen = int(r* num_measure) 
                infected += sum_infected_sweep[chosen]
                infected_sqr += sum_infected_sweep_sqr[chosen]
        
        else:
             for n in range(100):
                r = np.random.random()
                chosen = int(r* num_measure) 
                infected += sum_infected_sweep[chosen]
                infected_sqr += sum_infected_sweep_sqr[chosen]
        
        print(infected)
        infected = infected/100
        infected_sqr = infected_sqr/100
        #computed variance using the samples values
        bootstrap_var.append((infected_sqr/(lx*ly)) - ((infected**2)/(lx*ly)) )
    var_error = (np.mean((np.square(bootstrap_var))) - (np.mean(bootstrap_var))**2   )**(1/2)
    var_errors.append(var_error) 
    


plt.errorbar(p1s,var_infected_allprobs, xerr = None, yerr = var_errors )  
plt.xlabel("Probability from S to R")
plt.ylabel("Variance of number of infected sites")
plt.show()



f=open('infected_sites_variance_cut.dat','w')   
for site in (var_infected_allprobs):
    f.write( str(site) +  "\n")
f.close()

     







