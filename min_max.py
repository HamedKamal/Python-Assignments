# user guees a number from 1 to 10
# import random module to choose a random number from 1 to 10
import random
# initialize our random choise with the function that returns a integer from 0 to the number givien
computer_choise = random.randrange(10)
# initialize user trials
user_trials = 0
# initialize user maximum trials
max_trials = 6
# bollean if user guessed right
guessed_right = False
# loop if user dose n't consumed his trials and not gueeed right 
while user_trials != max_trials and not guessed_right:
    # input 
    user_guess = int(input('enter a number from 1 to 10 : '))
    # if user guessed right 
    if user_guess == computer_choise:
        # true value "to exit the loop"
        guessed_right = True
    # if user has a close value
    elif user_guess+1 == computer_choise or user_guess+2 == computer_choise or user_guess-1 == computer_choise or user_guess-2 == computer_choise:
        user_trials += 1
        print(
            f"too close !!!                                 {user_trials}/{max_trials}")
    # if user has a high guess
    elif user_guess > computer_choise:
        user_trials += 1
        print(
            f"too high !!!                                 {user_trials}/{max_trials}")
    # if user has a low guess
    elif user_guess < computer_choise:
        user_trials += 1
        print(
            f"too low !!!                                 {user_trials}/{max_trials}")
# print if he win or not 
if guessed_right:
    print(f'right guess {computer_choise}')
else:
    print('you lose ')
