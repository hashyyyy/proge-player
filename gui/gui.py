import dearpygui.dearpygui as dpg
import player.player as player
from tkinter import filedialog
import gui.config as config
import os

# kasutame tkinteri filedialogi et lasta kasutajal mangitav fail valida

def delete_window_callback(sender):
    dpg.delete_item(sender)

def load_song(sender, data):
    initial = str(os.getcwd() + f"\music\\")
    song_path = filedialog.askopenfilename(initialdir=initial, filetypes=[("MP3 files", "*.mp3")])
    if song_path:
        player.load_song(song_path)
        #dpg.set_value("Current Song", f"Loaded: {player.get_current_song()}")


def add_to_playlist(sender, data):
    initial = str(os.getcwd() + f"\music\\")
    song_path = filedialog.askopenfilename(initialdir=initial, filetypes=[("MP3 files", "*.mp3")])
    if song_path:
        player.add_to_new_playlist(song_path)
        dpg.delete_item("playlist_window")
        edit_playlist()

def edit_playlist():
    with dpg.window(label="Create Playlist", tag="playlist_window", width=200, height=200, on_close=delete_window_callback):
        dpg.render_dearpygui_frame()
        dpg.add_text("Music Player")
        dpg.add_button(label="Load Song", callback=add_to_playlist)
        dpg.add_button(label="Save playlist", callback=save_playlist)
        for i in player.new_playlist:
            dpg.add_text(i)

def load_playlist():
    with dpg.window(label="Load playlist", tag="load_playlist", width=200, height=200, on_close=delete_window_callback):
        playlists = player.get_playlists()
        for i in playlists:
            name = i.replace(".txt", "")
            dpg.add_button(label=name, callback=lambda: (player.select_playlist(name), dpg.delete_item("load_playlist")))
        

def save_playlist():
    with dpg.window(label="Save playlist", tag="textbox_window", width=200, height=200, on_close=delete_window_callback):
        input_text_tag = dpg.add_input_text(label="Enter name here:")
        dpg.add_button(label="Submit", callback=lambda: (player.save_playlist(str(dpg.get_value(input_text_tag))), dpg.delete_item("textbox_window"), dpg.delete_item("playlist_window")))


def create_gui():
    window_height = 200
    window_width = 600

    dpg.create_context()
    with dpg.window(label="Music Player", **config.main_window):
        dpg.add_button(label="Load Song", callback=load_song)
        dpg.add_button(label="Load playlist", callback=load_playlist)
        dpg.add_button(label="Volume Up", callback=player.volume_up)
        dpg.add_button(label="Volume Down", callback=player.volume_down)
        dpg.add_button(label="Create a playlist", callback=edit_playlist)
        with dpg.group(horizontal=True):
            dpg.add_button(label="Skip", pos=[0, window_height - 100], **config.button)
            dpg.add_button(label="Play/Pause", pos=[window_width/2 -50, window_height - 100], **config.play_button, callback=player.play_song)
            dpg.add_button(label="Skip", pos=[window_width - 50, window_height - 100], **config.button)
    
    dpg.create_viewport(title="Music Player", width=window_width, height=window_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

