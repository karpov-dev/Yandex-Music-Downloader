from yandex_music import Client
import eyed3
import os


class ErrorLog:
    counter = 0
    errors = []

    def log(self, song, type, msg):
        self.counter += 1
        self.errors.append(song + ' --- ' + type + ' --- ' + msg + '\n')

    def show(self):
        for error in self.errors:
            print(error)


LOGIN = 'passangerfeat@yandex.ru'
PASSWORD = '2015883Vova'
TOKEN = 'AQAAAAAbiKy6AAG8XgDQ_GkBHkslv2kjIdRJUgU'
PATH = "F:/"


client = Client.from_token('AQAAAAAbiKy6AAG8XgDQ_GkBHkslv2kjIdRJUgU')
musicCounter = 0
successCounter = 0
skippedCounter = 0
errors = ErrorLog()

for baseTrack in client.users_likes_tracks():
    track = baseTrack.fetch_track()

    trackName = track.artists[0].name + ' - ' + track.title.replace('?', '').replace('/', '')
    trackNameWithExtension = trackName + '.mp3'

    folderName = track.artists[0].name[0].upper()
    fullPath = PATH + folderName + '/' + trackNameWithExtension

    try:
        musicCounter += 1

        try:
            if not os.path.isdir(PATH + folderName):
                os.mkdir(PATH + folderName)
            if os.path.isfile(fullPath):
                print(str(musicCounter) + ' : ' + trackName + ' --- SKIP ---')
                skippedCounter += 1
                continue
        except Exception as err:
            errors.log(trackName, 'PATH ERROR', err)

        try:
            track.download(fullPath)
        except Exception as err:
            errors.log(trackName, 'DOWNLOAD ERROR', err)

        song = eyed3.load(fullPath)
        song.initTag()

        song.tag.artist = track.artists[0].name
        song.tag.album = track.albums[0].title
        song.tag.album_artist = track.artists[0].name
        song.tag.title = track.title

        song.tag.save()
        print(str(musicCounter) + ' : ' + trackName + ' --- DONE ---')

        successCounter += 1

    except:
        print(str(musicCounter) + ' : ' + trackName + ' --- ERROR ---')

print('ALL SONGS: ' + str(musicCounter))
print('SUCCESS: ' + str(successCounter))
print('SKIPPED: ' + str(skippedCounter))
errors.show()


