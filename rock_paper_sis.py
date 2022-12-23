import random
# computer list of choises
computerChoises = ['r', 'p', 's']
# score of the computer 
computerScore = 0
# score of the user 
userScore = 0
# turns
turns = 0
# increase the scores and turn function
def increase(isComputer):
    # make the variables global "as it gives me that eror UnboundLocalError: local variable 'computerScore' referenced before assignment ''
    # stackoverflow 
    #https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
    global computerScore
    global userScore
    global turns
    if isComputer:
        computerScore += 1
    else:
        userScore += 1
    turns += 1
while turns != 3:
    print('--------------------------------------------')
    userTurn = input('play "r" , "p" , "s" ').lower
    computerTurn = random.choice(computerChoises)
    # print (computerTurn)
    if userTurn != computerTurn:
        if computerTurn == 'r' and userTurn == 's':
            increase(True)
        elif computerTurn == 'r' and userTurn == 'p':
            increase(False)
        elif computerTurn == 's' and userTurn == 'p':
            increase(True)
        elif computerTurn == 's' and userTurn == 'r':
            increase(False)
            increase(True)
        elif computerTurn == 'p' and userTurn == 's':
            increase(False)
    elif userTurn == computerTurn:
        print('you played like the computer')
    else:
        print('please enter one character "r" , "p" , "s" ')
    print(
        f"your score {userScore} , computer score {computerScore}                   {turns}/3 ")
if userScore>computerScore:
    print('you win 😎')
else :
    print ('you lose 😥')