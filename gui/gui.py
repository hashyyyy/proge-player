import dearpygui.dearpygui as dpg
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
    dpg.create_context()
    dpg.create_viewport(title="Music Player", width=300, height=200)
    with dpg.window(label="Music Player"):
        dpg.add_text("Music Player")
        dpg.add_button(label="Load Song", callback=load_song)
        dpg.add_button(label="Play", callback=play_song)
        dpg.add_button(label="Pause", callback=pause_song)
        dpg.add_button(label="Resume", callback=resume_song)
        dpg.add_button(label="Stop", callback=stop_song)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
