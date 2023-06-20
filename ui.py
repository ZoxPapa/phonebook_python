import functions1
import text

def start():
    while True:
        choise = -1
        while 1 > choise or choise > 4:
            choise = int(input(text.main_menu))
            if choise == 1:
                print(text.watch_all_header)
                print(text.table_info)
                functions1.search_func()
                functions1.actions_with_contact()
            elif choise == 2:
                functions1.create_func()
                print(text.creating_complete)
            elif choise == 3:
                print(text.watch_all_header)
                print(text.table_info)
                functions1.watch_all()
                functions1.actions_with_contact()
            if choise == 4:
                exit()
