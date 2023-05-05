import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="62d0a5be746a44da9d2c2c54a429979b",
        client_secret="acd98a0894a6485cb50e408afe9d164b",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

#Creates playlist
#playlist = sp.user_playlist_create(user=user_id, name="Billboard100", public=False, collaborative=False, description="Created from python")

user_playlist = sp.user_playlists(user=user_id, limit=50, offset=1)


pp = pprint.PrettyPrinter(indent=4)

#pp.pprint(user_playlist["items"][0])

#pp.pprint(user_playlist["items"])

#user_playlist_add_tracks(user=user_id, playlist_id="1rdXSTJC1VfvwFEDzzCbLY", tracks, position=None)
#tracks = sp.user_playlist_tracks(user=None, playlist_id="1rdXSTJC1VfvwFEDzzCbLY",fields=None, limit=100, offset=0, market=None)
#pp.pprint(tracks)


