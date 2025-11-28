import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def theta(f, x):
    if "x" not in f:
        return int(f)
    return eval(f.replace("x", f"{x}"))

def twopart(a, b, eps, la, f):
    x = sp.symbols("x")
    df = str(sp.diff(f, x, 1))
    ddf = str(sp.diff(f, x, 2))
    la0 = np.round(la, 4)
    la = np.round(la0 - (theta(df, la0) / theta(ddf, la0)), 4)
    key = True
    while key:
        if int(la) == la:
            la = int(la)
        if theta(df, la) == 0 :
            key = False
            x = np.linspace(la-eps/2, la+eps/2, 1000)
            y = [theta(f, i) for i in x]
            plt.plot(x, y)
            plt.show()
            return f"X_min = {la}"
        elif theta(df, la) > 0:
            b = la
        else:
            a = la
        if abs(la - la0) > eps or abs(theta(df, la0)) > eps:
            key = False
        la0 = np.round(la, 4)
        la = np.round(la0 - (theta(df, la0) / theta(ddf, la0)), 4)
    x = np.linspace(a, b, 1000)
    y = [theta(f, i) for i in x]
    plt.plot(x, y, "c")
    plt.show()
    return f"X_min is in [{a},{b}]"

def main():
    a, b, eps, la = map(lambda x: int(x) if int(float(x)) == float(x) else float(x), input("Please enter a and b and eps and lamda0 : ").split())
    f = input("Please enter a function for example (x)**3 -2*(x)**2 -3 : \n")
    print(twopart(a, b, eps, la, f))

if __name__ == "__main__":
    main()