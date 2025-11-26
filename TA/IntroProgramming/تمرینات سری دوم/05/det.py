def det(matris):
    len_matris = len(matris)
    if len_matris == 1:
        return matris[0][0]
    determinan = 0
    for i in range(len_matris):   
        determinan +=  ((-1) ** i) * matris[0][i] * det([r[:i] + r[i+1:] for r in matris[1:]])
    return  determinan

n = int(input())
matris = []
for i in range(n):
    matris.append(list(map(float , input().split())))
print(int(det(matris)))