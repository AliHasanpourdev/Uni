import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def theta(f,x) :
    if "x" not in f :
        return int(f)
    return eval(f.replace("x", f"{x}"))


def twopart(a,b,eps,f) :
    x = sp.symbols("x")
    df = str(sp.diff(f))

    while b-a > eps :
        la = (a+b) / 2
        if int(la) == la :
            la = int(la)

        if theta(df,la) == 0 :
            c = (a+b)/2
            x = np.linspace(c-eps/2,c+eps/2,1000)
            y = [theta(f,i) for i in x]
            plt.plot(x,y)
            plt.scatter([la],[theta(f,la)],c="r")
            plt.show()
            return f"X_min = {la}"
        elif theta(df,la) > 0 :
            b = la
        else :
            a = la

    x = np.linspace(a,b,1000)
    y = [theta(f,i) for i in x]
    plt.plot(x,y,"c")
    plt.show()
    return f"X_min is in [{a},{b}]"


def main() :
    a, b, eps = map(lambda x : int(x) if int(float(x)) == float(x) else float(x), input("please enter a and b and eps : ").split())
    f = input("please enter a function for example (x)**3 -2*(x)**2 -3 : \n")
    print(twopart(a,b,eps,f))


if __name__ == "__main__" :
    main()