#Задание 1
ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}

collection = set()

for value in ids.values():
    for v in value:
        collection.add(v)
print(collection)

#Задание 2
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

list = []

for q in queries:
    count = q.count(' ') + 1
    list.append(count)
    count = 0

for c in list:
    if c==2:
        print('Поисковых запросов, содержащих 2 слов(а):', round(list.count(2)/len(list)*100, 2), '%')
        break
    elif c==3:
        print('Поисковых запросов, содержащих 3 слов(а):', round(list.count(3)/len(list)*100, 2), '%')

#Задание 3
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
for company, info in results.items():
    info['ROI'] = round((info['revenue']/info['cost'] - 1)*100, 2)
print(results)

#Задание 4
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
a = 0
for company, info in stats.items():
    if int(info) > a:
        b = ''
        a = int(info)
        b += company
print('Максимальный объем продаж на рекламном канале:', b)

#Задание 5
my_list = ['a', 'b', 'c', 'd', 'e', 'f']

temp_dict = dict()
pred_step_dict = dict()
for i in range(len(my_list)-1,0,-1):
    if i==len(my_list)-1:
        temp_dict[my_list[i-1]] = my_list[i]
    else:
        temp_dict[my_list[i-1]] = pred_step_dict
    pred_step_dict = temp_dict
    temp_dict = dict()
print(pred_step_dict)

#Задание 6
cook_book = {
  'салат': [
     {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
     {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},   
    ],
  'лимонад': [
     {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},    
    ]
}

temp_list1 = []
temp_list2 = []

n = int(input('Введи кол-во персон '))

for info in cook_book.values():
    for c in info:
        for value in c.values():
            temp_list1.append(value)

for i in range(0, len(temp_list1), 3):
    if temp_list1[i] not in temp_list2:
        temp_list2.append(temp_list1[i])
        temp_list2.append(temp_list1[i+1])
        temp_list2.append(temp_list1[i+2])
    elif temp_list1[i] in temp_list2 and temp_list1[i+2]!=temp_list2[temp_list2.index(temp_list1[i])+2]:
        temp_list2.append(temp_list1[i])
        temp_list2.append(temp_list1[i+1])
        temp_list2.append(temp_list1[i+2])
    else:
        temp_list2[temp_list2.index(temp_list1[i])+1] += temp_list1[i+1]

for i in range(0, len(temp_list2), 3):
    print(temp_list2[i], ': ', n*temp_list2[i+1], ' ', temp_list2[i+2], sep='')

