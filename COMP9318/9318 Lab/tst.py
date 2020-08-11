import numpy as np

a=np.sum([[0,1,2],[2,1,3]],axis=0)
b=np.sum([[0,1,2],[2,1,3]],axis=1)
c=np.multiply([[0,1,2],[2,1,3]],[[6,7,4]])
d=c.sum(axis=1)
e=c.sum(axis=0)
print(a)
print(b)
print(c)
print(d)
print(e)