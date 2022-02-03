def TheoreticalWind(tau_w, rho, k, z, z0):
  u_star = np.sqrt(tau_w/rho)
  u_z = u_star / k * np.log(z / z0)
  p_w = 0.5 * rho * u_z**2
  
  return p_w
