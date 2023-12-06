import numpy as np

def eqn1(x, y):
    eq = round(6*x**3 + x*y - 3*y**3 - 4,6)
    return eq

def eqn2(x, y):
    eq = round(x**2 - 18*x*y**2 + 16*y**3 + 1,6)
    return eq

def deqn1x(x, y):
    eq = round(18*x**2 + y,6)
    return eq

def deqn1y(x, y):
    eq = round(x - 9*y**2,6)
    return eq

def deqn2x(x, y):
    eq = round(2*x - 18*y**2,6)
    return eq

def deqn2y(x, y):
    eq = round(-36*x*y + 48*y**2,6)
    return eq

def steqn1(x, y):
    eq = "{0} + {1} - {2} - 4".format(round(6*x**3,6),round(x*y,6), round(- 3*y**3,6))
    return eq

def steqn2(x, y):
    eq = "{0} - {1} + {2} + 1".format(round(x**2,6) ,round(18*x*y**2,6), round(16*y**3,6))
    return eq

def stdeqn1x(x, y):
    eq = "{0} + {1}".format(round(18*x**2,6),round(y,6))
    return eq

def stdeqn1y(x, y):
    eq = "{0} - {1}".format(round(x,6), round(9*y**2,6))
    return eq

def stdeqn2x(x, y):
    eq = "{0} - {1}".format(round(2*x,6) , round(18*y**2,6))
    return eq

def stdeqn2y(x, y):
    eq = "{0} + {1}".format(round(-36*x*y,6) ,round(48*y**2,6))
    return eq

x, y = 2,2
xi, yi = 1.005, 1.002
it = 0

while True:
    xk = np.array([[x],[y]])
    print("Iteration ",it+1)
    fx = np.array([[eqn1(x,y)],[eqn2(x,y)]])
    fdx = np.array([[deqn1x(x,y), deqn1y(x,y)],[deqn2x(x,y), deqn2y(x,y)]])
    fdxi = np.linalg.inv(fdx)
    print("F(x{}) = {}".format(it, np.array([[steqn1(x,y)],[steqn2(x,y)]])))
    print("F(x{}) = {}".format(it,fx))
    print("DF(x{}) = {}".format(it,np.array([[stdeqn1x(x,y), stdeqn1y(x,y)],[stdeqn2x(x,y), stdeqn2y(x,y)]])))
    print("DF(x{}) = {}".format(it,fdx))
    print("DF(x{})-1 = {}".format(it,fdxi))
    s=np.matmul(fdxi,fx)
    print("s",s)
    xk1 = np.subtract(xk,s)
    print("{} - {} = {}".format(xk,s,xk1))
    x, y = xk1[:, 0]
    x=float(round(x,5))
    y=float(round(y,5))
    print("Root x = ", x)
    print("Root y = ", y)
    it+=1
    if(x<=xi and y<=yi):
        break
