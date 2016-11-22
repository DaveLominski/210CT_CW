import random

def shuffleArrays():

    array = []                                                                              #an empty arrays where numbers will be inserted from the user input
    maxArray = int(input("How many numbers would you like to input into an array? "))       #asking a user how long they want their array to be.

    while len(array) < maxArray :                                                           #this is going to ask a user for another number to add to an array as long as the length of the
        arrayq = input("Please input integers that you want to be shuffled :")              #array is less than the maxArray which is set by the user.
        array.append(arrayq)                                                                #adds the number into the array

    if len(array) > 1:                                                                      #Fisher-Yates algorithm, if the length of an array is larger than 1, the following statements will run
        index = len(array) - 1                                                              #take one away due to zero based array
        while index > 0:                                                                    #as long as the index variable is more than 0 the while loop will run
            ranInt = random.randint(0, index)                                               #selects a random number between 0 and the index value and assigns it to a ranInt variable name
            array[index], array[ranInt] = array[ranInt], array[index]                       #swaps array[index] and array[randInt] around, this is basically how an array is shuffled
            index -= 1                                                                      #decreases value of index variable by 1 everytime the while loop is run to make sure its not an infinite loop
        print("The shuffled array is :" ,array)                                             #prints a statement showing the shuffle array




shuffleArrays()