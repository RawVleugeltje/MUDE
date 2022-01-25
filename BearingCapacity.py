def MaxTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  return resistance*f1*f2*Op_mean*alpha

def IntTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  from scipy.integrate import quad
  import matplotlib.pyplot as plt
  
  intF = quad(MaxTensileForce,0,length,args=(resistance*1000,f1,f2,Op_mean,alpha))
  
  plt.plot(width,intF)
  
  return intF
