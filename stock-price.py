import numpy as np
from scipy.stats import *
def call(S,K,T,r,sigma):
  return S * norm.cdf((np.log(S/K) + (r+(sigma**2)/2)*T)/(sigma * np.sqrt(T)) - K * np.exp(-r*T)*N((np.log(S/K) + (r+(sigma**2)/2)*T)/(sigma * np.sqrt(T)-sigma*np.sqrt(T))
