PATH = r'C:\Users\Zox\Desktop\IT Future\5_python\phonebook_python\data.txt'
import text, classes

def create_func() ->None:
    first_name = input(text.qn_creating_1)
    second_name = input(text.qn_creating_2)
    phone_number = input(text.qn_creating_3)
    contact = classes.Contact(first_name, second_name, phone_number)
    output_contact(contact)
    with open (PATH, 'a', encoding="utf-8") as database:
        database.write(str(contact)+'\n')
def search_func()->None: 
    while True:
        with open (PATH, 'r', encoding='utf-8') as database:
            name = input(text.search_header)
            file = (database.readlines())
            result = [i[:4] for i in file if name.lower() in i.lower()]
            if len(result)>0:
                for i in result:
                    current_contact = contact_card(int(i))
                    output_contact(current_contact)
                break
        print(text.find_nothing)
def contact_card(index: int) -> classes.Contact:
    with open (PATH, 'r', encoding='utf-8') as database:
        file = (database.readlines())
        for i in file:
            user_id_finded = int(i.split()[0])
            first_name = i.split()[1]
            second_name = i.split()[2]
            phone_number = i.split()[3]
            if index == user_id_finded:
                current_contact = classes.Contact(first_name, second_name, phone_number)
                current_contact.user_id = user_id_finded
                return current_contact
        exit()

def call_func():
    print (text.calling)
def delete_func(index: int):
    with open (PATH, 'r', encoding='utf-8')as database:
        file = (database.readlines())
        new_base = [i for i in file if int(i[:4]) != index]
    with open (PATH, 'w', encoding='utf-8')as database:
        database.write("".join(new_base))
def watch_all():
    with open (PATH, 'r', encoding='utf-8') as database:
        file = (database.readlines())
        for i in file:
            current_contact = contact_card(int(i[:4]))
            output_contact(current_contact)

def edit_func(index: int):
    base_contact = contact_card(index)
    first_name, second_name, phone_number = base_contact.first_name,base_contact.second_name,base_contact.phone_number
    choise = int(input(text.edit_menu))
    if choise == 1:
        first_name = input(text.qn_creating_1)
    elif choise == 2:
        second_name = input(text.qn_creating_2)
    elif choise == 3:
        phone_number = input(text.qn_creating_3)
    contact = classes.Contact(first_name, second_name, phone_number)
    output_contact(contact)
    with open (PATH, 'a', encoding="utf-8") as database:
        database.write(str(contact)+'\n')
    delete_func(index)

def input_contact_menu():
    choise_contact_menu = -1
    while 1 > choise_contact_menu or choise_contact_menu > 4:
        choise_contact_menu = int(input(text.contact_menu))
        return choise_contact_menu

def output_contact(somecontact: classes.Contact):
    print(f'{somecontact.user_id:^8}{somecontact.first_name: ^20}{somecontact.second_name:^20}{somecontact.phone_number:^20}')

def actions_with_contact():
        print(text.qn_contact)
        index = int(input())
        print(text.contact_card_header)
        print(text.table_info)
        current_contact = contact_card(index)
        output_contact(current_contact)
        choise_contact_menu = input_contact_menu()
        if choise_contact_menu == 1:
            call_func()
        elif choise_contact_menu == 2:
            edit_func(index)
            print(text.editing_complete)
        elif choise_contact_menu == 3:
            delete_func(index)
            print(text.deleting_complete)
        else:
            pass

