def odd_even(lst) :
    if len(lst) == 0 :
        return lst
    
    if lst[0] % 2 != 0 :
        return [lst[0]] + odd_even(lst[1:])
    else :
        return odd_even(lst[1:]) + [lst[0]]

lst = list(map(int,input().split()))
print(odd_even(lst))