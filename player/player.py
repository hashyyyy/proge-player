import pygame

#Kasutame pygame'i, mis ei ole võibolla kõige optimaalsem, aga meile on loodetavasti piisav.
pygame.mixer.init()

volume = 0.0
current_song = None

def load_song(song_path):
    global current_song
    pygame.mixer.music.load(song_path)
    current_song = song_path

def play_song():
    pygame.mixer.music.play()

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
