user_input = input("enter your exppresion : ")

splitted_text_list = user_input.split()

while len(splitted_text_list) != 1:
    for index, item in enumerate(splitted_text_list):
        # print(index,' ',item)
        
        if item == '*' :
                times_index=index
                value = int(splitted_text_list[index-1]) * int(splitted_text_list[index+1])
                print(value)
                del splitted_text_list[index+1]
                del splitted_text_list[index]
                del splitted_text_list[index-1]
                splitted_text_list.insert(index-1, value)
                print(splitted_text_list)
        elif item == '/'and index==1:
                value = int(splitted_text_list[index-1]) / int(splitted_text_list[index+1])
                print(value)
                del splitted_text_list[index+1]
                del splitted_text_list[index]
                del splitted_text_list[index-1]
                splitted_text_list.insert(index-1, value)
                print(splitted_text_list)
        # if item == '+'and index==1:
        #         value = int(splitted_text_list[index-1]) / int(splitted_text_list[index+1])
        #         print(value)
        #         del splitted_text_list[index+1]
        #         del splitted_text_list[index]
        #         del splitted_text_list[index-1]
        #         splitted_text_list.insert(index-1, value)
        #         print(splitted_text_list)