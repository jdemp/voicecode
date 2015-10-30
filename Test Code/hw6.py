'''For this problem, start with the following list of words:

teams = ["Orioles", "Red Sox", "Rangers", "Indians", "Tigers", "Astros", "Royals", "Angels"]

Part 1
------
Write a program that maps the teams list of words to a different list of integers 
representing the lengths of the corresponding words. Use a for-loop.  
Print each item in the teams list and the corresponding string length from the list of integers.
Your list of string lengths must be stored in a separate list from the teams list.

Part 2
------
Replace "Red Sox" with "Mets", using a list method, recalculate the list of integer lengths 
and reprint the teams list and the corresponding lengths.

Part 3
------
Pop "Angels" off the list and append "Marlins".  
Recalculate the lengths and reprint the teams and lengths.
'''



# Homework 6 Answer
#
def main() :

    teams = ["Orioles", "Red Sox", "Rangers", "Indians", "Tigers", "Astros", "Royals", "Angels"]

    teamLengths = getLengths(teams)
    printTeams(teams, teamLengths)
    
    teams[1] = "Mets"
    teamLengths = getLengths(teams)
    printTeams(teams, teamLengths)
    
    teams.pop()
    teams.append("Marlins")
    teamLengths = getLengths(teams)
    printTeams(teams, teamLengths)
 

# getLengths()
# Pass in a list of strings and returns a list of lengths of each 
# string
#
def getLengths(teams) :
    
    teamLengths = []

    for name in teams :
        teamLengths.append(len(name))

    return teamLengths

# printTeams()
# Pass in a list of teams as strings and a list of integer
# string lengths for each corresponding team and print both
#
def printTeams(teams, teamLengths) :

    print("\nNew Run\n----------\n")
    index = 0
    for name in teams :
        print('%8s: %d'  % (name, teamLengths[index]))
        index += 1

main()
    
