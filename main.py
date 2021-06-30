from yandex_music import Client
from Songs import Songs
import logging


class ErrorLog:
    counter = 0
    errors = []

LOGIN = 'passangerfeat@yandex.ru'
PASSWORD = '2015883Vova'
TOKEN = 'AQAAAAAbiKy6AAG8XgDQ_GkBHkslv2kjIdRJUgU'
PATH = "/home/user/Documents/"

client = Client.from_token('AQAAAAAbiKy6AAG8XgDQ_GkBHkslv2kjIdRJUgU')

logging.getLogger('yandex_music').setLevel(logging.raiseExceptions)

songs = Songs(client.users_likes_tracks())
songs.download(PATH)


