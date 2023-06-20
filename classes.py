from functions1 import PATH 

class Contact:
    def __init__(self, first_name, second_name, phone_number) -> None:
        with open (PATH, 'r', encoding='utf-8') as database:
            file = (database.readlines())
            last_index = int(file[-1][:4])
        self.user_id: int = last_index+1
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f'{self.user_id :0>4} {self.first_name} {self.second_name} {self.phone_number}'