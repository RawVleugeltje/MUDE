import numpy as np
import matplotlib.pyplot as plt

def TheoreticalWind(tau_w, rho, k, z, z0):
  u_star = np.sqrt(tau_w/rho)
  u_z = u_star / k * np.log(z / z0)
  p_w = 0.5 * rho * u_z**2
  
  return p_w

def TheoreticalWindPlot(tau_w, rho, k, z, z0):
  tau_line = []
  z_line = []
  tau_number = np.linspace(0,1,100)
  z_number = np.linspace(10,500,100)
  
  for i in range(100):
    tau_line.append(TheoreticalWind(tau_number[i],rho,k,z,z0))
    z_line.append(TheoreticalWind(tau_w,rho,k,z_number[i],z0))
  
  fig, ax = plt.subplots(1,2,figsize=(12,4))
    
  ax[0].plot(tau_line, tau_number, 'r')
  ax[0].plot(TheoreticalWind(tau_w,rho,k,z,z0),tau_w,'r.',markersize=30)
  ax[0].set_xlabel('Dynamic wind pressure [Pa]')
  ax[0].set_ylabel('Surface shear stress [Pa]')
  ax[0].set_ylim(0,1.1)
  ax[0].set_xlim(0,102)
  ax[0].grid()
  
  ax[1].plot(z_line, z_number, 'b')
  ax[1].plot(TheoreticalWind(tau_w,rho,k,z,z0),z,'b.',markersize=30)
  ax[1].set_xlabel('Dynamic wind pressure [Pa]')
  ax[1].set_ylabel('Elevation [m]')
  ax[1].set_ylim(0,510)
  ax[1].set_xlim(0,102)
  ax[1].grid()
    
  plt.tight_layout()
  
  return

def DynamicWind(height, C_D, rho, beta_t, alpha, u_1h_10m):
  u = beta_t * (height / 10)**alpha * u_1h_10m
  q = 0.5 * rho * u**2 * C_D
  return q
  
def DynamicWindPlot(height, C_D, rho, beta_t, alpha, u_1h_10m):
  height_line = []
  u_1h_10m_line = []
  height_number = np.linspace(0,1000,100)
  u_1h_10m_number = np.linspace(26,32,2)
  
  for i in range(100):
    height_line.append(DynamicWind(height_number[i], C_D, rho, beta_t, alpha, u_1h_10m))
    u_1h_10m_line.append(DynamicWind(height, C_D, rho, beta_t, alpha, u_1h_10m_number[i]))
  
  fig, ax = plt.subplots(1,2,figsize=(12,4))
    
  ax[0].plot(height_line, height_number, 'r')
  ax[0].plot(DynamicWind(height, C_D, rho, beta_t, alpha, u_1h_10m),height,'r.',markersize=30)
  ax[0].set_xlabel('Dynamic wind pressure [Pa]')
  ax[0].set_ylabel('Height [m]')
#   ax[0].set_ylim(0,1.1)
#   ax[0].set_xlim(0,102)
  ax[0].grid()
  
  ax[1].plot(u_1h_10m_line, u_1h_10m_number, 'b')
  ax[1].plot(DynamicWind(height, C_D, rho, beta_t, alpha, u_1h_10m),u_1h_10m,'b.',markersize=30)
  ax[1].set_xlabel('Dynamic wind pressure [Pa]')
  ax[1].set_ylabel('Average wind velocity at 10m height during 1 hour [m/s]')
#   ax[1].set_ylim(0,510)
#   ax[1].set_xlim(0,102)
  ax[1].grid()
    
  plt.tight_layout()
  
  return
