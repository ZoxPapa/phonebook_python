PATH = r'C:\Users\Zox\Desktop\IT Future\5_python\phonebook_python\data.txt'
import text
def create_func():
    contact = []
    contact.append(input(text.qn_creating_1))
    contact.append(input(text.qn_creating_2))
    contact.append(input(text.qn_creating_3))
    with open (PATH, 'a', encoding="utf-8") as database:
        database.write(str(contact)+"\n")
def search_func()->None:
    with open (PATH, 'r', encoding='utf-8') as database:
        name = input(text.search_header)
        file = (database.readlines())
        flag = True
        for index, contact_row in enumerate(file):
            if name.lower() in contact_row.lower():
                print(index, '. ', contact_row)
                flag = False
        if flag:
            print(text.find_nothing)
            return search_func()
def contact_card(index: int) ->None:
    with open (PATH, 'r', encoding='utf-8') as database:
        file = (database.readlines())
        # print(file[index]) 
        for i in file[index].split(', '):
            print(f'{i.strip(): ^20}', end=' ') #strip не работает
        print()

def call_func():
    print (text.calling)
def delete_func(index: int):
    with open (PATH, 'r', encoding='utf-8')as database:
        file = (database.readlines())
        new_base = ([i for i in file if i!=file[index]])
    with open (PATH, 'w', encoding='utf-8')as database:
        database.write("".join(new_base))
def watch_all():
    with open (PATH, 'r', encoding='utf-8') as database:
        file = (database.readlines())
        # for i, j in enumerate(file):
        #     print(i, '. ', j)
        for i, j in enumerate(file):
            print(i, ". ", end = '')
            for k in j.split(","):
                print(f'{k: ^20}', end='') #надо стрипануть
            print() #попробуй закомментить и распечатать


def edit_func(index: int):
    create_func()
    delete_func(index)

def input_contact_menu():
    choise_contact_menu = int(-1)
    while 1 > choise_contact_menu or choise_contact_menu > 4:
        choise_contact_menu = int(input(text.contact_menu))
        return choise_contact_menu