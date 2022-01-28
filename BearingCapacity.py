def MaxTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  return resistance*f1*f2*Op_mean*alpha

def IntTensileForce(length, resistance, f1, f2, width, alpha, plot=False):
  from scipy.integrate import quad
  import matplotlib.pyplot as plt
  import numpy as np
  
  Op_mean = 4*width
  intF = quad(MaxTensileForce,0,length,args=(resistance*1000,f1,f2,Op_mean,alpha))[0]
    
  width_line = []
  resistance_line = []
  length_line = []
  width_number = np.linspace(0,1.1,100)
  resistance_number = np.linspace(9,21,100)
  length_number = np.linspace(0,11,100)
  
  if plot == True:
    for i in range(100):
      width_line.append(quad(MaxTensileForce,0,length,args=(resistance*1000,f1,f2,width_number[i]*4,alpha))[0])
      resistance_line.append(quad(MaxTensileForce,0,length,args=(resistance_number[i]*1000,f1,f2,width*4,alpha))[0])
      length_line.append(quad(MaxTensileForce,0,length_number[i],args=(resistance*1000,f1,f2,width*4,alpha))[0])
  
    fig, ax = plt.subplots(1,3,figsize=(12,4))
    ax[0].plot(width_line,width_number,'r')
    ax[0].plot(intF,width,'r.',markersize=30)
    ax[0].set_xlabel('Tensile Force [kN]')
    ax[0].set_ylabel('Width [m]')
    ax[0].set_ylim(0,1.1)
    ax[0].set_xlim(200,60000)
    ax[0].grid()
  
    ax[1].plot(length_line,length_number,'b')
    ax[1].plot(intF,length,'b.',markersize=30)
    ax[1].set_xlabel('Tensile Force [kN]')
    ax[1].set_ylabel('Length [m]')
    ax[1].set_ylim(0,11)
    ax[1].set_xlim(200,60000)
    ax[1].grid()
  
    ax[2].plot(resistance_line,resistance_number,'g')
    ax[2].plot(intF,resistance,'g.',markersize=30)
    ax[2].set_xlabel('Tensile Force [kN]')
    ax[2].set_ylabel('Resistance [mPa]')
    ax[2].set_ylim(9,21)
    ax[2].set_xlim(200,60000)
    ax[2].grid()
    
    plt.tight_layout()
    
  return intF

def ClumpCriterion(width, length, r_grid, v_soil, v_water, v_concrete):
    import numpy as np
    import matplotlib.pyplot as plt
    Deq = np.sqrt(np.pi/4) * width
    if r_grid < 6 * Deq:
        print('Overlap')
    else:
        d = 6 * Deq
        b = 1/2 * (d - Deq)
        V1 = np.pi/4 *d**2 * (length - b)
        V2 = 1/3 * np.pi/4 * d**2 * (b + 1/2*Deq)
        V3 = 1/3 * np.pi/4 * Deq**2 * 1/2*Deq
        V4 = np.pi/4 * Deq**2 * length
        Vclump = V1 + V2 + V3 + V4
    
        Vpile = V4

        v_weight_soil = v_soil - v_water
        v_weight_pile = v_concrete - v_water

    F_tension_max = Vclump * v_weight_soil + Vpile * v_weight_pile
    
    return F_tension_max

def ClumpCriterionFig(width, length, r_grid, v_soil, v_water, v_concrete):
  import numpy as np
  import matplotlib.pyplot as plt
  
  width_line = []
  length_line = []
  width_number = np.linspace(0,0.75,100)
  length_number = np.linspace(0,11,100)
      
  for i in range(100):
    width_line.append(ClumpCriterion(width_number[i],length,r_grid,v_soil,v_water,v_concrete))
    length_line.append(ClumpCriterion(width,length_number[i],r_grid,v_soil,v_water,v_concrete))
  
  fig, ax = plt.subplots(1,2,figsize=(12,4))
  ax[0].plot(width_line,width_number,'r')
  ax[0].plot(ClumpCriterion(width,length,r_grid,v_soil,v_water,v_concrete),width,'r.',markersize=30)
  ax[0].set_xlabel('Tensile Force [kN]')
  ax[0].set_ylabel('Width [m]')
#       ax[0].set_ylim(0,1.1)
#       ax[0].set_xlim(200,60000)
  ax[0].grid()
  
  ax[1].plot(length_line,length_number,'b')
  ax[1].plot(ClumpCriterion(width,length,r_grid,v_soil,v_water,v_concrete),length,'b.',markersize=30)
  ax[1].set_xlabel('Tensile Force [kN]')
  ax[1].set_ylabel('Length [m]')
#       ax[1].set_ylim(0,11)
#       ax[1].set_xlim(200,60000)
  ax[1].grid()
      
  plt.tight_layout()
    
  return 
  
