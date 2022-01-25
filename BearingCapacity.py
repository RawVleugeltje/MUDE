def MaxTensileForce(length, resistance, f1, f2, Op_mean, alpha):
  return resistance*f1*f2*Op_mean*alpha

def TensileForceInt(length, resistance, f1, f2, Op_mean, alpha):
  intF = quad(MaxTensileForce(length, reistance, f1, f2, Op_mean, alpha))
