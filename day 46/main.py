import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from base64 import b64encode

BILLBOARD_ENDPOPINT ="https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET_KEY = ""
AUTH_URL = "https://accounts.spotify.com/api/token"
PLAYLIST_CREATE_URL = "https://api.spotify.com/v1/users/mirzan/playlists"
USER_ID ="mirzan"

date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD :")
response = requests.get(f"{BILLBOARD_ENDPOPINT}{date}/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
song_names = soup.select("li ul li h3")
songs_name_list = [song.getText().strip() for song in song_names]
print(songs_name_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET_KEY,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in songs_name_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. skipped.")

print(song_uris)

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} top 100 songs",
    public=True,
)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

