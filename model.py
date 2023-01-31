db_list = []

# функция считывает из файла 
def read_db(path: str) -> list:
    global db_list
    # открытие файла 
    with open(path, 'r', encoding='UTF-8') as file:
        # создание переменной my_list и сохранение в неё всего, что прочитали в файле
        # readlines() считывает и создает список из строк
        my_list = file.readlines() 
        for line in my_list: 
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)
        return db_list


# функция добавляет новый контакт(словарь) в список контактов 
def add_contact(new_contact: dict) -> list:
    db_list.append(new_contact)
    return db_list


# функция дописывает в файл добавленный контакт
def save_contact(path: str, new_contact: dict):
    contact = ''
    if len(db_list) == 1:
        contact = ';'.join(new_contact.values())
    elif len(db_list) > 1:
        contact = ';'.join(new_contact.values())
        contact = '\n' + contact
    with open(path, 'a', encoding='UTF-8') as data:
        data.write(contact)


# функция перезаписывает измененный список контактов
def save_change_contacts(path: str):
    contact = ''
    if len(db_list) == 1:
        contact = ';'.join(db_list.values())
    elif len(db_list) > 1:
        for i in db_list:
            if i != len(db_list)-1:
                contact = contact + ';'.join(i.values()) + '\n'
            elif i == len(db_list)-1:
                contact = contact + ';'.join(i.values())
    with open(path, 'w', encoding='UTF-8') as data:
        data.write(contact)


# функция удаляет из списка контактов указанный контакт
def delete_contact(contact: dict):
    global db_list
    db_list.remove(contact)
    return db_list
    

# функция поиска указанного пользователем контакта по фамилии
def search_contact(k: str, v):
    global db_list
    d = next((d for d in db_list if d.get(k) == v))
    return d
