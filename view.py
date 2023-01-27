# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы
phon_book = []
commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт', 
            'Выход из программы']
def menu():
    print ('Главное меню:')
    for i, item in enumerate(commands, 1):
        print (f'\t{i}. {item}')
    choice = int(input('Выберете пунки меню: '))
    return choice
#menu()

def show_contact(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта') 
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()


def input_error():
    print()
    print("Ошибка ввода, введите коррентый пункт меню")

def exit():
    print()
    print("Работа с телефонной книгой закончена")
    print()

def create_new_contact():
    name = input('Введите имя и фамилию:')
    phone = input('Введите телефон:')
    comment = input('Введите коментарий:')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def del_contact():
    del_n = int(input('Введите номер строки для удаления: '))
    return del_n

def del_end():
    print()
    print("Запись удалена")    

def edit_contact():
    edit_n = int(input('Введите номер строки для изменения: '))
    return edit_n

def edit_end():
    print()
    print("Запись изменена")
    print()


def edit_error(edit_n: int):
    print()
    print("Номера записи не существует")
    print()