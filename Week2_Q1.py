def perfSq(number):
    if number >= 0:
        square =  number**(1/2)
        square = square - (square % 1)
        square = square * square
        return square


    else:
        print("Error ! Try again with a positive integer")

perfSq(50)