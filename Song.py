import eyed3


class Song:
    describe = {}

    def __init__(self, describe):
        self.describe = describe

    def artists(self):
        artists = ''

        for artist in self.describe.artists:
            artists += artist.name

        return artists

    def track_name(self):
        return self.artists() + ' - ' + self.describe.title + '.mp3'

    def full_path(self, path):
        return path + '/' + self.track_name()

    def download(self, path):
        if self.download_track(path) is None:
            return None
        self.prepare_metadata(path)

        print(self.track_name() + ' ----- DONE ----- ')


    def download_track(self, path):
        try:
            return self.describe.download(self.full_path(path))
        except Exception as error:

            return None

    def prepare_metadata(self, path):
        song = eyed3.load(self.full_path(path))
        song.initTag()

        song.tag.artist = self.artists()
        song.tag.album = self.describe.albums[0].title
        song.tag.album_artist = self.artists()
        song.tag.title = self.describe.title

        song.tag.save()
