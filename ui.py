def menu():
    choise = int(-1)
    while 1 > choise or choise > 3:
        choise = int(input('''Phonebook. Main menu
        1. Search
        2. Create contact
        3. Close Phonebook
        '''))
        main_menu(choise)
menu()

def contact_menu():
    choise = int(-1)
    while 1 > choise or choise > 3:
        choise = int(input('''What you want to do?
        1. Call
        2. Edit
        3. Delete
        '''))
        contact_func(choise)    

# search_menu = input('''Search
# Please input name:
# ''')

# print(search_menu)
# print(main_menu)