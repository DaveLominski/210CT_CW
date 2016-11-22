def sequences(L, a, b):
    for i in range (0, len(L)):
        if i == 0:
            a.append(L[0])
        elif L[i] <= (L[i-1]):
            if len(a) > len(b):
                b = a[:]
                a[:] = []
                a.append(L[i])
            else:
                pass
        elif L[i] > (L[i-1]):
            a.append(L[i])
            if len(a) > len(b):
                print("The longest sequence so far is ", a)
            elif len(a) == len(b):
                print("The two longest sequences are ", a, b)
            else:
                print("The longest sequence so far is ", b)
        else:
            pass


sequences([1,2,3,4,5,8,9,10,1,2,3,4,1],[],[])
