import os.path
import json
from song import Song

class Playlist():
    def load(file_name):
        my_file = open(file_name, 'r')
        content = my_file.read()
        content = json.loads(content)
        my_file.close()
        loaded_plist = Playlist(content['name'])
        for song in content['songs']:
            loaded_plist.songs.append(
                Song(
                    song['name'],
                    song['artist'],
                    song['album'],
                    song['rating'],
                    song['length'],
                    song['bitrate']
                )
            )
        return loaded_plist

    def __init__(self, pls_name):
        self.name = pls_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        index = len(self.songs) - 1
        while index >= 0:
            if self.songs[index] is not None:
                if self.songs[index].title == song_name:
                    self.songs[index] = None
            index = index - 1

    def total_length(self):
        leng = 0
        for i in self.songs:
            leng = leng + i.length

        return leng

    def remove_disrated(self,rating):
        for i in self.songs:
            if i.rating <= rating:
                self.remove_song(i.title)

    def remove_bad_quality(self):
        index = len(self.songs) - 1
        while index >= 0:
            if self.songs[index] is not None:
                if self.songs[index].bitrate < 128:
                    self.songs[index] = None
            index = index - 1

    def show_artists(self):
        artists = []
        for i in self.songs:
            if i.artist not in artists:
                artists.append(i.artist)
        return artists

    def __str__(self):
        output = ""
        for i in self.songs:
            output = output + str(i) + "\n"

        return output


    def save(self):
        playlist = {"name": self.name, "songs": []}
        for item in self.songs:
            item = item.__dict__
            playlist["songs"].append(item)
        if os.path.isfile(self.name + ".json"):
            print("That playlist name is taken")
        else:
            my_file = open("{}.json".format(self.name), 'a+')
            my_file.write(json.dumps(playlist))
            my_file.close()
        
