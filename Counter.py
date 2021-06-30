class Counter:
    index = 0
    track = ''
    msg = ''

    def __init__(self, index, track, msg):
        self.index = index
        self.track = track
        self.msg = msg

    def print(self):
        print(self.index + ' : ' + self.track + ' ' + self.msg)
