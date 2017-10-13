import numpy as np

n=11
x=np.linspace(0,1,n)
print("with %i points x="%n,x)

y=x
y[0]=-1
print(x)
print('x has changed!!!')



