from polynomial import Polynomial


def divisible(f,g) :#check f and g are divisible
    if f.degree >= g.degree :
        return f.coefficent[0]%g.coefficent[0] == 0
    return -1

def LTdiv(f,g) :#divide of leading terms
    if divisible(f, g) :
        deg = (f.degree - g.degree)*[0]
        return Polynomial([int(f.coefficent[0]/g.coefficent[0])]+deg)
    return 0

def mul(f,g) :#multiplate Leading term of f and polynomial of g
    coef = g.coefficent
    co = [i for i in coef if i != 0]
    po = [g.degree+len(coef)-1-i for i in range(len(coef)) if coef[i] != 0]
    l = int(f.coefficent[0])*[0]
    for i in range(len(l)+1) :
        if i+1 in co :
            print("befor")
            l[i] = po[0]
            print("after")
            po = po[1:]
            print("finish")
    return Polynomial(l)



#----------------------------start program---------------------------
coef = list(map(int, input("please enter list of coeficent of polynomial f , seperated by one space : ").split(" ")))
coeg = list(map(int, input("please enter list of coeficent of polynomial g , seperated by one space : ").split(" ")))
f = Polynomial(coef)
g = Polynomial(coeg)
q = Polynomial([0])
r = f
while r.degree >= g.degree:
    q += LTdiv(r.LT(), g.LT())
    r -= mul(LTdiv(r.LT(), g.LT()),g)

print(f"riminder is {r} and quatient is {q}")