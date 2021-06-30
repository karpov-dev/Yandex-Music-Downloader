import eyed3
import os
from Log import log


class Song:
    describe = {}

    def __init__(self, describe):
        self.describe = describe

    def artists(self):
        artists = ''

        for artist in self.describe.artists:
            artists += artist.name + ' '

        return artists

    def track_name(self):
        return self.artists() + ' - ' + self.describe.title + '.mp3'

    def full_path(self, path):
        return self.path_with_folder(path) + '/' + self.track_name()

    def path_with_folder(self, path):
        return path + '/' + self.artists()[0].upper()

    def download(self, path):
        if self.is_exists(path):
            return 'EXISTS'

        if not self.download_track(path):
            return 'DOWNLOAD ERROR'

        self.prepare_metadata(path)

        return 'SUCCESS'

    def is_exists(self, path):
        if not os.path.isdir(self.path_with_folder(path)):
            os.mkdir(self.path_with_folder(path))
            return False
        if os.path.isfile(self.full_path(path)):
            return True

    def download_track(self, path):
        try:
            self.describe.download(self.full_path(path))
            return True
        except Exception as error:
            log(self.track_name(), 'DOWNLOAD ERROR', error)
            return False

    def prepare_metadata(self, path):
        try:
            song = eyed3.load(self.full_path(path))
            song.initTag()

            song.tag.artist = self.artists()
            song.tag.album = self.describe.albums[0].title
            song.tag.album_artist = self.artists()
            song.tag.title = self.describe.title

            song.tag.save()
        except Exception as error:
            log(self.track_name(), 'METADATA ERROR', error)
