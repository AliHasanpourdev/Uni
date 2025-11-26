def Permutation(num,mystr=""):
    if num==0:
        print(mystr)
    else:
        for item in ['0', '1']:
            Permutation(num-1,mystr+item)
num=int(input())
Permutation(num)
