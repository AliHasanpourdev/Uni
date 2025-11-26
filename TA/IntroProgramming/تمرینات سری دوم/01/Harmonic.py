def h(n):
    if n==1:
        return 1
    else:
        return (1/n)+h(n-1)


n = int(input())
print(round(h(n),4))
