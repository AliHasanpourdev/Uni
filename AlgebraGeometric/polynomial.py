from collections.abc import Iterable


class Polynomial :
    def __init__(self, c) :
        self.degree = len(c)-1
        self.coefficent = c

    def __str__(self) :#write how display a polynomial
        s = f"{self.coefficent[0]}x^{self.degree}"
        for i in range(1,self.degree) :
            if self.coefficent[i] == 0 :
                continue
            elif self.coefficent[i] > 0 :
                s+=f"+{self.coefficent[i]}x^{self.degree-i}"
            else :
                s+=f"{self.coefficent[i]}x^{self.degree-i}"
        if self.coefficent[-1] == 0 :
            pass
        elif self.coefficent[-1] > 0 :
            s += f"+{self.coefficent[-1]}"
        else :
            s += f"{self.coefficent[-1]}"
        return s.replace("^1", "").replace("+0", "").replace("1x", "x")

    def __add__(self,other) :#write how add two polynomial
        new_coef = []
        dif = self.degree - other.degree
        if dif > 0 :
            l = dif*[0]
            l += other.coefficent
            for i in range(len(l)) :
                new_coef.append(self.coefficent[i]+l[i])
        if dif < 0 :
            l = -dif*[0]
            l += self.coefficent
            for i in range(len(l)) :
                new_coef.append(other.coefficent[i]+l[i])
        return Polynomial(new_coef)
    
    def __sub__(self,other) :#write how sub two polynomial
        new_coef = []
        dif = self.degree - other.degree
        if dif > 0 :
            l = dif*[0]
            l += other.coefficent
            for i in range(len(l)) :
                new_coef.append(self.coefficent[i]-l[i])
        if dif < 0 :
            l = -dif*[0]
            l += self.coefficent
            for i in range(len(l)) :
                new_coef.append(l[i]-other.coefficent[i])
        return Polynomial(new_coef)

    def value(self, x) :#value of polynomial in a special point
        s = str(self).replace("x", f"*({x})").replace("^", "**")
        return eval(s)
    
    def LT(self) :#leading term of polynomial
        l = self.degree*[0]
        return Polynomial([self.coefficent[0]]+l)
