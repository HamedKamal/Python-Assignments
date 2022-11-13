def plus(x,y):
    print(x+y)

def minus(x,y):
    print(x-y)

def times(x,y):
    print(x*y)

def devide(x,y):
    print(x/y)
while True:
    first_number=int(input('Enter the First Number '))
    secound_number=int(input('Enter the Secound Number '))
    operation=input('Enter Your Opreator \n+ - * /\n')
    if operation=='+':
        plus(first_number,secound_number)
    elif operation =='-':
        minus(first_number,secound_number)
    elif operation =='*':
        times(first_number,secound_number)
    elif operation =='/':
        devide(first_number,secound_number)
    else:print('please choose an opreator')    
    again=input('do you want to use the calculator agin ? \n"yes" or "no" : ')
    if again=='no':
        break