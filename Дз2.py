#Задание 1
word = 'test'
if len(word)%2==0:
    print(word[len(word)//2-1] + word[len(word)//2])
else:
    print(word[len(word)//2])

#Задание 2
n = int(input())
summa = 0
while n!=0:
    summa += n
    n = int(input())
print(summa)

#Задание 3
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()
if len(boys)==len(girls):
    pair = list(zip(boys, girls))
    print('Идеальные пары:')
    for a in pair:
        a = str(a)
        a = a.replace('(', '')
        a = a.replace(')', '')
        a = a.replace("'", '')
        a = a.replace(',', '')
        a = a.replace(' ', ' и ')
        print(a)
else:
    print('Внимание, кто-то может остаться без пары!')

#Задание 4
countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
print('Средняя температура в странах:')
for i in countries_temperature:
    print(i[0], '-', round((sum(i[1])/len(i[1])-32)/1.8, 1), 'C')

#Задание 5
numbers = '0123456789'
letters = 'АВЕКМНОРСТXУ'
car_ids = ['А222ВС96', 'АБ22ВВ193']
for i in car_ids:
    if len(i)==8 and i[0] in letters and i[1] in numbers and i[2] in numbers and i[3] in numbers and i[4] in letters and i[5] in letters and i[6] in numbers and i[7] in numbers:
        print('Номер', i, 'валиден. Регион: ', i[-2]+i[-1])
    elif len(i)==9 and i[0] in letters and i[1] in numbers and i[2] in numbers and i[3] in numbers and i[4] in letters and i[5] in letters and i[6] in numbers and i[7] in numbers and i[8] in numbers:
        print('Номер', i, 'валиден. Регион: ', i[-3] + i[-2]+i[-1])
    else:
        print('Номер', i, 'не валиден')

#Задание 6
stream = [
    'user100,2022-01-01;150',
    'user99,2022-01-07;205',
    'user1001,2022-03-29;81'
]
count_users = 0
summa = 0
users = ''
list_split = []
list_users = []
list_summa = []

for c in stream:
    b = c.split(',')
    list_split.append(b)

for c in list_split:
    list_users.append(c[0])

for c in list_split:
    c[1] = c[1][c[1].find(';')+1: len(c[1])+1]
    list_summa.append(c[1])

for c in list(zip(list_users, list_summa)):
    if c[0] not in users:
        users += c[0]
        count_users += 1
        summa += int(c[1])
print('Среднее количество просмотров на уникального пользователя:', round(summa/count_users, 2))