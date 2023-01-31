import model
import view

# обработчик пользовательского ввода
def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_db('database.txt')
            view.db_success(model.db_list)
        case 3:
            new_contact = view.create_contact()
            model.add_contact(new_contact)
            model.save_contact('database.txt', new_contact)
        case 5:
            model.delete_contact(model.search_contact('lastname', view.delt_contact()))
            view.show_all(model.db_list)
            model.save_change_contacts('database.txt')
        case 7:
            view.exit_program()    
            
              
        

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
