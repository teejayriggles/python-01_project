####################################
#region        Imports
# TODO:
# Import random so we can pick a random choice for the computer
import random
# Import system from os so we can clear the screen
from os import system
# Import Fore and Style from Colorama so we can add color to our text
from colorama import Fore, Style
#endregion
####################################

#////////////////////////////////////////////////////////////////////

####################################
#region        Global Variables 

# I created these variables for some of the print statements we'll use. 
divider = f'{Style.RESET_ALL}{Fore.CYAN}------------------------------------------------------{Fore.RESET}'
firstPlayAgain = f'Would you like to play rock, paper, scissors? [y/n]\n{Style.BRIGHT}'
otherPlayAgain = f'Would you like to play again? [y/n]\n{Style.BRIGHT}'
didNotUnderstand = f'I\'m sorry I only understand \'y\' or \'n\'{Style.BRIGHT}'
choicePrompt = f'Please pick "Rock", "Paper", or "Scissors" [r/p/s].\n{Style.BRIGHT}'
didNotUnderstandChoice = f'I\'m sorry I only understand \'r\',\'p\' or \'s\'{Style.BRIGHT}'
msgWin = f'{Fore.GREEN}You win!{Fore.RESET}'
msgLose = f'{Fore.RED}You lose!{Fore.RESET}'
msgTied = f'{Fore.YELLOW}You tied!{Fore.RESET}'

# TODO: Create an array variable named userChoices that has "r","p","s"

# TODO: Create an array variable named compChoices that has "Rock","Paper","Scissors"

# TODO: Create an integer variable named wins equal to 0

# TODO: Create an integer variable named losses equal to 0

# TODO: Create an integer variable named ties equal to 0

# I created this to clear out the screen when we start the program
_=system('clear')

#endregion
####################################

#////////////////////////////////////////////////////////////////////

####################################
#region        Functions 


#####################################
# wantToPlay(firstTime)
# 
# Parameters: 
#   - firstTime (Boolean): True if it's the first time we're playing.
#
# Return: 
#   - play (Boolean)
#
# This function asks the user if they would like to play. 
# Then calls the fucntion wantToPlayValidate(answer).
##################################### 
def wantToPlay(firstTime):
    #TODO: If first time is true, set userAnswer equal to the input from the user 
    # when prompting them with firstPlayAgain ( input(firstPlayAgain) )

    #TODO: Else set userAnswer equal to the input from the user 
    # when prompting them with otherPlayAgain ( input(otherPlayAgain) )

    #TODO: Return the results from valdiateWantToPlay passing userAnswer as the parameter ( validateWantToPlay(userAnswer) )
    return

#####################################
#  validateWantToPlay(answer)
#
# Parameters:
#   - answer (String)
#
# Return:
#   - play (Boolean)
#
# This function validates the users input to play (again)
# If it validates yes/no it returns boolean.
# If it cannot validate it reprompts and calls playValidate(answer) to validate.
##################################### 
def validateWantToPlay(answer):

    # TODO: If answer is equal to (==) 'y' then return True

    # TODO: Elif answer is equal to (==) 'n' then return False

    # TODO: Else :
    #       - Print the didNotUnderstand variable
    #       - Print the divider variable 

    # TODO: Return the value from validateWantToPlay() using input(firstPlayAgain) as the parameter
    return

#####################################
#  getUserChoice()
#
# Return userChoice (String)kd
#
# Asks the user for their choice
# Call validateUserChoice(userChoice) 
##################################### 
def getUserChoice():
    # TODO: Set the variable userChoice equal to the user input using the variable choicePrompt as the prompt ( input(choicePrompt) )

    # TODO: Return the value of validateUserChoice() using the variable userChoice as the parameter
    return

#####################################
#  validateUserChoice(userChoice)
#
# Parameter:
#   - userChoice (String)
#
# Return:
#   - validatedChoice (String)
#
# Gets the userChoice and validates it.
# If validated it returns
# If not validated it re-prompts and calls validateUsersChoice(userChoice)
##################################### 
def validateUserChoice(userChoice):
    # TODO: If the value of userChoice is in the array userChoices
    #       - Return the value from compChoices with the same index as the userChoice from userChoices

    # TODO: Print the variable didNotUnderstandChoice

    # TODO: Return the value of validateUserChoice() using input(choicePrompt) as the parameter
    return 

#####################################
#  getOutcome(userChoice,compChoice)
#
# Parameters:
#   - userChoice (String) 
#   - compChoice (String) 
# 
# Return: Outcome (String)
# 
# This fucntion takes the user choice and comp choice
# It compares the two and finds out if the user won, lost, or tied
# It then updates the record and returns the result 
##################################### 
def getOutcome(userChoice,compChoice):
    # Reference the variables you created for wins, losses, and ties so we can add to them
    # We will have to use the "global" identitifier here so the program knows we want the variables we already created
    # example : global wins, losses, ties

    # Here we print out what the user chose, and what the computer chose
    print(f'{Style.RESET_ALL}You chose {Style.BRIGHT}{userChoice}{Style.RESET_ALL} and the computer chose {Style.BRIGHT}{compChoice}{Style.RESET_ALL}')

    # TODO: If userChoice is equal to (==) compChoice
    #       Add 1 to ties
    #       Return msgTied

    # TODO: If userChoice is equal to (==) "Rock"

        # TODO: If compChoice is equal to (==) "Paper"
        #       Add 1 to losses
        #       Return msgLose
        
        # TODO: Else:
        #       Add 1 to wins
        #       Return msgWin 

    # TODO: Elif userChoice is equal to (==) "Paper"

        # TODO: If compChoice is equal to (==) "Scissors"
        #       Add 1 to losses
        #       Return msgLose
        
        # TODO: Else:
        #       Add 1 to wins
        #       Return msgWin 
    # TODO: Else:

        # TODO: If compChoice is equal to (==) "Rock"
        #       Add 1 to losses
        #       Return msgLose
        
        # TODO: Else:
        #       Add 1 to wins
        #       Return msgWin 

    return

#####################################
#  printRecord()
# 
# This fucntion prints the wins, losses, and ties
##################################### 
def printRecord():
    print("Here's your record:")
    print(f'{Fore.GREEN}\tWins: {wins}{Fore.RESET}')
    print(f'{Fore.RED}\tLosses: {losses}{Fore.RESET}')
    print(f'{Fore.YELLOW}\tties: {ties}{Fore.RESET}')
    print("Goodbye!")

#endregion
####################################

#////////////////////////////////////////////////////////////////////

####################################
#region        Execution 

# TODO: Print divider

# TODO: Set a variable playAgain equal to wantToPlay() and enter True as the parameter

# TODO: While playAgain is equal to (==) True :

#       TODO: Set a variable userChoice equal to getUserChoice()

#       TODO: Set a variable compChoice equal to compChoices[] using random.randint(0,2) as the index ( compChoices[random.randint(0,2)] )

#       TODO: Print the result from calling getOutcome() using userChoice and compChoice as the parameters ( getOutcome(userChoice,compChoice) )

#       TODO: Print divider

#       TODO: Set the variable playAgain equal to wantToPlay() and enter False as the Parameter

# TODO: Print divider

# TODO: Call printRecord() to print out the record and say goodbye


#endregion
####################################
