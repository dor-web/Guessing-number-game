import random



def start_game():
    #Variables that are used in the program
    number = random.randint(1, 10)
    guess = 0
    attemps = 1
    games_play = 0
    high_score_guess = 0
    
    #introduction to the game
    print("Welcome to the guessing number game")
    name = input("Please enter your name: ")
    print("Welcome, {}".format(name),"!\n")
    
    #The game may begin or player can exit the game
    answer = input("Would you like to play? \n(Y)es/(N)o \t\n")
    
    while answer.lower() == 'y':
        if high_score_guess == 1:
            print("The current high score is: ",high_score_guess)
        elif high_score_guess == 2:
            print("The current high score is: ",high_score_guess)
        elif high_score_guess == 3:
            print("The current high score is: ",high_score_guess)
        elif high_score_guess == 0:
            print("Try to get score that is 3 or less")
            print("The current high score is, ", high_score_guess)
        else:
            print("Try to get score that is 3 or less")
            print("The current score is, ", high_score_guess, "\n")       

        while guess != number:
            try:
            #check to make sure the user inputs the correct number in range
                guess = int(input("Guess a number between 1 to 10: "))
            #checks to see if the user inputs the correct number that has been generated
            except ValueError:
                print("Please enter a numerical value.")
                attemps += 1
            else:
                if guess < 0:
                    print("please another number that falls between 1 to 10.")
                    attemps += 1
                elif guess > 11:
                    print("please another number that falls between 1 to 10.")
                    attemps += 1
                elif guess > number:
                    print("It's lower!")
                    attemps += 1
                elif guess < number:
                    print("It's higher!")

                    attemps += 1

        print("Got it!\n")
        print("The number is: ", number)
        print("It took you",attemps,"to get the right number! GOOD JOB!\n")
        games_play += 1
        if games_play == 1:
            high_score_guess = attemps
        elif attemps < high_score_guess:
            high_score_guess = attemps

        answer = input("Would you like to play? \n(Y)es/(N)o ")     #ask user if they want to play again
        number = random.randint(1, 10)                              #picks a new random number
        attemps = 1                                                 #rest the counter to 1
    return

if __name__ == '__main__':
    start_game()
    print("Thanks for playing!")

    
    
    
