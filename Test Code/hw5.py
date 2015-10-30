#====================================================================
# Homework #5
# Counts the number of occurences of vowels in a sentence entered by
# the user
#====================================================================
def main() :
    
    sentence = input("Please enter a word: ")
    sentence.lower()

    print("The letter a is found: ", letterCount("a", sentence), "times")
    print("The letter e is found: ", letterCount("e", sentence), "times")
    print("The letter i is found: ", letterCount("i", sentence), "times")
    print("The letter o is found: ", letterCount("o", sentence), "times")
    print("The letter u is found: ", letterCount("u", sentence), "times")

#---------------------------------------------------------------    
# lettercount()
# Parameters letterToMatch and sentence
# Count the occurences of letterToMatch in sentence and return
# the number of occurences
#---------------------------------------------------------------    
def letterCount(letterToMatch, sentence) :
    
    letterCount = 0
    
    for currentLetter in sentence :
        if (currentLetter == letterToMatch) :
            letterCount += 1
    
    return letterCount

main()
