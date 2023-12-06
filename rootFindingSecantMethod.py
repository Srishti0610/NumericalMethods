def eqn(x):
    eq = round(x**2-2,6)
    return eq

def eqn1(x):
    strin = "{0} - 2 ".format(round(x**2,6))
    return strin

x = 1
y = 2
e=0.00002

# fx=eqn(x)
# fy=eqn(y)
# print(fx, fy)

# yi = round(y - ((fy)*(y-x)/(fy-fx)),6)
# print("yi = ", yi)

# fyi=eqn(yi)

# print(fyi)
it = 1


while True:
    print("Iteration ",it)
    print("x{0} = {1}".format(it-1,x))
    print("x{0} = {1}".format(it,y))
    fx=eqn(x)
    fy=eqn(y)
    print("f(x{0}) = {1}".format(it-1, eqn1(x)))
    print("f(x{0}) = {1}".format(it-1, fx))
    print("f(x{0}) = {1}".format(it, eqn1(y)))
    print("f(x{0}) = {1}".format(it, fy))

    yi = round(y - ((fy)*(y-x)/(fy-fx)),6)
    print("x{0} = {1}".format(it+1, yi))
    it+=1
    if(abs(yi-y) <= e):
        break
    else:
        x = y
        y = yi

    





