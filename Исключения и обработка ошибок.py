#1 задание
from datetime import datetime as dt

dt.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
dt.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
dt.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')

#2 задание
def correct(arg_list):
    i = -1
    while i != len(arg_list) - 1:
        i += 1
        try:
            dt.strptime(arg_list[i], '%Y-%m-%d')
            print(f"{arg_list[i]} - True")
        except:
            print(f"{arg_list[i]} - False")
stream = ['2018-04-02', '2018-02-29', '2018-19-02']
correct(stream)

#3 задание
from datetime import timedelta
def date_range(start_date_dt, end_date_dt):
    try:
        start_date_dt, end_date_dt = dt.strptime(start_date_dt, '%Y-%m-%d'), dt.strptime(end_date_dt, '%Y-%m-%d')
        if end_date_dt < start_date_dt:
            print([])
        else:
            my_list = []
            current_date = start_date_dt
            while current_date <= end_date_dt:
                my_list.append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta (days = 1)
            print(my_list)
    except:
        print([])

start_dt = '2023-04-01'
end_dt = '2023-05-05'

date_range(start_dt, end_dt)

#4 задание
"""1) list index out of range - обращаемся к несуществующему индексу списка. 
2) Был список длиной 3. Вызываем первый раз функцию: удалили элемент, стал список длиной два, элемнты в этом списке имеют индексы 0 и 1, обращаемся к элементу (A101) по первому индексу - всё ок.
Вызываем функцию второй раз: снова удаляем элемент - длина списка стала равна 1, и единственный оставшийся элемент этого списка имеет индекс 0, а мы пытаемся обратиться к списку по индексу 1, поэтому падает с ошибкой"""