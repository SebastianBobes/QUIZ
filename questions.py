import json
def read_file(path = "questions.json"):
    with open(path, 'r') as file:
        x = json.loads(file.read())
        return x

def read_index_and_answers_index(new_list):
    for x in new_list:
        my_list=list(x.keys())
        index = my_list[0]
        nr=len(my_list)-1
        ans_index = my_list[1:nr:1]
        return index,ans_index

def read_questions(my_list):
    my_list = read_file()
    for my_dict in my_list:
        q=list(my_dict.items())[0][1]
        print(q)

def read_answers(my_list):
    new_dict = {}
    for my_dict in my_list:
        a=list(my_dict.items())[0][0]
        new_dict[a]=list(my_dict.items())[1][1],list(my_dict.items())[2][1],list(my_dict.items())[3][1], list(my_dict.items())[4][1]
    print(new_dict)



if __name__ == '__main__':
    my_list = read_file()
    # read_answers(my_list)
    # read_questions(my_list)
    print(read_index_and_answers_index(my_list))
