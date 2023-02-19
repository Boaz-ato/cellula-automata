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
    
    elif cell_state == -1:
         r  =random.random()
         if r <= p3:
             state[i_update,j_update] = 1
         else:
            pass
    
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
             

p1 =0.5
p2= 0.5
p3= 0.5




#f1m = np.linspace(start=0 , stop=lx*ly, num = lx*ly) # sample just 50 points
f1m = np.linspace(start=0 , stop=50 , num = 50)  # can reduce num to 10?
#print(len(f1m))
infected_repeat = np.zeros((5,(len(f1m))), dtype =float)
#print(infected_repeat)
errors =[]
infected_repeat_mean =[]

for row in range(5):
    
    average_infected_allprobs = []
    for fm in range(len(f1m)):
        
        
        for i in range(lx):
            for j in range(ly):
                r=random.random()
                if(r<0.3): state[i,j]=1
                if(r>=0.3 and r < 0.6 ): state[i,j]= 0
                if(r >=  0.6): state[i,j] = -1 
        
        for i in range(fm):
                                    
            i_immu = np.random.randint(0,lx)
            j_immu = np.random.randint(0,ly)
            state[i_immu,j_immu] = 2
            
        
        
        
        
        sum_infected_sweep = 0
        counter = 0 
            
            
    
    
        for n in range(nsteps): #reduce nsteps to maybe 1000
           
            if n < 100:
                for t_step in range (lx*ly):
                    state = sirs_rules(state,p1,p2, p3) 
                    
                   
            if n >= 100:
                for t_step in range (lx*ly):
                    state = sirs_rules(state,p1,p2,p3) 
                    sum_infected_sweep += (np.count_nonzero(state == 0))
                    counter += 1
                    
                    if np.count_nonzero(state == 0) == 0:
                        break
                
               
               
        
                else:
                    continue
                break
                
                    
        average_infected_allprobs.append(((sum_infected_sweep/counter)/ (lx*ly)))
    
    for a in range(len(average_infected_allprobs)):
       
        infected_repeat[row,a] = average_infected_allprobs[a]

for e in range(len(f1m)):
    infected_repeat_mean.append(np.mean(infected_repeat[:,e])) # selecting a column and finding the mean
    errors.append(np.std(infected_repeat[:,e])/np.sqrt(5))


    
        
        
        
                    
#print(average_infected_allprobs)              
#print(f1m/(lx*ly))

  
     
plt.errorbar(f1m/(lx*ly),infected_repeat_mean, xerr = None, yerr = errors)  
plt.xlabel("Fraction of agents permanently immune to the infection")
plt.ylabel("Avrage infected fraction")
plt.show()



f=open('immune_fraction.dat','w')   
  
f.write("Fraction_immune" + "  " + "Infected_fraction" + "\n")
for imm ,infect  in zip(f1m/(lx*ly) ,infected_repeat_mean):
    f.write( str(imm) + " "  + str(infected_repeat_mean) +  "\n")
f.close()





