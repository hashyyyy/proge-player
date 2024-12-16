import pygame
import os
import random

#Kasutame pygame'i, mis ei ole võibolla kõige optimaalsem, aga meile on loodetavasti piisav.
pygame.mixer.init()

new_playlist=[]
active_playlist=[]
volume = 0.0
current_song = None
playing = True

def get_playlists():
    playlists = []
    path = str(os.getcwd() + f"\player\playlists\\")
    for playlist in os.listdir(path):
        playlists.append(playlist)
    return playlists

def select_playlist(name):
    global active_playlist
    active_playlist = []
    path = str(os.getcwd() + f"\player\playlists\{name}.txt")
    for i in open(path, "r", encoding="UTF-8").readlines():
        active_playlist.append(i.strip())
    random.shuffle(active_playlist)
    print(active_playlist)

def load_song(song_path):
    global current_song
    pygame.mixer.music.load(song_path)
    current_song = song_path
    pygame.mixer.music.play()

def add_to_new_playlist(song_path):
    global new_playlist
    new_playlist.append(str(song_path).split("/")[-1])

def save_playlist(name):
    #Salvestab playlisti faili laulude nimed, et playliste salvestada.
    global new_playlist
    p = str(os.getcwd() + f"\player\playlists\{name}.txt")
    with open(p, "w", encoding="UTF-8") as f:
        for i in new_playlist:
            f.write(i + "\n")
    f.close()
    new_playlist = []

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

# while pygame.mixer.music.get_busy():
#     print("123")
#     pygame.time.Clock.tick(1)
#     break

# while active_playlist and not pygame.mixer.music.get_busy():
#     print("sds")
#     break
#     # path = str(os.getcwd() + f"\music\\{active_playlist.pop()}.txt")
#     # print(path)
#     # load_song(path)
    