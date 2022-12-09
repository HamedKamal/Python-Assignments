user_input = input("enter your exppresion : ")

splitted_text_list = user_input.split()

while len(splitted_text_list) != 1:
    
    for index, item in enumerate(splitted_text_list):
        # print(index,' ',item)
        if ('/' in splitted_text_list or '*' in splitted_text_list):
            if item == '*':
                value = float(
                    splitted_text_list[index-1]) * float(splitted_text_list[index+1])
                print(value)
                del splitted_text_list[index+1]
                del splitted_text_list[index]
                del splitted_text_list[index-1]
                splitted_text_list.insert(index-1, value)
                print(splitted_text_list)
                break
            elif item == '/':
                value = float(
                    splitted_text_list[index-1]) / float(splitted_text_list[index+1])
                print(value)
                del splitted_text_list[index+1]
                del splitted_text_list[index]
                del splitted_text_list[index-1]
                splitted_text_list.insert(index-1, value)
                print(splitted_text_list)
                break

        else:

            if item == '+':
                value = float(
                    splitted_text_list[index-1]) + float(splitted_text_list[index+1])
                print(value)
                del splitted_text_list[index+1]
                del splitted_text_list[index]
                del splitted_text_list[index-1]
                splitted_text_list.insert(index-1, value)
                print(splitted_text_list)
                break
            elif item == '-':
                value = float(
                    splitted_text_list[index-1]) - float(splitted_text_list[index+1])
                print(value)
                del splitted_text_list[index+1]
                del splitted_text_list[index]
                del splitted_text_list[index-1]
                splitted_text_list.insert(index-1, value)
                print(splitted_text_list)
                break
