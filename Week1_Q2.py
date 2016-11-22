def trailingZeros():
    number = int(input("Give me a number: "))           #Asking a user for a number to check

    trailing = 0                                        #A starting value for a variable
    for i in range(5, number+1):                        #A for loop checking every number between 5 and the number user inputted + 1
        factorial = int(i)                              #making sure i is an integer data type
        while factorial:                                #an infinite while loop to make sure the calculations below is made for each number
            if factorial % 5 == 0:                      #checking if a number is a factor of 5
                trailing += 1                           #if the number is a factor of 5, add 1 to trailing variable
                factorial = factorial / 5               #if the quotient is also a factor of 5, it does the same calculcation, e.g. 25 % 5 = 0 therefore adds one to trailing, then does                                       #25/5 = 5, since 5%5 = 0, the while loop runs again
            else:                                       #if a number is not a factor of 5, the while loop breaks and goes back to the for loop
                break

    print("There are ",trailing, "zeros")               #prints how many trailing zeros there are


trailingZeros()
