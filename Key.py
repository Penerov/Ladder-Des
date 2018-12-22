import Ferma 
import random as rnd

def f1(x):
    a = 4
    b = 101
    x = ((a * x) + b)
    return (x)
def f2(x):
    a = 3
    b = 92
    x = ((x / a) + b)
    return (x)   
def gpsc(x):
    i=0
    mas=[]
    while i<100:
    
        if i%2==0:
            x=f1(x)
        else:
            x=f2(x)
        if x<min_key:
            x=f1(x)
        if x>max_key:
            x=f2(x)
        mas.append(int(x))
        i+=1
    rnd_num=int(rnd.uniform(0,99))
    key=Ferma.find_primes(mas[rnd_num],100,1)
    tmp='{0:b}'.format(key[0])
    while len(tmp)!=64:
        tmp='0'+tmp
    return(tmp)
