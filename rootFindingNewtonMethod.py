def eqn1(x):
    eq = round(x**3-(10*x**2)+5 , 6)
    return eq

def eqn2(x):
    eq = round(3*x**2-(20*x),6)
    return eq

def eqn11(x):
    strin = "{0} - {1} + 5 ".format(round(x**3,6),round((10*x**2),6))
    return strin

def eqn21(x):
    strin = "{0} - {1}".format(round(3*x**2,6),round((20*x),6))
    return strin

a=0.7
print("a = ",a)
e=0.0002
print("e = ",e)

fa=eqn1(a)
fda=eqn2(a)
# print("Iteration 1")
# print("f(a) = ", eqn11(a))
# print("f(a) = ", fa)
# print("f'(a) = ", eqn21(a))
# print("f'(a) = ", fda)
a1=round(a-(fa/fda),6)
# print("a1 = ", a1)
it = 1

while True:
    print("Iteration ",it)
    print("x{0} = {1}".format(it-1,a))
    fa=eqn1(a)
    fda=eqn2(a)
    print("f(x) = ", eqn11(a))
    print("f(x) = ", fa)
    print("f'(x) = ", eqn21(a))
    print("f'(x) = ", fda)
    print("x{3} = {0} - ({1}/{2})".format(a,fa,fda,it))
    a1=round(a-(fa/fda),6)
    print("x{0} = {1}".format(it,a1))
    it+=1
    if(abs(a1-a) <= e):
        break
    else:
        a=a1




