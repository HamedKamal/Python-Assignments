x = int(input('Enter The Kilos '))
def possible_values(y):
    a=0
    while(a<=y):
        a+=2
        y-=2
        print(str(a)+'  and  '+str(y))
if x%2==0 and x!=2:
    possible_values(x)
    print('yes')
    
else:
    print('no')


