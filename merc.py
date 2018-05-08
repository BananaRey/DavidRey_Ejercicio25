import numpy as np
import matplotlib.pyplot as plt
V=172.404 #km/h
r=57.91*(10.0**6.0) #km
beta_teo=(V**2.0)/(r**2.0)
 
alpha=np.linspace(-2,2,100) 
beta_0=np.exp( ((((V**2.0)/r**(1.0-alpha))-beta_teo)**2.0)/4.0)*alpha
beta=np.exp( ((((V**2.0)/r**(1.0-alpha))-beta_teo)**2.0)/4.0)*alpha

print(beta)
normalizacion=np.sum(beta)*4.0/100.0
beta=beta/normalizacion
#plt.ylim(0.0,1.0)
plt.plot(beta_0,beta)
plt.title('Beta',fontsize=25)
plt.xlabel('Beta_0',fontsize=25)
plt.ylabel('prob.Beta',fontsize=25)
plt.show()
plt.savefig('Beta.png')
plt.close()

