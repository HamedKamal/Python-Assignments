import random
words = ['hamed', 'computer', 'laptop']
random_word = random.choice(words)
user_trial = ''
print(random_word)
# print('guess'+len(random_word)*' _ ')
dash_list = list(len(random_word)*'_')
print(dash_list)
splited_word = list(random_word)
user_right_guess = []
user_worng_guess = []

guess_count = 0
guess_count_max = 6
finished = False
# user_trial = input('enter the  charcter : ')

# if user_trial in random_word:
#         print('true')
while len(splited_word) != len(user_right_guess) and not finished:
    if guess_count<guess_count_max : 
        user_trial = input('enter the  charcter : ')
        if user_trial in splited_word:
            for index, item in enumerate(splited_word):
                if user_trial == item:
                    # print(True)
                    user_right_guess.append(user_trial)
                    del dash_list[index]
                    dash_list.insert(index, user_trial)
                    print(dash_list)
            
        else:
            guess_count+=1
            
            print(guess_count)
    else:
        finished = True


        