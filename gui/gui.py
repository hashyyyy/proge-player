import dearpygui.dearpygui as dpg
import player.player as player
from tkinter import filedialog
import gui.config as config
import gui.style as style
import os
import json

# kasutame tkinteri filedialogi et lasta kasutajal mangitav fail valida


def delete_window_callback(sender):
    dpg.delete_item(sender)


def load_song(sender, data):
    initial = str(os.getcwd() + f"\music\\")
    song_path = filedialog.askopenfilename(
        initialdir=initial, filetypes=[("MP3 files", "*.mp3")]
    )
    if song_path:
        player.load_song(song_path)


def add_to_playlist(sender, data):
    initial = str(os.getcwd() + f"\music\\")
    song_path = filedialog.askopenfilename(
        initialdir=initial, filetypes=[("MP3 files", "*.mp3")]
    )
    if song_path:
        player.add_to_new_playlist(song_path)
        dpg.delete_item("playlist_window")
        edit_playlist()


def edit_playlist():
    with dpg.window(
        label="Create Playlist",
        tag="playlist_window",
        width=200,
        height=200,
        on_close=delete_window_callback,
    ):
        dpg.render_dearpygui_frame()
        dpg.add_text("Music Player")
        dpg.add_button(label="Load Song", callback=add_to_playlist)
        dpg.add_button(label="Save playlist", callback=save_playlist)
        for i in player.new_playlist:
            dpg.add_text(i)


def load_playlist():
    with dpg.window(
        label="Load playlist",
        tag="load_playlist",
        width=200,
        height=200,
        on_close=delete_window_callback,
    ):
        playlists = player.get_playlists()
        for i in playlists:
            name = i.replace(".txt", "")
            dpg.add_button(
                label=name,
                callback=lambda sender: (
                    player.select_playlist(dpg.get_item_label(sender)),
                    dpg.delete_item("load_playlist"),
                ),
            )


def save_playlist():
    with dpg.window(
        label="Save playlist",
        tag="textbox_window",
        width=200,
        height=200,
        on_close=delete_window_callback,
    ):
        input_text_tag = dpg.add_input_text(label="Enter name here:")
        dpg.add_button(
            label="Submit",
            callback=lambda: (
                player.save_playlist(str(dpg.get_value(input_text_tag))),
                dpg.delete_item("textbox_window"),
                dpg.delete_item("playlist_window"),
            ),
        )


def expand_slider():
    dpg.configure_item("volume_slider", width=200)
    dpg.configure_item("volume_slider", height=20)


def contract_slider():
    dpg.configure_item("volume_slider", width=20)
    dpg.configure_item("volume_slider", height=20)


def check_hover():
    if dpg.is_item_hovered("volume_slider"):
        expand_slider()
    else:
        contract_slider()


# COLOR SCHEME

default_colors = {
    "button_color": [0.1, 0.1, 0.1, 1.0],  # RGB with alpha (light blue)
    "button_hover_color": [0.5, 0.7, 1.0, 1.0],  # Light blue hover effect
    "background_color": [0.1, 0.1, 0.1, 1.0],  # Dark background
    "text_color": [1.0, 1.0, 1.0, 1.0],  # White text
    "slider_color": [0.2, 0.1, 1.0, 1.0],  # Light slider color
}

config_file = "colors.json"


def load_color_scheme():
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            color_scheme = json.load(f)
    else:
        color_scheme = default_colors
    return color_scheme


def open_menu():
    with dpg.window(
        label="Menu",
        tag="playlist_window",
        width=200,
        height=200,
        on_close=delete_window_callback,
    ):
        dpg.render_dearpygui_frame()
        dpg.add_text("Menu")
        with dpg.group(tag="vertical-buttons"):
            dpg.bind_item_theme("vertical-buttons", "button_theme")
            dpg.add_button(label="Load Song", callback=load_song)
            dpg.add_button(label="Load playlist", callback=load_playlist)
            dpg.add_button(label="Create a playlist", callback=edit_playlist)
        for i in player.new_playlist:
            dpg.add_text(i)


def create_color_scheme(color_scheme):

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            # Background color
            dpg.add_theme_color(
                dpg.mvThemeCol_WindowBg,
                color_scheme["background_color"],
                category=dpg.mvThemeCat_Core,
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ChildBg,
                color_scheme["background_color"],
                category=dpg.mvThemeCat_Core,
            )

            # Button colors
            dpg.add_theme_color(
                dpg.mvThemeCol_Button,
                color_scheme["button_color"],
                category=dpg.mvThemeCat_Core,
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ButtonHovered,
                color_scheme["button_hover_color"],
                category=dpg.mvThemeCat_Core,
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ButtonActive,
                color_scheme["button_hover_color"],
                category=dpg.mvThemeCat_Core,
            )

            # Text color
            dpg.add_theme_color(
                dpg.mvThemeCol_Text,
                color_scheme["text_color"],
                category=dpg.mvThemeCat_Core,
            )

            # Slider color
            dpg.add_theme_color(
                dpg.mvThemeCol_SliderGrab,
                color_scheme["slider_color"],
                category=dpg.mvThemeCat_Core,
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_SliderGrabActive,
                color_scheme["slider_color"],
                category=dpg.mvThemeCat_Core,
            )


def update_song_name(name):
    dpg.set_value("playing_song", name)


def create_gui():
    # start of the gen
    dpg.create_context()

    # COLORS AND STUFF

    style.load_themes()
    # WINDOW CREATION STUFF

    with dpg.window(label="Music Player", **config.main_window) as main_window:
        window_height, window_width = (
            config.main_window["height"],
            config.main_window["width"],
        )
        dpg.bind_item_theme(main_window, "app_theme")
        dpg.add_button(label="Menu", tag="open_menu", callback=open_menu)
        dpg.add_text(
            tag="playing_song", default_value=player.current_song, **config.text
        )
        with dpg.group(horizontal=True, tag="buttons"):
            dpg.bind_item_theme("buttons", "button_theme")
            dpg.add_button(
                label="Skip",
                pos=[8, window_height - 100],
                **config.button,
                callback=player.skip_song,
            )
            dpg.add_button(
                label="Play/Pause",
                pos=[window_width / 2 - 70, window_height - 100],
                **config.play_button,
                callback=player.play_song,
            )
            dpg.add_button(
                label="Skip",
                pos=[window_width - 58, window_height - 100],
                **config.button,
                callback=player.skip_song,
            )

        default_volume = 5
        player.update_volume("", default_volume, "")
        slider = dpg.add_slider_int(
            label="Volume (hover)",
            min_value=0,
            max_value=100,
            default_value=default_volume,
            callback=player.update_volume,
            width=20,
            tag="volume_slider",
        )

        with dpg.handler_registry():
            dpg.add_mouse_move_handler(callback=lambda: check_hover())

    dpg.bind_item_handler_registry(slider, "slider_handler")

    # FONT STUFF

    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_dir, "0xProtoNerdFontPropo-Regular.ttf")

    with dpg.font_registry():
        default_font = dpg.add_font(font_path, 20)
    window_height, window_width = (
        config.main_window["height"] + 10,
        config.main_window["width"] + 10,
    )

    dpg.bind_font(default_font)
    dpg.create_viewport(
        title="Music Player", width=window_width, height=window_height, resizable=False
    )
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
