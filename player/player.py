import pygame

pygame.mixer.init()

current_song = None

def load_song(song_path):
    global current_song
    pygame.mixer.music.load(song_path)
    current_song = song_path

def play_song():
    pygame.mixer.music.play()

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.resume()

def stop_song():
    pygame.mixer.music.stop()

def get_current_song():
       return current_song.split('/')[-1] if current_song else "No song loaded" 
