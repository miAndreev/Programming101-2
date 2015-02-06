class Song():
    MAX_RATING = 5
    MIN_RATING = 1
    def __init__(self, title, artist, album, rating, length, bitrate):    
        self.title = title
        self.artist = artist
        self.album = album
        self.rate(rating)
        self.length = length
        self.bitrate = bitrate
        self.file_name = ""

    def rate(self, rating):
        if rating >= 0 and rating <= 5:
            self.rating = rating
        else:
            formatted = "Rating must be between {} and {}"
            raise ValueError(formatted.format(Song.MIN_RATING, Song.MAX_RATING))

    def __str__(self):
        minutes = self.length//60
        seconds = self.length % 60
        if seconds < 10:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)
        str_out = self.artist + " " + self.title + " - " + str(minutes) + ":" + seconds
        return str_out

    def add_file_name(self, file_name):
        self.file_name = file_name
