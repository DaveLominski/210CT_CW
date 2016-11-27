def primeNumber(number, counter=None):
    if counter == 1:
        print(number, "is a prime number")
    elif number < 2:
        print(number, "is not a prime number")
    elif counter == None:
        counter = number-1
        primeNumber(number, counter)
    elif number % counter == 0:
        print(number, "is not a prime number")
    elif number % counter != 0:
        primeNumber(number, counter - 1)

    else:
        return primeNumber(number, counter - 1)
    


primeNumber(29)
