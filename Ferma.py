import random

def expmod(osn,p,m):
    if p%2==0:
        return (expmod(osn,p//2,m))**2%m
    else:
        return (osn*expmod(osn,p-1,m))%m

def ferma1(n):
    a=random.randint(2,n-1)
    return expmod(a,n-1,n)==1

def ferma2(n, kkk):
    for test in range(kkk):
        if not ferma1(n):
            return False
    return True

def findpr(max_num, max_test, q=-1):
    pr=[]
    for num in range(max_num, 2, -1):
        if ferma2(num, max_test):
            pr.append(num)
        if q>=0 and len(pr)>=q:
            break
    return pr
