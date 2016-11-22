def reversingWordsInaSentence():
    a = str(input("Enter a sentence that you want to be reversed :"))           #asking a user a sentence that they want to be reversed
    for i in a:                                                                 #starts a for loop which goes through every character in the user input
        b = a.split(" ")                                                        #splits the words in a sentence, detects a new word whenever there is a SPACE in the sentence
        c = b[::-1]                                                             #reverses a list
    for j in c:                                                                 #a for loop that changes a list into normal looking sentence
        print(j, end= " ")                                                      #prints the sentence, end= " " basically takes care of the sentence being in one line







reversingWordsInaSentence()