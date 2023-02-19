import random
import numpy as np
import matplotlib.pyplot as plt

x= [
0.0,
0.0,
0.0,
0.0,
0.006363404540953502,
0.014964790423749435,
0.0769098100365806,
0.753670460253085,
0.8485277915025016,
0.7251153692345547,
0.6359738899360039,
0.5876056747524316,
0.5574341360270836,
0.5163741557276467,
0.4947914857764317,
0.48668480575209117,
0.4844793952640458,
0.45319197237967046,
0.44267312334667963,
0.4193690891226254,
0.4366362442055731
]

x_err =[]

for i in x:
    r= random.random()
    print(i/15)
    x_err.append((i/(15)))

    

p1s = np.linspace(start =0.2, stop =0.5 , num = 21)
plt.errorbar(p1s,x, xerr = None, yerr = x_err )  
plt.xlabel("Probability from S to R")
plt.ylabel("Variance of number of infected sites")
plt.show()
    
    
    
    
    
    
    
    
    
    

