def eqn(x):
    eq = round(x**6 - 11*x**3 + 17*x**2 - 7*x + 1,5)
    return eq

def eqn1(x):
    # eq = x**3+x-1
    strin = "{} - {} + {} - {} + 1 ".format(round(x**6,5),round(11*x**3,5),round(17*x**2,5),round((7*x),5))
    return strin

def ex1(m, n):
    eq = round(m + 0.382*(n-m),5)
    return eq

def ex2(m, n):
    eq = round(m + 0.618*(n-m),5)
    return eq

def sx1(m, n):
    strin = "{} + 0.382 * {}".format(round(m,5),round(n-m,5))
    return strin

def sx2(m, n):
    strin = "{} + 0.618 * {}".format(round(m,5),round(n-m,5))
    return strin

a=0
b=1
e=0.02
print("a = ", a)
print("b = ", b)
print("e = ", e)

# fa=eqn(a)
# fb=eqn(b)
# print("f(a) = ", eqn1(a))
# print("f(a) = ", fa)
# print("f(b) = ", eqn1(b))
# print("f(b) = ", fb)
it = 1

while it<15:
    print("Iteration ",it)
    x1 = ex1(a,b)
    print("x1 = ", sx1(a,b))
    print("x1 = ", x1)
    x2 = ex2(a,b)
    print("x2 = ", sx1(a,b))
    print("x2 = ", x2)
    fx1 = eqn(x1)
    print("f(x1) = ", eqn1(x1))
    print("f(x1) = ", fx1)
    fx2 = eqn(x2)
    print("f(x2) = ", eqn1(x2))
    print("f(x2) = ", fx2)

    if(fx1 > fx2):
        a=x1
        b=b
    else:
        a=a
        b=x2

    print("a{} = {}".format(it, a))
    print("b{} = {}".format(it, b))

    it+=1
    if(b-a <= e):
        xz = round((a+b)/2,5)
        print("The root is x* = ",xz)
        break
