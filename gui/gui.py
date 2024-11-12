from dearpygui import *
import player.player as player
from tkinter import filedialog

def load_song(sender, data):
    song_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if song_path:
        player.load_song(song_path)
        set_value("Current Song", f"Loaded: {player.get_current_song()}")
        player.play_song()

def play_song(sender, data):
    player.play_song()

def pause_song(sender, data):
    player.pause_song()

def resume_song(sender, data):
    player.resume_song()

def stop_song(sender, data):
    player.stop_song()

def create_gui():
    with window("Music Player", width=300, height=200):
        add_text("Music Player")
        add_button("Load Song", callback=load_song)
        add_button("Play", callback=play_song)
        add_button("Pause", callback=pause_song)
        add_button("Resume", callback=resume_song)
        add_button("Stop", callback=stop_song)
        add_label_text("Current Song", default_value="No song loaded")
    start_dearpygui()
