import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data, 'html.parser')
movies = soup.find_all(name='h3')
all_movies = []
for movie in movies:
    all_movies.append(movie.get_text())
reversed_movie_list = all_movies[::-1]
print(reversed_movie_list)
with open("top_100_movies.txt",'w') as cinema:
    for movie in reversed_movie_list:
        cinema.write(f"{movie}\n")



