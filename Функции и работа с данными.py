#Задание №1
import pandas as pd

ratings, movies = pd.read_csv('ratings.csv'), pd.read_csv('movies.csv')

joined = ratings.merge(movies, on = 'movieId', how = 'left')[['title', 'rating']]

def check(rating):
    if rating <= 2:
        return 'низкий рейтинг'
    elif rating <= 4.0 and rating > 2.0:
        return 'средний рейтинг'
    elif rating == 4.5 or rating == 5.0:
        return 'высокий рейтинг'
    
joined['class'] = joined['rating'].apply(check)  #Как сделать через lambda функцию? Не получилось реализовать

#Задание №2
import pandas as pd

geo_data = {

'Центр': ['москва', 'тула', 'ярославль'],

'Северо-Запад': ['петербург', 'псков', 'мурманск'],

'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

def check_geo(keyword):
    flag = False
    for c in keyword.split():
        for key, value in geo_data.items():
            if c.lower() in value:
                return key
                flag = True
                break
    if flag == False:
        return 'undefined' 
keywords = pd.read_csv('keywords.csv')

keywords['region'] = keywords['keyword'].apply(check_geo)

print(keywords.head())

#Задание №3
import pandas as pd

ratings, movies = pd.read_csv('ratings.csv'), pd.read_csv('movies.csv')

joined = ratings.merge(movies, on = 'movieId', how = 'left')[['title', 'rating']]

years = tuple(range(1950, 2011))

def production_year(title):
    flag = True
    for c in years:
        if str(c) in title:
            a = int(c)
            flag = True
            break
        else:
            flag = False
    if flag:
        return a
    else:
        return 1900
            
joined['years'] = joined['title'].apply(production_year)

print(joined.groupby('years').mean().sort_values('rating', ascending=False).reset_index().head())
