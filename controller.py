import view
import model

# def button_click():
#     value = view.menu()
#     model.init(value)

phon_book = []

def button_click():
    choice = ''
    while choice != 8:
        choice = view.menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_contact(model.get_phon_book())
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                del_n = int(view.del_contact())  # добавить проверку что значение в спписке
                del_result = model.delete_contact(del_n)
                view.show_contact(del_result)             
                view.del_end()
            case 6:
                edit_n = int(view.edit_contact())
                count = model.count_len()
                if count <= edit_n-1 or edit_n == 0:
                    view.edit_error(edit_n)
                else:
                    new_contact = list(view.create_new_contact())
                    model.edit_cont(edit_n, new_contact)
                    view.edit_end()
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contact(result)
            case 8:
                view.exit()
            case _:
                view.input_error()
    