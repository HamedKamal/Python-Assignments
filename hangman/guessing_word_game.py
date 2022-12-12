# import random to choose random word from our lits
import random
# intialize our list 
words = ['hamed', 'computer', 'laptop']
# pick a random word from our list "using our library"
random_word = random.choice(words)
# intialzize our user input 
user_trial = ''
print(random_word)
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
guess_count = 0
# max guess counter 
guess_count_max = 6
# bollean if trials ends
finished = False
# while loop cheaks for 
while len(splited_word) != len(user_right_guess) and not finished:
    if guess_count < guess_count_max:
        user_trial = input('enter the  charcter : ')
        if user_trial in splited_word and user_trial not in user_right_guess:
            for index, item in enumerate(splited_word):
                if user_trial == item:
                    # print(True)

                    user_right_guess.append(user_trial)
                    del dash_list[index]
                    dash_list.insert(index, user_trial)
                    print(dash_list)

        else:
            # user_worng_guess.append(user_trial)
            if user_trial in user_worng_guess or user_trial in user_right_guess:
                print('you used '+user_trial)
                print('you have used ', guess_count, 'trials from 6')
            else:
                user_worng_guess.append(user_trial)
                guess_count += 1
                print('you have used ', guess_count, 'trials from 6')
    else:
        finished = True
