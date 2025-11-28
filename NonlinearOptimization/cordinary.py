import numpy as np
import sympy as sp

def func(f, c, v, k="lam") :
    f = f.replace("lam", "(lam)")
    l = sp.symbols(k)
    for i in range(len(c)) : 
        f = f.replace(f"{c[i]}",f"{v[i]}")
    try :
        return np.round(eval(f),4)
    except NameError :
        return str(sp.simplify(f))


def find_min(f) :
    lam = sp.symbols("lam")
    f1 = str(sp.diff(f,lam,1)).replace("lam", "(lam)")
    f2 = str(sp.diff(f,lam,2)).replace("lam", "(lam)")
    l = []
    sol = sp.solve(f1,lam)
    sol = [complex(sp.simplify(i)) for i in sol]
    for i in sol :
        if i.imag == 0 :
            l.append(i.real)
    for i in l :
        if func(f2,["lam"],[i]) > 0 :
            return i

def cordinary(f, x, eps) :
    n = len(x)
    y = x
    bul = True
    k = 1
    j = 1
    while bul :
        s = y.copy()
        s[j-1] = str(s[j-1])+"+lam"
        new_func = func(f,["x", "y"],s)
        lamn = find_min(new_func)
        y[j-1] += lamn
        if j<n :
            j += 1
        elif j == n :
            x0 = x
            x = y
            t = [x[i]-x0[i] for i in range(len(x))]
            if float(np.linalg.norm(np.array(t))) < eps :
                bul = False
                break
            else :
                j = 1
    return y


def main() :
    eps = float(input("please enter epsilon for stop condition : "))
    x = list(map(float, input("please enter members of x_start : ").split(" ")))
    f = input("please neter your function in form of python : ")
    print(cordinary(f, x, eps))


if __name__ == "__main__" :
    main()
