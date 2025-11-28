#Ali Hasanpoor
#9821153

#import needed libraries---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------

#take inputs---------------------------------------------------------
l, a, b = map(float, input("please enter in order a stop point and a(begining interval) and b(end interval) with a space : ").split(" "))
f = input("please enter your function in this form (x)**2+2*(x) : ")
#--------------------------------------------------------------------

#start the method----------------------------------------------------
#determine the alpha as golden step
alpha = (np.sqrt(5)-1)/2

#determine a function for calculate value of input function
def func(f,x) :
    f = f.replace("x",str(x))
    return eval(f)

#if interval of [a,b] was less than l must be stop and show answer
if b-a < l :
    x1 = np.linspace(a,b,1000)
    y1 = [func(f,i) for i in x1]
    plt.plot(x1,y1)
    plt.show()
    print(f"x_min is in [{a},{b}]")
else :
    #else do steps of golden-section-method
    while b-a > l :
        lamda = a + (1-alpha)*(b-a)
        mu = a + alpha*(b-a)
        if func(f,lamda) >= func(f,mu) :
            a = lamda
        else :
            b = mu

#show answer
x1 = np.linspace(a,b,1000)
y1 = [func(f,i) for i in x1]
plt.plot(x1,y1)
plt.show()

print(f"x_min is in [{a},{b}]")
#--------------------------------------------------------------------