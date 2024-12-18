import pygame
import os
import random
import time
import gui.gui as gui
import re
from mutagen.mp3 import MP3

# Kasutame pygame'i, mis ei ole võibolla kõige optimaalsem, aga meile on loodetavasti piisav.
pygame.mixer.init()

new_playlist = []
active_playlist = []
volume = 0.0
current_song = ""
playing = True
song_length = ""
last_songs = []

def clear_playlist():
    global new_playlist
    new_playlist = []


def get_playlists():
    playlists = []
    path = os.path.join(os.getcwd(), "player", "playlists")
    for playlist in os.listdir(path):
        playlists.append(playlist)
    return playlists


def select_playlist(name):
    global active_playlist
    active_playlist = []
    path = os.path.join(os.getcwd(), "player", "playlists", f"{name}.txt")
    for i in open(path, "r", encoding="UTF-8").readlines():
        active_playlist.append(i.strip())
    random.shuffle(active_playlist)


def add_to_new_playlist(song_path):
    global new_playlist
    new_playlist.append(str(song_path).split("/")[-1])


def save_playlist(name):
    # Salvestab playlisti faili laulude nimed, et playliste salvestada.
    global new_playlist
    p = os.path.join(os.getcwd(), "player", "playlists", f"{name}.txt")
    with open(p, "w", encoding="UTF-8") as f:
        for i in new_playlist:
            f.write(i + "\n")
    f.close()
    new_playlist = []


def load_song(song_path):
    global current_song, song_length
    if song_path:
        song_length = MP3(song_path).info.length
        #splitib vastavalt opsysteemile ja votab viimase vaartuse ehk nime
        current_song = re.split(r"\\\\|//|/|\\", song_path)[-1]
        gui.update_song_name(current_song)
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()


def play_song():
    global playing
    if not playing:
        pygame.mixer.music.unpause()
        playing = True
    else:
        print("asds")
        pygame.mixer.music.pause()
        playing = False

def percentage_played(song_length):
    song_pos = pygame.mixer.music.get_pos()
    if song_length and song_pos:
        return round((song_pos/1000)/song_length,2)

def skip_song():
    global current_song, last_songs
    if current_song:
        last_songs.append(current_song)
    current_song = None
    pygame.mixer.music.stop()

def back_song():
    global current_song, last_songs, active_playlist
    if last_songs:
        if current_song:
            active_playlist.append(current_song)
        current_song = last_songs.pop()
        load_song(os.path.join(os.getcwd(), "music", f"{current_song}"))

def update_volume(sender, app_data, user_data):
    volume = app_data / 100.0
    pygame.mixer.music.set_volume(volume)


def is_playing():
    global current_song, active_playlist, last_songs
    while True:
        if not current_song and active_playlist:
            last_songs
            current_song = active_playlist.pop(0)
            load_song(os.path.join(os.getcwd(), "music", f"{current_song}"))
        else:
            time.sleep(0.01)
