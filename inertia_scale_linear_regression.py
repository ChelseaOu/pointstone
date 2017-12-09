import numpy as np 
from scipy.optimize import leastsq
import matplotlib.pyplot as plt 

Xi = np.array([0.08,0.12,0.19,0.23,0.26,0.30,0.34,0.37,0.42,0.46])
Yi = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])

k,b = [1,1]

class datas:

	p0 = [1,1]

	def __init__(self,X,Y):
		self.X = X
		self.Y = Y

	def linear_regression(self):

		global k
		global b

		def linear_func(p,x):
			k,b = p
			return k*x + b 

		def error(p,x,y):
			return linear_func(p,x) - y

		Params = leastsq(error,datas.p0,args = (self.X,self.Y))
		k,b = Params[0]
		print "k = ",k,"b=",b

data = datas(Xi,Yi)
data.linear_regression()


plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) 
x=np.linspace(0,.5,10)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) 
plt.legend()
plt.show()
