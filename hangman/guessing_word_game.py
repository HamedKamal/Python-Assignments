# import random to choose random word from our lits
import random
# intialize our list
words = ['hamed', 'computer', 'laptop']
# pick a random word from our list "using our library"
random_word = random.choice(words)
# intialzize our user input
user_trial = ''
# print(random_word)
# intialize our dashes list
dash_list = list(len(random_word)*'_')
print(dash_list)
# split our word and return it in a list
splited_word = list(random_word)
# store user right guess
user_right_guess = []
# store user wrong guess
user_worng_guess = []
# guess counter
guess_wrong_count = 0
# max guess counter
guess_count_max = 6
# bollean if trials ends
finished = False
# while loop cheaks for if the user guess right or finished his trials
while len(splited_word) != len(user_right_guess) and not finished:
    # cheak if the user does not reach his trials
    if guess_wrong_count < guess_count_max:
        # take the character from user
        user_trial = input('enter the  charcter : ')
        # cheak the user entered character in our random word 'seacrch in our splitted word ' => list
        # and cheak that the user entered character not entered as a right guess before
        if user_trial in splited_word and user_trial not in user_right_guess:
            # use the for loop and enumerate to identifiy the index and character that user choose
            for index, item in enumerate(splited_word):
                # to know which character is in the splited word
                if user_trial == item:
                    # add the right user's guess in a the right guess list 'to tell him he used it or not'
                    user_right_guess.append(user_trial)
                    # delete the dash 'using the index that enumerate gived us'
                    del dash_list[index]
                    # replace the dash with the right guess with inserting it in the dashed list
                    dash_list.insert(index, user_trial)
                    print(user_trial,'✔')
                    # show the user what he gueesed
                    print(dash_list)
        # if the user guees wrong character
        else:
            # cheak if  the charcter used before or not
            if user_trial in user_worng_guess or user_trial in user_right_guess:
                # show the user the used character
                print('you used '+user_trial)
                # show the user the number of used trials
                print('you have used ', guess_wrong_count,'trials from ', guess_count_max)
            # if user guesses wrong
            else:
                print(user_trial,'✖')

                # add the wrong guess to our list 'to tell him that he used it '
                user_worng_guess.append(user_trial)
                # add 1 to the user wrong guess count
                guess_wrong_count += 1
                # show the user how many trials left for his deth 💀
                print('you have used ', guess_wrong_count,'trials from ', guess_count_max)
    # if user wrong count reached the max 
    else:
        # the finished boolean has true value => exit the loop 
        finished = True
# massege for the player 
if len(user_right_guess)==len(splited_word):
    print('You Win 😎')
else :
    print('You Lose 😥')
# github https://github.com/HamedKamal