#=======================================================
# Assignment #3
# Your Name Here
#=======================================================
def main() :    
    
    doTestOne()
    doTestTwo()
    doTestThree()

#-------------------------------------------------------
# doTestOne()
# Determines whether a number entered by the user is odd
# or even
#-------------------------------------------------------
def doTestOne() :
    
    userInput = int(input("Please enter an integer: "))
    
    if (userInput % 2 == 0) :
        print(userInput, " is even")
    else :
        print(userInput, " is odd")
    
#--------------------------------------------------------
# doTestTwo()
# Determines if the variables hungry and thirsty are True
# or False and prints a message accordingly
#
# Possible states are:
# hungry and thirsty are true
# hungry is false, thirsty is true
# hungry is true and thirsty is false
# hungry is false and thirsty is false
#--------------------------------------------------------    
def doTestTwo() :
    
    hungry = True
    thirsty = False
    
    if (hungry == True and thirsty == True) :
        print("Hungry and thirsty are true")
    
    elif (hungry == False and thirsty == True) :
        print("Hungry is false and thirsty is true")
        
    elif (hungry == True and thirsty == False) :
        print("Hungry is true and thirsty is false")
        
    else :
        print("Hungry is false and thirsty is false")

#-------------------------------------------------------
# doTestThree()
# Retrieve a number from a user
# Determine if the number is divisible by 2 and or 3
# There are four possible states
#
# divisible by 2 and 3
# divisible by 2 but not 3
# not divisible by 2 but divisible by 3
# not divisible by 2 or 3
#------------------------------------------------------     
def doTestThree() :

    userInput = int(input("Please enter an integer"))
    
    if (userInput %2 == 0 and userInput %3 == 0) :
        print(userInput, " is divisible by 2 and 3")
    
    elif (userInput %2 == 0 and userInput %3 != 0) :
        print(userInput,  " is divisible by 2 but not 3")
        
    elif (userInput %2 != 0 and userInput %3 == 0) :
        print(userInput, " is not divisible by 2 but is divisible by 3")
    
    else :
        print(userInput, " is not divisible by 2 or 3")
        
   

main()