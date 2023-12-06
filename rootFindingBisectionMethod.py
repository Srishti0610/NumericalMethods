def eqn(x):
    # eq = x**3+x-1
    # print("--", round(x**3,6),"-",round((10*x**2),6),"+",5)
    eq = round(x**3-(10*x**2)+5 , 6)
    return eq

def eqn1(x):
    # eq = x**3+x-1
    strin = "{0} - {1} + 5 ".format(round(x**3,6),round((10*x**2),6))
    return strin

a=0.6
b=0.8
e=0.0002
print("a = ", a)
print("b = ", b)
print("e = ", e)

fa=eqn(a)
fb=eqn(b)
print("f(a) = ", eqn1(a))
print("f(a) = ", fa)
print("f(b) = ", eqn1(b))
print("f(b) = ", fb)
it = 1

if(fa*fb < 0):
    print("Root lies within since f(a)*f(b) < 0 ")
    while (abs((b-a)/2) > e):
        print("Iteration ",it)
        it+=1
        print("a = ",a, " b = ",b)
        fa=eqn(a)
        fb=eqn(b)
        print("f(a) = ", eqn1(a))
        print("f(a) = ", fa)
        print("f(b) = ", eqn1(b))
        print("f(b) = ", fb)
        c=round((a+b)/2 , 5)
        print("c = ", c)
        fc=eqn(c)
        print("f(c) = ", eqn1(c))
        print("f(c) = ", fc)
        if(fc == 0):
            print("Root is ", c)
            break
        elif(fa*fc < 0):
            b=c
        else:
            a=c
elif(fa*fb > 0):
    print("Root does not lie within")
elif(fa*fb == 0):
    print("Root is either a or b")






