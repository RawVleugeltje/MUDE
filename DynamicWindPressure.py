import numpy as np
import matplotlib.pyplot as plt

def TheoreticalWind(tau_w, rho, k, z, z0):
  u_star = np.sqrt(tau_w/rho)
  u_z = u_star / k * np.log(z / z0)
  p_w = 0.5 * rho * u_z**2
  
  fig, ax = plt.subplots(1,2,figsize=(12,4))
  
  ax[0].plot(p_w,tau_w,'r.',markersize=30)
  ax[0].set_xlabel('Dynamic wind pressure [Pa]')
  ax[0].set_ylabel('Surface shear stress [Pa]')
#   ax[0].set_ylim(0,0.8)
#   ax[0].set_xlim(-10,800)
  ax[0].grid()
  
  ax[1].plot(p_w,z,'b.',markersize=30)
  ax[1].set_xlabel('Dynamic wind pressure [Pa]')
  ax[1].set_ylabel('Elevation [m]')
#   ax[1].set_ylim(0,11)
#   ax[1].set_xlim(-10,850)
  ax[1].grid()
    
  plt.tight_layout()
  
  return p_w
