import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
print()

#a. Create a discrete random variable with poissonian distribution and plot its probability 
#mass function (PMF), cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable

# a:
dist = stats.poisson(10)

x = np.linspace(0,22,23)
PMF = dist.pmf(x)
CDF = dist.cdf(x)
random_realizations_poisson = dist.rvs(1000)
plt.figure(figsize=[4.5,3.6])
plt.hist(random_realizations_poisson, bins=np.linspace(0.5,22.5,23), density=True)
plt.plot(x,PMF)
plt.plot(x,CDF)
#plt.show()

# b:
dist = stats.norm(10,np.sqrt(10))

x = np.linspace(0,20,1000)
PDF = dist.pdf(x)
CDF = dist.cdf(x)
random_realizations_norm = dist.rvs(1000)
#plt.figure(figsize=[4.5,3.6])
plt.hist(random_realizations_norm, bins=100, density=True)
plt.plot(x,PDF)
plt.plot(x,CDF)
plt.show()

# c:
result = stats.ttest_ind(random_realizations_poisson,random_realizations_norm)
print(result)
print("The distributions look indistinguishable using this a t-test. We need a better test.")