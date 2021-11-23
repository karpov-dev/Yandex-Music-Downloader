from yandex_music import Client
from Songs import Songs
from Config import TOKEN, ROOT_PATH

client = Client.from_token(TOKEN)

songs = Songs(client.users_likes_tracks())
songs.download()