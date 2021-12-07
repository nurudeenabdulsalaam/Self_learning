print("Note: You only have 3 trials")
secret_word = input("Enter your secret word: ")
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and out_of_guesses == False:
    if guess_count < guess_limit:
        guess = input("ENTER GUESS: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("YOU LOSE, YOU CAN DO BETTER!")
    #up = 2
    print("new trail?")
    print("type 1 for yes and 0 for no")
    down = int(input("Your chioce: "))
    if down == 1:
        print("new trial starts")
        print("Note: You only have 3 trials")
        secret_word = input("Enter your secret word: ")
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False

        while guess != secret_word and out_of_guesses == False:
            if guess_count < guess_limit:
                guess = input("ENTER GUESS: ")
                guess_count += 1
            else:
                out_of_guesses = True

    else:
        print("thanks!")
        
    '''
    try:
        print(chioce)
    except ZeroDivisionError:
        print("next time")
        '''
else:
    print("YOU WIN, PUT MORE EFFORT")


# this is where i began my try and error
'''
def new_trial(new):
    #new_trial(input("Your choice: "))
    for letter in new:
        if new in "Yes" or "yes":
            guess = ""
            guess_count = 0
            guess_limit = 3
            out_of_guesses = False
            while guess != secret_word and out_of_guesses == False:
                if guess_count < guess_limit:
                    guess = input("ENTER GUESS: ")
                    guess_count += 1
                else:
                    out_of_guesses = True
        elif new in "No" or "no":
            print("try again next time")
        else:
            print("invalid input")

    if out_of_guesses:
        print("YOU WIN, keep it up!")
    else:
        '''
#print("YOU LOSE, YOU CAN DO BETTER!")
       