def MaxTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  return resistance*f1*f2*Op_mean*alpha

def IntTensileForce(length, resistance, f1, f2, width, alpha):
  from scipy.integrate import quad
  import matplotlib.pyplot as plt
  
  Op_mean = 4*width
  intF = quad(MaxTensileForce,0,length,args=(resistance*1000,f1,f2,Op_mean,alpha))[0]
  
  print(f'Maximum tensile force = {intF:.0f} kN')
  
  plt.plot(width,intF,'.',markersize=15)
  
  return intF
