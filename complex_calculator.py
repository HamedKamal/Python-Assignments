print('enter your expression like this 5 * 9 - 8 / 7')
user_input = input("Calculate : ")

splitted_text_list = user_input.split()


# recommend uncomment print functions
def times(index):
    value = float(
        splitted_text_list[index-1]) * float(splitted_text_list[index+1])
    # print(value)
    del splitted_text_list[index+1]
    del splitted_text_list[index]
    del splitted_text_list[index-1]
    splitted_text_list.insert(index-1, value)
    # print(splitted_text_list)

def devide(index):
    value = float(
        splitted_text_list[index-1]) / float(splitted_text_list[index+1])
    # print(value)
    del splitted_text_list[index+1]
    del splitted_text_list[index]
    del splitted_text_list[index-1]
    splitted_text_list.insert(index-1, value)
    # print(splitted_text_list)


def plus(index):
    value = float(
        splitted_text_list[index-1]) + float(splitted_text_list[index+1])
    # print(value)
    del splitted_text_list[index+1]
    del splitted_text_list[index]
    del splitted_text_list[index-1]
    splitted_text_list.insert(index-1, value)
    # print(splitted_text_list)


def minus(index):
    value = float(
        splitted_text_list[index-1]) - float(splitted_text_list[index+1])
    # print(value)
    del splitted_text_list[index+1]
    del splitted_text_list[index]
    del splitted_text_list[index-1]
    splitted_text_list.insert(index-1, value)
    # print(splitted_text_list)


while len(splitted_text_list) != 1:

    for index, item in enumerate(splitted_text_list):
        # print(index,' ',item)
        if ('/' in splitted_text_list or '*' in splitted_text_list):
            if item == '*':
                times(index)
                break
            elif item == '/':
                devide(index)
                break
        else:
            if item == '+':
                plus(index)
                break
            elif item == '-':
                minus(index)
                break
print('Your answer is ', splitted_text_list)
# after 2 hours i did it 🎉
