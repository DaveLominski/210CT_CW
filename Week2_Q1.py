def perfSq(number):
    if number >= 0:
        # square roots a number inserted by a user
        square =  number**(1/2)
        # takes away square rooted number and takes away the decimal from the square rooted number
        square = square - (square % 1)
        #squares the number to find the closest perfect square number
        square = square * square
        return square


    else:
        print("Error ! Try again with a positive integer")

print(perfSq(69))