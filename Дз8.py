#Задание №1
import pandas as pd

ratings, movies = pd.read_csv('ratings.csv'), pd.read_csv('movies.csv')

joined = ratings.merge(movies, on = 'movieId', how = 'left')[['title', 'rating']]

print(joined[ joined.rating == 5.0 ]['title'].value_counts().head(1))

#Задание №2
import pandas as pd

power = pd.read_csv('power.csv')

print(sum(power[ ((power.country == 'Estonia') | (power.country == 'Lithuania') | (power.country == 'Latvia')) & ((power.category == 4.0) | (power.category == 12.0) | (power.category == 21.0)) & (power.year >= 2005) & (power.year <= 2010) & (power.quantity > 0)]['quantity']))

#Задание №3
import pandas as pd

data = pd.read_html('https://fortrader.org/quotes', encoding='utf-8')[1]

print(data.head())
