def primeNumber(number, counter=None):
    #if the number is not divisible by the counter as it goes down, and the
    #counter gets to 1, it means that the number only divides by itself and 1
    if counter == 1:
        print(number, "is a prime number")
    #if number is below 2, it's not a prime number
    elif number < 2:
        print(number, "is not a prime number")
    #only runs at the beginning to make the counter 1 less than a number
    elif counter == None:
        counter = number-1
        primeNumber(number, counter)
    #checks if the number is divisible by a counter
    elif number % counter == 0:
        print(number, "is not a prime number")
    #if the number is not divisible by the counter, the counter decreases by 1
    else:
        return primeNumber(number, counter - 1)
    

primeNumber(11)