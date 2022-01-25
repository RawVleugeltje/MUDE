def MaxTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  return resistance*f1*f2*Op_mean*alpha

def IntTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  intF = quad(MaxTensileForce,0,length,args=(resistance*1000,f1,f2,Op_mean,alpha))
  return intF
