# from ui import contact_menu
PATH = r'C:\Users\Zox\Desktop\IT Future\5_python\phonebook_python\data.txt'
def menu():
    choise = int(-1)
    while 1 > choise or choise > 3:
        choise = int(input('''Phonebook. Main menu
        1. Search
        2. Create contact
        3. Close Phonebook
        '''))
        main_menu_func(choise)
    menu()
def contact_menu(index):
    choise = int(-1)
    while 1 > choise or choise > 4:
        choise = int(input('''What you want to do?
        1. Call
        2. Edit
        3. Delete
        4. To main menu
        '''))
        contact_func(index,choise)   
def main_menu_func(choise: int):
    if choise == 1:
        return search_func()
    elif choise == 2:
        return create_func()
    return ''
def create_func():
    contact = {}
    contact['first_name'] = input("Input first name: ")
    contact['second_name'] = input("Input second name: ")
    contact['mobile_number'] = input("Input mobile number: ")
    with open (PATH, 'a', encoding="utf-8") as database:
        database.write(str(contact)+"\n")
def search_func():
    with open (PATH, 'r', encoding='utf-8') as database:
        name = input("Input part of name of number: ")
        file = (database.readlines())
        flag = True
        # print("Which contact you want to open?")
        for index, contact_dict in enumerate(file):
            if name.lower() in contact_dict.lower():
                print(index, contact_dict)
                flag = False
        if flag:
            print("We find nothing. Return to main menu. ")
            return menu()
        print("Which contact do you want to open?")
        return contact_card(input())
def contact_card(index: int) ->str:
    with open (PATH, 'r', encoding='utf-8') as database:
        file = (database.readlines())
        print("Contact card.")
        # как обратиться к строке из базы по индексу?
        for i, contact_dict in enumerate(file):
            if int(i)==int(index): #костыли, пришлось добавлять int перед значениями, даже когда они равны
                print('\n'.join(contact_dict.split(', '))) #надо навести красоту, убрать { и "
                return(contact_menu(i)) 
def contact_func(index,choise: int):
    if choise == 1:
        return call_func()
    elif choise == 2:
        return edit_func(index)
    elif choise == 3:
        return delete_func(index)
    else:
        return menu()

def call_func():
    print ('zzzz....zzzz.....zzzz....The phone number is switched off or out of the coverage')
def edit_func(index: int):
    pass
def delete_func(index: int):
    with open (PATH, 'r', encoding='utf-8')as database:
        file = (database.readlines())
        new_base = ([i for i in file if i!=file[index]])
    with open (PATH, 'w', encoding='utf-8')as database:
        database.write("".join(new_base))
    print("Deleting complete. Return to main menu")
    menu()
menu()