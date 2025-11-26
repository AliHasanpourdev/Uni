def f(n, k, arr=[], start=1):
    if len(arr) == k:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n + 1):
        if(n - i >= k - len(arr) - 1):
            f(n, k, arr + [i], i + 1)
n,k = input().split()
f(int(n), int(k))