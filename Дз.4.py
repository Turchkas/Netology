documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def function_p():
    b = input("Введите номер документа: ")
    for c in documents:
        if c.get('number') == b:
            d = c.get('name')
            break
        else:
            d = 'Документ не найден в базе'
    return print(d)
            
def function_s():
    b = input("Введите номер документа: ")
    for key, values in directories.items():
        flag = True
        if b in values:
            print('Документ хранится на полке:', key)
            break
        else:
            flag = False
    if flag == False:
        print('Документ не найден в базе')

def function_l():
    for c in documents:
        for key, values in directories.items():
            if c.get('number') in values:
                print('№: ',c.get('number'), ', ', 'тип: ', c.get('type'), ', ' ,'владелец: ', c.get('name'), ', ',  'полка хранения: ', key, sep = '')
                       
def function_ads():
    b = input("Введите номер документа полки: ")
    if b in directories.key():
        print('Такая полка уже существует. Текущий перечень полок: ', ', '.join(list(directories.key())))
    else:
        directories[b] = []
        print('Полка добавлена. Текущий перечень полок: ', ', '.join(list(directories.key())))

def function_ds():
    b = input("Введите номер полки: ")
    if b in directories and directories[b] == []:
        directories.pop(b)
        print('Полка удалена. Текущий перечень полок:', ', '.join(list(directories.key())))
    elif b in directories and directories[b] != []:
        print('На полке есть документа, удалите их перед удалением полки. Текущий перечень полок:', ', '.join(list(directories.key())))
    else:
        print('Такой полки не существует. Текущий перечень полок:', ', '.join(list(directories.key())))
 
def function_ad():
    b = input("Введите номер документа: ")
    c = input("Введите тип документа: ")
    d = input("Введите владельца документа: ")
    e = input("Введите полку для хранения: ")
    documents.append({'type': c, 'number': b, 'name': d})
    if e in directories.key():
        print('Документ добавлен. Текущий список документов: ')
        directories[e] += [b]
        for doc in documents:
            for key, values in directories.items():
                if doc.get('number') in values:
                    print('№: ',doc.get('number'), ', ', 'тип: ', doc.get('type'), ', ' ,'владелец: ', doc.get('name'), ', ',  'полка хранения: ', key, sep = '')
    else:
        print('Такой полки не существует. Добавьте полку командой as.')
        print('Текущий список документов:')
        for doc in documents:
            for key, values in directories.items():
                if doc.get('number') in values:
                    print('№: ',doc.get('number'), ', ', 'тип: ', doc.get('type'), ', ' ,'владелец: ', doc.get('name'), ', ',  'полка хранения: ', key, sep = '')

def function_d():
    b = input("Введите номер документа: ")
    for i in range(len(documents)):
        if b in documents[i].values():
            flag = True
            documents.pop(i)
            break
        else:
            flag = False
    if flag == False:
        print('Документ не найден в базе. Текущий список документов:')
        for doc in documents:
            for key, values in directories.items():
                if doc.get('number') in values:
                    print('№: ',doc.get('number'), ', ', 'тип: ', doc.get('type'), ', ' ,'владелец: ', doc.get('name'), ', ',  'полка хранения: ', key, sep = '')
    else:
        print('Документ удалён. Текущий список документов:')
        for doc in documents:
            for key, values in directories.items():
                if doc.get('number') in values:
                    print('№: ',doc.get('number'), ', ', 'тип: ', doc.get('type'), ', ' ,'владелец: ', doc.get('name'), ', ',  'полка хранения: ', key, sep = '')

def function_m():
    cur_d = None
    b = input('Введите номер документа: ')
    d = input('Введите номер полки: ')
    for key, values in directories.items():
        if b in values:
            cur_d = key
            break
    if cur_d is None:
        print('Документ не найден. Текущий список документов: ')
    else:
        if d == cur_d:
            print('Документ уже содержится на данной полке. Текущий список документов: ')
        else:
            directories[cur_d].remove(b)
            directories[d].append(b)
            print('Документ перемещён. Текущий список документов: ')
    for doc in documents:
        for key, values in directories.items():
            if doc.get('number') in values:
                print('№: ',doc.get('number'), ', ', 'тип: ', doc.get('type'), ', ' ,'владелец: ', doc.get('name'), ', ',  'полка хранения: ', key, sep = '')

def main():
    a = ''
    while a != 'q':
        a = input('Введите нужную команду: ')
        if a == 'p':
            function_p()
        elif a == 'l':
            function_l()
        elif a == 'p':
            function_p()
        elif a == 'ad':
            function_ad()
        elif a == 's':
            function_s()
        elif a == 'ds':
            function_ds()
        elif a == 'ads':
            function_ads()
        elif a == 'd':
            function_d()
        elif a == 'm':
            function_m()
        elif a == 'q':
            break
        else:
            print('Нет такой команды')

main()
