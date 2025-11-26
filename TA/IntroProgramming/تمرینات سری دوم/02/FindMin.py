p =list(map(float, input().split())) 
def mini(a):
    if len(a) == 1:
        return a[0]
    else:
        min0 = mini(a[1:])
        if a[0] < min0:
            return a[0]
        else:
            return min0
print(mini(p))