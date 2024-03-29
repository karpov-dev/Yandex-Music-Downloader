import copy

from Logger import Logger
from Song import Song


def sort_key(track):
    return track.artists[0].name


class Songs:
    logger = {}
    liked_songs = []
    tracks = []

    def __init__(self, liked_songs):
        self.liked_songs = liked_songs
        self.logger = Logger()

    def fetch(self):
        self.logger.message('START FETCHING MUSIC DATA')

        counter = 0
        for base_info in self.liked_songs:
            counter += 1
            full_info = base_info.fetch_track()
            self.tracks.append(full_info)
            self.logger.message(str(counter) + '/' + str(len(self.liked_songs)) + ' : (' + str(round(counter / len(self.liked_songs) * 100, 3) ) + '%) ' + ': ' + full_info.title)

        print(self.tracks)

        for full_info in self.tracks:
            if len(full_info.artists) <= 1:
                continue

            for artist in full_info.artists:
                song_copy = copy.deepcopy(full_info)
                song_copy.artists = []
                song_copy.artists.append(artist)
                self.tracks.append(song_copy)

            self.tracks.remove(full_info)

        print(self.tracks)

        self.logger.message('FETCHING DATA WAS SUCCESS')

    def sort(self):
        self.logger.message('SORTING TRACKS')
        self.tracks = sorted(self.tracks, key=sort_key)
        self.logger.message('SORTING DONE')

    def download(self):
        self.fetch()
        self.sort()

        counter = 0
        for track_full_info in self.tracks:
            counter += 1
            song = Song(track_full_info)
            song.download()
            self.logger.message(str(counter) + '/' + str(len(self.liked_songs)) + ' : (' + str(round(counter / len(self.liked_songs) * 100, 3)) + '%) ' + ': ' + track_full_info.title)

        self.logger.print_finish_message()
