def MaxTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  return resistance*f1*f2*Op_mean*alpha

def IntTensileForce(length, resistance, f1, f2, width, alpha):
  from scipy.integrate import quad
  import matplotlib.pyplot as plt
  import numpy as np
  
  Op_mean = 4*width
  intF = quad(MaxTensileForce,0,length,args=(resistance*1000,f1,f2,Op_mean,alpha))[0]
  
  print(f'Maximum tensile force = {intF:.0f} kN')
  
  width_line = []
  resistance_line = []
  length_line = []
  width_number = np.linspace(0,1,100)
  resistance_number = np.linspace(0,10,100)
  length_number = np.linspace(10,20,100)
  
  for i in range(100):
    width_line.append(quad(MaxTensilForce,0,length,args=(resistance*1000,f1,f2,width_number[i]*4,alpha))[0])
  
  fig, ax = plt.subplots(1,3,figsize=(15,10))
  ax[0].plot(intF,width,'r.',markersize=15)
  ax[0].set_xlabel('Tensile Force [kN]')
  ax[0].set_ylabel('Width [m]')
  ax[0].set_ylim(0,1.1)
  ax[0].set_xlim(200,60000)
  ax[0].plot(width_line,width_number)
  
  ax[1].plot(intF,length,'b.',markersize=15)
  ax[1].set_xlabel('Tensile Force [kN]')
  ax[1].set_ylabel('Length [m]')
  ax[1].set_ylim(0,11)
  ax[1].set_xlim(200,60000)
  
  ax[2].plot(intF,resistance,'g.',markersize=15)
  ax[2].set_xlabel('Tensile Force [kN]')
  ax[2].set_ylabel('Resistance [mPa]')
  ax[2].set_ylim(9,21)
  ax[2].set_xlim(200,60000)
  
  return intF
