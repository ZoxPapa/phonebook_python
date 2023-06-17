PATH = r'C:\Users\Zox\Desktop\IT Future\5_python\phonebook_python\data.txt'
import text

def create_func() ->None:
    contact = []
    contact.append(input(text.qn_creating_1))
    contact.append(input(text.qn_creating_2))
    contact.append(input(text.qn_creating_3))
    with open (PATH, 'a', encoding="utf-8") as database:
        database.write(str(contact)+"\n") #надо было джойнить, не было бы барахла рядом со значениями
def search_func()->None: 
    while True:
        with open (PATH, 'r', encoding='utf-8') as database:
            name = input(text.search_header)
            file = (database.readlines())
            flag = True
            for index, contact_row in enumerate(file):
                if name.lower() in contact_row.lower():
                    print(index, '. ', contact_row) #выводит некрасиво, сделать как 27,28 строки + шапка таблицы.
                                                    #!лучше не принтить в теле, а добавлять в словарь(например).и словарь на ретерн
                    flag = False
            if not flag:
                break
        print(text.find_nothing)
def contact_card(index: int) ->None:
    with open (PATH, 'r', encoding='utf-8') as database:
        file = (database.readlines())
        # print(file[index]) 
        for i in file[index].split(', '):
            print(f'{i.strip(): ^20}', end=' ')
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
        for i, j in enumerate(file):
            print(i, ". ", end = '')
            for k in j.split(","):
                print(f'{k: ^20}', end='') #надо стрипануть
            print()

def edit_func(index: int): #это незаконно, научиться вытаскивать конкретный элемент контакта, переделать
    create_func()
    delete_func(index)

def input_contact_menu():
    choise_contact_menu = -1
    while 1 > choise_contact_menu or choise_contact_menu > 4:
        choise_contact_menu = int(input(text.contact_menu))
        return choise_contact_menu