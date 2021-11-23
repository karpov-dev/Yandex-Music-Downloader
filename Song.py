import eyed3
from Logger import Logger
from Service import is_file_exists, create_dir_if_not_exist, delete_service_symbols
from Config import FILE_SYSTEM_SEPARATOR, MUSIC_FILE_EXTENSION, ROOT_PATH


class Song:

    describe = {}
    logger = {}
    total_tracks = 0

    def __init__(self, track_describe):
        self.describe = track_describe
        self.logger = Logger()

    def download(self):
        self.__separate_download__()

    def __separate_download__(self):
        for artist in self.describe.artists:
            self.__download_to_artist_folder__(artist.name)

    def __download_to_artist_folder__(self, artist_name):
        create_dir_if_not_exist(self.__get_path_to_symbol_folder__(artist_name))
        create_dir_if_not_exist(self.__get_path_to_artist_folder__(artist_name))

        if is_file_exists(self.__get_path_to_track__(artist_name)):
            self.logger.download_skip(self.__get_track_name_with_artist__(artist_name))
        else:
            try:
                self.describe.download(self.__get_path_to_track__(artist_name))
                self.prepare_metadata(self.__get_path_to_track__(artist_name), artist_name)
                self.logger.download_success(self.__get_track_name_with_artist__(artist_name))
            except Exception as error:
                self.logger.download_error(self.__get_track_name_with_artist__(artist_name), error)

    def __get_path_to_symbol_folder__(self, artist_name):
        return ROOT_PATH + FILE_SYSTEM_SEPARATOR + delete_service_symbols(artist_name[0].upper())

    def __get_path_to_artist_folder__(self, artist_name):
        return self.__get_path_to_symbol_folder__(artist_name) + FILE_SYSTEM_SEPARATOR + delete_service_symbols(artist_name)

    def __get_path_to_track__(self, artist_name):
        return self.__get_path_to_artist_folder__(artist_name) + FILE_SYSTEM_SEPARATOR + self.__get_track_name__()

    def __get_track_name__(self):
        track_name = delete_service_symbols(self.describe.title)

        if self.describe.version:
            track_name += '(' + delete_service_symbols(self.describe.version) + ')'

        track_name += MUSIC_FILE_EXTENSION

        return track_name

    def __get_track_name_with_artist__(self, artist_name):
        return artist_name + ' - ' + self.__get_track_name__()

    def prepare_metadata(self, path, artist_name):
        song = eyed3.load(path)
        song.initTag()

        song.tag.artist = artist_name
        song.tag.album = self.describe.albums[0].title
        song.tag.album_artist = artist_name
        song.tag.title = self.describe.title

        song.tag.save()