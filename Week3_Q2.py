def primeCheck(n,d=0):
    if n == 0:
        return False
    elif d == 0:
        d = n
        return primeCheck(n,d)
    elif n == 1:
        return False
    elif n == d:
        return True
    elif n%d == 0:
        return False
    else:
        primeCheck(n,d+1)
        
    
