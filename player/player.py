import pygame, os

#Kasutame pygame'i, mis ei ole võibolla kõige optimaalsem, aga meile on loodetavasti piisav.
pygame.mixer.init()

current_playlist=[]
volume = 0.0
current_song = None
playing = True

def load_song(song_path):
    global current_song
    pygame.mixer.music.load(song_path)
    current_song = song_path
    pygame.mixer.music.play()

def add_to_current_playlist(song_path):
    global current_playlist
    current_playlist.append(str(song_path).split("/")[-1])

def save_playlist(name):
    #Salvestab playlisti faili laulude nimed, et playliste salvestada.
    global current_playlist
    p = str(os.getcwd() + f"\player\playlists\{name}.txt")
    with open(p, "w", encoding="UTF-8") as f:
        for i in current_playlist:
            f.write(i + "\n")
    f.close()

def play_song():
    global playing
    if not playing:
        pygame.mixer.music.unpause()
        playing=True
    else:
        pygame.mixer.music.pause()
        playing=False

def pause_song():
    pygame.mixer.music.pause()

def volume_up():
     global volume
     if volume <= 1.0:
          volume += 0.1
          pygame.mixer.music.set_volume(volume)
    
def volume_down():
     global volume
     if volume >= 0.0:
          volume -= 0.1
          pygame.mixer.music.set_volume(volume)

def resume_song():
    pygame.mixer.music.unpause()

def stop_song():
    pygame.mixer.music.stop()

def get_current_song():
       return current_song.split('/')[-1] if current_song else "No song loaded" 
