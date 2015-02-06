from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from song import Song
from playlist import Playlist
import os
import glob
import fnmatch

class Music_crawler():
    def __init__(self, path):
        self.path = path


    def craw_dir(self):
        #audio = MP3("NO ESCAPE MP3.mp3")
        songs = []
        print (self.path)
        #mp3_fieles = [ f for f in os.listdir(self.path) if re.match(r'*\.mp3', f) ]
        #mp3_fieles = [ f for f in os.listdir(self.path) if fnmatch.fnmatch(f, '*.mp3') ]
        #print (mp3_fieles)
        for filename in glob.glob(os.path.join(self.path, '**.mp3')):
        #for filename in mp3_fieles:
            audio = MP3(filename, ID3=EasyID3)
            print(filename)
            artist = audio["artist"][0]
            title = audio["title"][0]
            album = audio["album"][0]
            bitrate = audio.info.bitrate
            length = int(audio.info.length)
            if audio.info.length - length > 0.5:
                length = length + 1
            so = [artist, title, album, bitrate, length]
            
            s = Song(title, artist, album, 0, length, bitrate)
            
            songs.append((s, filename))
            
        print(songs)
        return songs

    def generate_pls(self):
        pass
        songs = self.craw_dir()
        pls_name = self.path.replace("/","_")
        pls = Playlist(pls_name)
        for song in songs:
            s = song[0]
            s = s.add_file_name(song[1])#.add_file_name(song[1])
            pls.add_song(s)
        pls.save()
        return pls

if __name__ == '__main__':
    cr = Music_crawler("/media/mihail/data/music/bg/КGB (Кольо Гилън Банд)/(2008) Swing Time") #"/home/mihail/Музика")
    p = cr.generate_pls()
    #cr = Music_crawler("/home/mihail/solutions/w2/2-Music-Library")
    #p = cr.generate_pls()


