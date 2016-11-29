def binarySearch(array, a, b):
    firstIndex = 0                                              #first index in an array is always 0
    lastIndex = (len(array) - 1)                                #since array start with 0, to get an actual length of an array we need to take 1 away
    itemFound = False                                           

    while firstIndex <= lastIndex and not itemFound:            
        mp = (firstIndex + lastIndex) // 2                      #finds the mid-point
        if array[mp] >= a and array[mp] <= b:                   #if statement that checks if midpoint is in the between the numbers that user inputted
            itemFound = True                                    #if number is in range, variable value is change to TRUE
        else:   
            if a < array[mp] and b < array[mp]:                 #if a and b are smaller than the mid-point, take one away from the mid-point,    
                lastIndex = mp - 1                              #and start looking for a number in the first half of an array
            else:
                firstIndex = mp + 1                             #otherwise add one to the mid-point and start looking for a number in the second half of an array
    print(itemFound)


binarySearch([1,7,10,15,30,100,343],1,100)







