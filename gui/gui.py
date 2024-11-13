import dearpygui.dearpygui as dpg
import player.player as player
from tkinter import filedialog

# kasutame tkinteri filedialogi et lasta kasutajal mangitav fail valida

def load_song(sender, data):
    song_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if song_path:
        player.load_song(song_path)
        #dpg.set_value("Current Song", f"Loaded: {player.get_current_song()}")
        player.play_song()

def create_gui():
    dpg.create_context()
    dpg.create_viewport(title="Music Player", width=300, height=200)
    with dpg.window(label="Music Player"):
        dpg.add_text("Music Player")
        dpg.add_button(label="Load Song", callback=load_song)
        dpg.add_button(label="Play", callback=player.play_song)
        dpg.add_button(label="Pause", callback=player.pause_song)
        dpg.add_button(label="Resume", callback=player.resume_song)
        dpg.add_button(label="Stop", callback=player.stop_song)
        dpg.add_button(label="Volume Up", callback=player.volume_up)
        dpg.add_button(label="Volume Down", callback=player.volume_down)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
