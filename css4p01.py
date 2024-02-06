# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:33:15 2024

@author: 23676469
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv", index_col=0)

"""
Index: 1000 entries, 1 to 1000
Data columns (total 11 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Title               1000 non-null   object 
 1   Genre               1000 non-null   object 
 2   Description         1000 non-null   object 
 3   Director            1000 non-null   object 
 4   Actors              1000 non-null   object 
 5   Year                1000 non-null   int64  
 6   Runtime (Minutes)   1000 non-null   int64  
 7   Rating              1000 non-null   float64
 8   Votes               1000 non-null   int64  
 9   Revenue (Millions)  872 non-null    float64
 10  Metascore           936 non-null    float64
"""

# Replace empty values for Revenue and Metascore with mean values - using fillna method
revMean = df['Revenue (Millions)'].mean().round(2)
df['Revenue (Millions)'].fillna(revMean, inplace=True)

metaMean = df['Metascore'].mean().round(2)
df['Metascore'].fillna(metaMean, inplace=True)

"""
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Title               1000 non-null   object 
 1   Genre               1000 non-null   object 
 2   Description         1000 non-null   object 
 3   Director            1000 non-null   object 
 4   Actors              1000 non-null   object 
 5   Year                1000 non-null   int64  
 6   Runtime (Minutes)   1000 non-null   int64  
 7   Rating              1000 non-null   float64
 8   Votes               1000 non-null   int64  
 9   Revenue (Millions)  1000 non-null   float64
 10  Metascore           1000 non-null   float64
"""

#pd.set_option('display.max_rows', None)

df.drop_duplicates(inplace=True)

# QUESTION 1
max_rating = df["Rating"].max()
max_rating_row = df[df['Rating'] == max_rating]
max_rating_title = max_rating_row['Title'].values[0]
print(max_rating_title)
"""
The Dark Knight
"""
# ANSWER

#QUESTION 2
average_revenue = df['Revenue (Millions)'].mean()
print(average_revenue)
"""
82.95684 ~ 82 956 840
Between 70 and 100 Million
"""
# ANSWER

# QUESTION 3
fltr_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue2 = fltr_df['Revenue (Millions)'].mean()
print(average_revenue2)
"""
68.06492924528301 ~ 68 064 929.25
Between 50 and 80 Million
"""
# ANSWER

# QUESTION 4
num_movies_2016 = len(df[df['Year'] == 2016])
print(num_movies_2016)
"""
297
"""
# ANSWER

# QUESTION 5
num_mov_Christopher = len(df[df['Director'] == 'Christopher Nolan'])
print(num_mov_Christopher)
"""
5
"""
# ANSWER

# QUESTION 6
num_mov_rating8 = len(df[df['Rating'] >= 8.0])
print(num_mov_rating8)
"""
78
"""
# ANSWER

#QUESTION 7
chris_df = df[df['Director'] == 'Christopher Nolan']
median_chris = chris_df['Rating'].median()
print(median_chris)
"""
8.6
"""
# ANSWER

# QUESTION 8
group_year = df.groupby('Year')
mean_year = group_year['Rating'].mean().sort_values(ascending=False)
highest_rated_year = mean_year.index[0]
print(highest_rated_year)
"""
2007
"""
# ANSWER

# QUESTION 9
num_mov_06 = (df['Year'] == 2006).sum()
num_mov_16 = (df['Year'] == 2016).sum()
percentage = ((num_mov_16 - num_mov_06) / num_mov_06) * 100
print(percentage)
"""
575.0
"""
# ANSWER

# QUESTION 10
# splitting the names by comma from actors column
actors_columns = df['Actors'].str.split(',')
# ['Chris Pratt', ' Vin Diesel', ' Bradley Cooper', ' Zoe Saldana']

arrActors = []
# remove each actor from index array and populate into a single array index
for i in actors_columns:
    arrActors.extend(i)


# using a dictionary as storage to count the number of occurences
actors_count = {}
# loop through each index in array actors
for actor in arrActors: # remove white spaces using strip
    stripped = actor.strip()
    loop_count = actors_count.get(stripped, 0)
    actors_count[stripped] = loop_count + 1

most_common_actor = max(actors_count, key=actors_count.get)
print(most_common_actor)
"""
Mark Wahlberg
"""
# ANSWER

# QUESTION 11
genres = df['Genre'].str.split(',')

arrGenres = []
for i in genres:
    arrGenres.extend(i)

unique = {}
# loop through list and add to dictionary
for word in arrGenres:
    unique[word] = unique.get(word, 0) + 1
# if first occurence add 1, otherwise increment
# lastly, find the length of the dictionary
unique_genres = len(unique)
print(unique_genres)
"""
20
"""
# ANSWER

# QUESTION 12

import matplotlib.pyplot as plt
import seaborn as sns

# Working only with numerical columns for correlation analysis
numerical_columns = ['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', "Metascore"]
num_df = df[numerical_columns]

cor_matrix = num_df.corr()

plt.figure(figsize=(12,10))
sns.heatmap(cor_matrix, annot=True, cmap='coolwarm', fmt='0.2f')
plt.title("Correlation Matric of Num Values")
plt.show()

# END

#print(df)
#print(df.info())
#print(df.describe())











































