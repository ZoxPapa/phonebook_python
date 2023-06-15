import functions1
import text

def start():
    choise = int(-1)
    while 1 > choise or choise > 4:
        choise = int(input(text.main_menu))
        if choise == 1:
            functions1.search_func()
            print(text.qn_contact)
            index = int(input())
            print(text.contact_card_header)
            print(text.table_info)
            functions1.contact_card(index)
            choise_contact_menu = functions1.input_contact_menu()
            if choise_contact_menu == 1:
                functions1.call_func()
            elif choise_contact_menu == 2:
                functions1.edit_func(index)
                print(text.editing_complete)
            elif choise_contact_menu == 3:
                functions1.delete_func(index)
                print(text.deleting_complete)
            else:
                pass
        elif choise == 2:
            functions1.create_func()
            print(text.creating_complete)
        elif choise == 3:
            print(text.watch_all_header)
            print(text.table_info)
            functions1.watch_all()
        if choise == 4:
            break
        start() 
