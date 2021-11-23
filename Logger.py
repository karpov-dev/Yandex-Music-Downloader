from Singleton import Singleton


class DownloadMessage:
    index = 0
    track_name = ''
    status = ''
    message = ''

    def __init__(self, index, track_name, status, message):
        self.index = index
        self.track_name = track_name
        self.status = status
        self.message = message


class Logger(metaclass=Singleton):

    total_counter = 0
    success_messages = []
    error_messages = []
    skip_messages = []

    def download_success(self, track):
        self.total_counter += 1

        message = DownloadMessage(self.total_counter, track, 'SUCCESS', '-')
        self.success_messages.append(message)

        self.print_message(message)

    def download_skip(self, track):
        self.total_counter += 1
        self.success_messages.append(
            DownloadMessage(self.total_counter, track, 'SKIP', '-')
        )

    def download_error(self, track, error_message):
        self.total_counter += 1
        self.success_messages.append(
            DownloadMessage(self.total_counter, track, 'ERROR', error_message)
        )

    def message(self, message):
        print('-------' + message + '-------')

    def print_message(self, message):
        print('------- ' + message.track_name + ' -------')
        print('NUMBER: ' + str(self.total_counter))
        print('STATUS: ' + message.status)

        if message.status == 'ERROR':
            print('MESSAGE: ' + message.message)

    def print_finish_message(self):
        print('SUCCESS: ' + str(len(self.success_messages)))

        print('ERRORS: ' + str(len(self.error_messages)))
        for error_message in self.error_messages:
            print(error_message.track_name + ' : ' + error_message.message)

        print('SKIPPED: ' + str(len(self.skip_messages)))
        for skip_message in self.skip_messages:
            print(skip_message.track_name + ' : ' + skip_message.message)
