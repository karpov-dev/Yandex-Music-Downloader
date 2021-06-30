from Log import log
from Song import Song
from Counter import Counter
from Folder import rename_with_count


def sort_key(track):
    return track.title


class Songs:
    liked_songs = []
    tracks = []

    def __init__(self, liked_songs):
        self.liked_songs = liked_songs

    def fetch(self):
        log('ALL TRACKS', 'FETCHING DATA', None)

        counter = 0
        for base_info in self.liked_songs:
            counter += 1
            full_info = base_info.fetch_track()
            self.tracks.append(full_info)
            log(str(counter), 'FETCH SUCCESS', full_info)

        log('ALL TRACKS', 'FETCHING DATA SUCCESS', None)

    def sort(self):
        log('ALL TRACKS', 'SORTING TRACKS', None)
        self.tracks = sorted(self.tracks, key=sort_key)
        log('ALL TRACKS', 'SORTING DONE', None)

    def download(self, path):
        self.fetch()
        self.sort()

        errors_counter = []
        skip_counter = []
        success_counter = []
        index_counter = 0

        for track_full_info in self.tracks:
            index_counter += 1
            song = Song(track_full_info)
            result = song.download(path)

            if result == 'EXISTS':
                skip_counter.append(Counter(str(index_counter), song.track_name(), '---- SKIP ----').print())
            if result == 'DOWNLOAD ERROR':
                errors_counter.append(Counter(str(index_counter), song.track_name(), '---- DOWNLOAD ERROR ----').print())
            if result == 'SUCCESS':
                success_counter.append(Counter(str(index_counter), song.track_name(), '---- SUCCESS ----').print())

        print('TOTAL: ' + str(index_counter))
        print('SUCCESS: ' + str(len(success_counter)))
        print('SKIP: ' + str(len(skip_counter)))
        print('ERROR: ' + str(len(errors_counter)))