def fact(x):
    if x<0:
        return None
    if x==1:
        return 1
    if x==0:
        return 1
    return x * fact(x-1)
def perm(a,b):
    if a==b>0:
        return fact(a)
    elif a>b>0:
        result=int(fact(a)/fact(a-b))
        return result
    else:
        return None
def com(a,b):
    if a==b>0:
        return 1
    elif a>b>0:
        result=int(fact(a)/(fact(a-b)*fact(b)))
        return result
    else:
        return None
