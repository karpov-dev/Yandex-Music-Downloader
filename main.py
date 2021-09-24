from yandex_music import Client
from Songs import Songs
from Folder import rename_with_count


LOGIN = 'passangerfeat@yandex.ru'
PASSWORD = '2015883Vova'
TOKEN = 'AQAAAAAbiKy6AAG8XgDQ_GkBHkslv2kjIdRJUgU'
PATH = "E:\\"

client = Client.from_token('AQAAAAAbiKy6AAG8XgDQ_GkBHkslv2kjIdRJUgU')

songs = Songs(client.users_likes_tracks())
songs.download(PATH)
