

def removeVowels(c = 0):

    vowels = ["a","e","i","o","u"]                  #list of all the vowels

    if c == len(vowels):                            # 
        return True
    elif vowels[c] in s1:                           #check every vowel if it's in the word
        s1.remove(vowels[c])                        #removes a vowel from the word if found
        print(s1)                                   #prints the word after one vowel has been removed
        removeVowels(c)                             #calls the function to check if there are multiples of the same vowel

    else:                                           
        removeVowels(c + 1)                         #calls the function if there are no more multiples of the vowels and adds one to the counter to move onto the next vowels in the list



s = input("Type a word : ")                         #asks a user for input
s1 = list(s)                                        #changes the user input into a list



removeVowels()
