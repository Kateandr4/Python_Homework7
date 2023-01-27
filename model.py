# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

phon_book = []
path = 'seminar 7/data.txt'

def get_phon_book():
    global phon_book
    return phon_book

def open_file():
    #path = 'seminar 7/data.txt'
    global phon_book
    global path
    with open (path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
   
    for contact in file:
         phon_book.append(contact.strip().split(';'))


def save_file():
    global phon_book
    global path
    pb_str = []
    for contact in phon_book:
        pb_str.append(';'.join(contact))
    # print(pb_str)
    # print('\n'.join(pb_str))
    with open (path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))
   
def add_new_contact(new_contact: list):
    global phon_book
    phon_book.append(new_contact)

def search_contact(find: str):
    global phon_book
    result = []
    for contact in phon_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def delete_contact(del_n: int):
    global phon_book
    for contact in range(len(phon_book)):
            if del_n == contact+1:
                phon_book.pop(contact)
                break
    return phon_book
def count_len():
    global phon_book
    count = len(phon_book)
    return count

def edit_cont(edit_n: int, new_contact :list):
    global phon_book
    phon_book.pop(edit_n-1)
    phon_book.insert(edit_n-1, new_contact)    

    return phon_book
def show_contact(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта') 
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}.{contact[0]}:20 {contact[1]}:13')


