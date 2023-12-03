import requests
from bs4 import BeautifulSoup
from base64 import b64encode

BILLBOARD_ENDPOPINT ="https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID =
SPOTIFY_CLIENT_SECRET_KEY =
AUTH_URL = "https://accounts.spotify.com/api/token"
PLAYLIST_CREATE_URL = "https://api.spotify.com/v1/users/mirzan/playlists"
USER_ID ="mirzan"
#
# date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD :")
# response = requests.get(f"{BILLBOARD_ENDPOPINT}{date}/")
# data = response.text
# soup = BeautifulSoup(data,"html.parser")
# songs = soup.find_all(name='h3', class_="c-title")
# # print(songs)
# songs_list = []
# for song in songs:
#     song_name = song.get_text().strip()
#     songs_list.append(song_name)

# credentials = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET_KEY}"
# base64_credentials = b64encode(credentials.encode()).decode('utf-8')
#
# auth_headers = {
#     'Authorization': f'Basic {base64_credentials}',
# }
# auth_data = {
#     'grant_type': 'client_credentials',
# }

parameters = {

}
auth_response = requests.post(AUTH_URL, headers=auth_headers, data=auth_data)
auth_data = auth_response.json()
access_token = auth_data['access_token']
echo = {
    "name": f"{"22"} top 100",
    "description": f"New playlist for the date {"22"}",
    "public": "false"
}
playlist_create_headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.post(url=f"https://api.spotify.com/v1/users/{SPOTIFY_CLIENT_ID}/playlists", headers=playlist_create_headers, json=echo)
print(response.text)
