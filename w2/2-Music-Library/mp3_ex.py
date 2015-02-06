from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from music_lib import Song
import os
import glob
def main():
    audio = MP3("NO ESCAPE MP3.mp3")
    #print (audio.info.__dict__)
    songs = []
    #for filename in os.listdir(os.getcwd()):

    for filename in glob.glob('*.mp3'):
        #if ".mp3" in filename:
            audio = MP3(filename, ID3=EasyID3)
            #print (audio.__dict__)
            for i in audio:
                #print (i, audio[i])
                pass
            print( filename)

            artist = audio["artist"][0]
            title = audio["title"][0]
            album = audio["album"][0]
            bitrate = audio.info.bitrate
            length = int(audio.info.length)
            if audio.info.length - length > 0.5:
                length = length + 1
            so = [artist, title, album, bitrate, length]
            #print (so)
            s = Song(title, artist, album, 0, length, bitrate)
            #print(s)
            songs.append((s, filename))
            #for i in 
            #print (EasyID3.valid_keys.keys())
    print(songs)
if __name__ == '__main__':
    main()