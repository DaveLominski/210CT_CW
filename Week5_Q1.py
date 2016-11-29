def sequences(L, a, b):
    for i in range (0, len(L)):                                     #the for loops that goes through the whole list
        if i == 0:
            a.append(L[0])                                          #always adds the first element of the list to a
        elif L[i] <= (L[i-1]):                                      #if value of i is smaller than or equal to the value before it
            if len(a) > len(b):                                     #if length of list a is larger than length of list b
                b = a[:]                                            #list b = a
                a[:] = []                                           #clear all the elements in list a
                a.append(L[i])                                      #add element i to the list a
            else:                                                   #if length of b is larger than length of a
                a[:] = []
                a.append(L[i])
        elif L[i] > (L[i-1]):                                       #if value of i is larger than the previous value
            a.append(L[i])                                          #add the value to the list a
            if len(a) > len(b):                                     #if length of a is larger than b, print list a
                print("The longest sequence so far is ", a)
            elif len(a) == len(b):                                  #if length of list a and b are the same, print both of them
                print("The two longest sequences are ", a, b)
            else:                                                   #if length of b is larger, print b
                print("The longest sequence so far is ", b)
        else:
            pass


sequences([1,2,3,4,4,4,1,2,3,4,5],[],[])
