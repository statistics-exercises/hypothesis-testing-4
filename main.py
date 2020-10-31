import numpy as np
import scipy.stats

def sampleMean( data ) :
  #Your code to calcualte the sampe mean should go here
  
def criticalRange( mu, sigma, N ) : 
  # Your code to calculate the critical range should go here
  lower = # This variable should be the lower of the two
  upper = # This variable should be the higher of the two
  return lower, upper
  
def hypothesisTest( data, mu, sigma ) : 
  l, u = criticalRange( mu, sigma, len(data) )
  # You need to use the l and u values that are returned from the critical range
  # function above within an if statement.  This if statement should decide when
  # each of the following statements should be returned.
  return "the null hypothesis is rejected in favour of the alternative"
  return "there is insufficient evidence to reject the null hypothesis"
  
data = np.loadtxt("mydata.dat")
print("Null hypothesis: the data points in mydata.dat are all samples from a ")
print("normal random variable with expectation 20 and variance 4")
print("Alternative hypothesis: the data points in mydata.dat are not all samples from a ")
print("normal random variable with expectation 20 and variance 4")
print( hypothesisTest( data, 20, 4 ) )
  
