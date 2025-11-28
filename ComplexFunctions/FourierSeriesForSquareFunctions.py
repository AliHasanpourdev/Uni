import matplotlib.pyplot as plt
import numpy as np
#----------variables----------
n = int(input("How many terms of the Fourier series are needed to approximate the function? :"))
a = -1 * np.pi
b = np.pi
#----------create fourier series of f(x) value function----------
def sigma(n, x) :
    s = []
    for i in range(1, n+1) :
        s.append((((4)/((np.pi)))*((np.sin((2*i - 1)*(x)))/(2*i - 1))))
    return sum(s)
#----------plot the function----------
x = np.linspace(a, b, 500)
y = sigma(n,x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, linestyle=':')
ax.tick_params(labelcolor='#112233', labelsize='medium', width=1)
label = f"{n}th" if n>2 else "1st" if n==1 else "2nd"
plt.plot(x,y,"#dd2211", label=label)
plt.title(label=f"The diagram of the {label} partial sum of The Fourier series for the function")
plt.legend()
plt.show()