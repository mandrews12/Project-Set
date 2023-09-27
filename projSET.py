# Meghan Andrews, 11/20/22, Final Project - SET (12/13/22)

# I chose to do the SET programming project which is a computerized version of the game
# SET. The program generates 12 random cards and displays them to the user where the user
# will be prompted to choose 3 cards they believe are a set. The program will then
# determine if the cards are indeed a SET or not.

# imports random function to generate the 12 random cards from the deck
import random


# function to create all possible combinations of the SET deck
def createDeck():
    # creates the empty deck list and possible choices for the four elements
    deck = []
    num = ['1','2','3']
    colors = ['R','G','P']
    shade = ['S','O','P']
    shape = ['O','S','D']
    # takes the 3 possible choices of the four elements and computes every
    # possible combination, saves each combination as a string, and appends
    # each string to the list
    for i in range(0,3):
        first = num[i]
        for i in range(0,3):
            second = colors[i]
            for i in range (0,3):
                third = shade[i]
                for i in range(0,3):
                    fourth = shape[i]
                    card = first + second + third + fourth
                    deck.append(card)
    return deck


# function that generates the 12 random cards from the deck and appends them to a list
def generatePlayCards(deck):
    chosenCards = []
    i = 0
    while i < 12:
        # generates a random number from 0 to 80 and appends the corresponding card
        # to the choosen cards list 
        x = random.randint(0,80)
        # checks to make sure the cards has not been choosen already
        if deck[x] not in chosenCards:
            chosenCards.append(deck[x])
            i += 1
    return chosenCards


# function to ask the user to input three cards they believe makes a SET and returns
# a list of the cards they chose
def getCards(chosenCards):
    playerCards = []
    i = 1
    while i < 4:
        card = input(str(i)+": ")
        # checks if the inputed card is in the choosen cards dislpayed to the user
        # and if it is not or has been choosen already, asks the user to choose again
        if card not in chosenCards:
            print("Not a valid choice, please choose again")
        elif card in playerCards:
            print("You have already chosen that card, please try again")
        else:
            playerCards.append(card)
            i += 1
    return playerCards


# determins if the cards selected by the player are a SET
def isSET(playerCards):
    # splits the 3 different cards out of the list
    c1 = playerCards[0]
    c2 = playerCards[1]
    c3 = playerCards[2]
    setList = []
    # goes through each element in each card and compares them
    for i in range(0,4):
        # checks to see if the corresponding elements in each card are all the same
        if c1[i] == c2[i] and c2[i]==c3[i]:
            set = 1
            setList.append(set)
        # checks to see if the corresponding elements in each card are all different
        elif c1[i] != c2[i] and c2[i] != c3[i]:
            set = 1
            setList.append(set)
        # if both the previous cases are false, the elements do not make a set
        else:
            set = 0
            setList.append(set)
    # compares the results of the elements to determin if the cards as a whole form a SET
    if setList[0] == 1 and setList[1] == 1 and setList[2] == 1 and setList[3] == 1:
        return True
    else:
        return False


# creates deck, generates chosen cards and displayes them for the user to choose
def printCards():
    deck = createDeck()
    chosenCards = generatePlayCards(deck)
    print(chosenCards[0], chosenCards[1], chosenCards[2], chosenCards[3])
    print(chosenCards[4], chosenCards[5], chosenCards[6], chosenCards[7])
    print(chosenCards[8], chosenCards[9], chosenCards[10], chosenCards[11])
    return chosenCards


# gets players choice and checks if the cards are a SET or not 
def printIsSet(chosenCards):
    print("Choose three cards that make a SET\n")
    playerCards = getCards(chosenCards)
    result = isSET(playerCards)
    if result == True:
        print("\nYES that is a SET\n")
    else:
        print("\nSorry, that is not a SET\n")


# asks user for input on what they want to do next
def printNext():
    print("What would you like to do next?")
    print("F - Find another SET\nD - Deal another set of cards\nQ - Quit")      
    dec = input("==>")
    return dec


# function to calls other functions in program
def main(seedIn):
    random.seed(seedIn)
    # prints out directions for the user
    print("Choose a SET from the following cards.")
    print("A SET consists of three cards where each feature is EITHER the same")
    print("on each card, or different on each card.\n")
    
    # creates deck, generates chosen cards and displayes them for the user to choose
    chosenCards = printCards()
    # gets players choice and checks if the cards are a SET or not
    printIsSet(chosenCards)
    # displays options to user for what they want to do next
    dec = printNext()
    done = 0
    
    # loops through until the user inputs 'Q' to stop
    while done == 0:
        # ends the program 
        if dec == 'Q':
            print(" Game Over - Thanks for Playing...")
            done = 1
            
        # asks the user to enter 3 new cards they believe are a set
        elif dec == 'F':
            # gets players choice and checks if the cards are a SET or not
            printIsSet(chosenCards)
            # asks what the player wants to do next
            dec = printNext()

        # deals a new deck
        elif dec == 'D':
            # creates deck, generates chosen cards and displayes them for the user to choose
            chosenCards = printCards()
            # gets players choice and checks if the cards are a SET or not
            printIsSet(chosenCards)
            # asks what the player wants to do next
            dec = printNext()
                
        # when the user inputs an option besides F, D, or Q
        elif dec != 'F' and dec != 'D' and dec != 'Q':
            dec = input("Bad input, try again ==>")
        
