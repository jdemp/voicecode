# Assignment 4
#
import random

def main() :
    
    ranNum = random.randint(1,50)
    numTries = 1
    guessedNum = 0
    
    while (guessedNum != ranNum):

        guessedNum = int(input("Please guess another number between 1 and 50: "))
        
        if (guessedNum < ranNum):
            print("\nHigher")
            
        elif (guessedNum > ranNum):
            print("\nLower")        
        else:
            break
		
		numTries += 1
    
    print("\nYou got it in " ,numTries, " attempts")
    
main()