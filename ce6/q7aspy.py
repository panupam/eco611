import scipy.optimize as spo 
import numpy as np
f=lambda x: 3*x[0]-5*x[1]+x[2]
lin=spo.LinearConstraint([[1,0,-2],[2,-1,1]],[4,2],[np.inf]*2)
bond=spo.Bounds([0,0,0],[np.inf]*3)
res=spo.minimize(f,[1,1,1],constraints=lin,bounds=bond,options={'gtol': 1e-6,'disp':True})