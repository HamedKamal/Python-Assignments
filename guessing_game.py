original='hamed'
guess=''
guess_count=0
guess_count_max=3
finished=False
while original != guess and not finished :
    if guess_count<guess_count_max:
        guess = input ('enter your gussing : ')
        guess_count+=1
    else:
        finished = True

if finished :
    print('you lose ')

else :
    print('you win ')