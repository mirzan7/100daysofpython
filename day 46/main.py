import requests
from bs4 import BeautifulSoup

BILLBOARD_ENDPOPINT ="https://www.billboard.com/charts/hot-100/"

date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD :")
response = requests.get(f"{BILLBOARD_ENDPOPINT}{date}/")
data = response.text
soup = BeautifulSoup(data,"html.parser")
songs = soup.find_all(name='h3', class_="c-title")
# print(songs)
songs_list = []
for song in songs:
    song_name = song.get_text().strip()
    print(song_name)
    songs_list.append(song_name)
print(songs_list)

