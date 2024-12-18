import dearpygui.dearpygui as dpg
import player.player as player
from tkinter import filedialog
import gui.config as config
import gui.style as style
import os
import time

# kasutame tkinteri filedialogi et lasta kasutajal mangitav fail valida


def load_song(sender, data):
    initial = str(os.getcwd() + f"\music\\")
    song_path = filedialog.askopenfilename(
        initialdir=initial, filetypes=[("MP3 files", "*.mp3")]
    )
    if song_path:
        player.load_song(song_path)


def add_to_playlist():
    initial = str(os.getcwd() + f"\music\\")
    song_path = filedialog.askopenfilename(
        initialdir=initial, filetypes=[("MP3 files", "*.mp3")]
    )
    if song_path:
        player.add_to_new_playlist(song_path)
        dpg.set_value("playlist_songs", value="\n".join(player.new_playlist))


def create_elements():
    # loob vajaminevad elemendid ja peidab need alguses nahtavusest
    with dpg.window(
        label="Create Playlist",
        tag="create_playlist",
        **config.window,
        on_close=lambda: (
            player.clear_playlist(),
            dpg.set_value("playlist_songs", value=""),
        ),
        pos=[7, 8],
    ):
        with dpg.group(tag="create_playlist_choices"):
            dpg.add_button(label="Load Song", callback=add_to_playlist)
            dpg.add_button(label="Save playlist", callback=save_playlist)
            for i in player.new_playlist:
                dpg.add_text(i)

        dpg.bind_item_theme("create_playlist_choices", "button_theme")

    dpg.add_text("", tag="playlist_songs")
    dpg.bind_item_theme("create_playlist", "menu_theme")

    with dpg.window(
        label="Load playlist", tag="load_playlist", **config.window, pos=[7, 8]
    ):
        with dpg.group(tag="playlist_choices"):
            playlists = player.get_playlists()
            for i in playlists:
                name = i.replace(".txt", "")
                dpg.add_button(
                    label=name,
                    callback=lambda sender: (
                        player.select_playlist(dpg.get_item_label(sender)),
                        dpg.hide_item("load_playlist"),
                    ),
                )
    dpg.bind_item_theme("playlist_choices", "button_theme")
    dpg.bind_item_theme("load_playlist", "menu_theme")

    with dpg.window(
        label="Save playlist", tag="save_playlist", **config.window, pos=[7, 8]
    ):
        input_text_tag = dpg.add_input_text(label="")
        with dpg.group(tag="save_playlist_choices"):
            dpg.add_button(
                label="Submit",
                callback=lambda: (
                    player.save_playlist(str(dpg.get_value(input_text_tag))),
                    dpg.hide_item("save_playlist"),
                    dpg.hide_item("create_playlist"),
                ),
            )
        dpg.bind_item_theme("save_playlist_choices", "button_theme")
    dpg.bind_item_theme("save_playlist", "menu_theme")

    with dpg.window(
        label="···",
        tag="menu",
        **config.window,
        pos=[7, 8],
    ):

        with dpg.group(tag="vertical-buttons"):
            dpg.bind_item_theme("vertical-buttons", "button_theme")
            dpg.add_button(label="Load Song", callback=load_song)
            dpg.add_button(label="Load playlist", callback=load_playlist)
            dpg.add_button(label="Create playlist", callback=create_playlist)
    dpg.bind_item_theme("menu", "menu_theme")


def create_playlist():
    # alguses itemid peidetakse ja tuuakse siis uuesti nahtavale et oleks kindel, nad kuhugi ara ei kao.
    dpg.hide_item("create_playlist")
    time.sleep(0.1)
    dpg.show_item("create_playlist")


def load_playlist():
    dpg.hide_item("load_playlist")
    time.sleep(0.1)
    dpg.show_item("load_playlist")


def save_playlist():
    dpg.hide_item("save_playlist")
    time.sleep(0.1)
    dpg.show_item("save_playlist")


def open_menu():
    dpg.hide_item("menu")
    time.sleep(0.1)
    dpg.show_item("menu")


def expand_slider():
    dpg.configure_item("volume_slider", width=25)
    dpg.configure_item("volume_slider", height=100)
    dpg.configure_item("volume_slider", show=True)


def contract_slider():
    dpg.configure_item("volume_slider", width=0)
    dpg.configure_item("volume_slider", height=0)
    dpg.configure_item("volume_slider", show=False)


def hide_volume():
    dpg.configure_item("volume_icon", show=False)


def show_volume():
    dpg.configure_item("volume_icon", show=True)


def check_hover():
    if dpg.is_item_hovered("volume_icon") or dpg.is_item_hovered("volume_slider"):
        expand_slider()
        hide_volume()
    else:
        contract_slider()
        show_volume()


def update_song_name(name):
    dpg.set_value("playing_song", name)


def play_pressed():
    print(player.current_song)
    if player.current_song:
        player.play_song()
        if dpg.get_item_label("play_button") == "[play]":
            dpg.set_item_label("play_button", "[stop]")
        else:
            dpg.set_item_label("play_button", "[play]")


def move_text(title):
    if player.current_song:
        current_song = player.current_song
        curr_x, curr_y = dpg.get_item_pos(title)
        window_width = config.main_window["width"]
        text_width = len(current_song)

        new_x = curr_x + 1

        if new_x > window_width:
            new_x = 0 - text_width * 10

        dpg.set_item_pos(title, (new_x, curr_y))


def create_gui():
    # start of the gen
    dpg.create_context()
    # COLORS AND STUFF

    style.load_themes()

    # LOAD IMAGE
    image_path = os.path.join(os.getcwd(), "gui", "images", "volume5.png")

    if not os.path.isfile(image_path):
        print("ERROR: Couldn't find the image")

    width, height, channels, data = dpg.load_image(image_path)

    # TEXTURE IMAGE STUFF

    with dpg.texture_registry():
        dpg.add_static_texture(width, height, data, tag="volume_icon_texture")

    # WINDOW CREATION STUFF

    with dpg.window(label="Music Player", **config.main_window) as main_window:
        window_height, window_width = (
            config.main_window["height"],
            config.main_window["width"],
        )

        # bind theme to window
        dpg.bind_item_theme(main_window, "app_theme")

        with dpg.group(horizontal=True, tag="closed_menu"):
            dpg.add_button(label="···", callback=open_menu)

        # bind theme to menu
        dpg.bind_item_theme("closed_menu", "closed_menu_theme")
        dpg.add_text(
            pos=(75, 125), tag="progress_bar", default_value="[--------------------]"
        )

        title = dpg.add_text(
            tag="playing_song",
            default_value=player.current_song,
            **config.text,
            pos=[-40, window_height / 2],
        )
        with dpg.group(horizontal=True, tag="buttons"):
            dpg.bind_item_theme("buttons", "button_theme")
            dpg.add_button(
                label="[skip]",
                pos=[8, window_height - 50],
                **config.button,
                callback=player.back_song,
            )
            dpg.add_button(
                label="[stop]",
                pos=[window_width / 2 - 60, window_height - 60],
                **config.play_button,
                callback=play_pressed,
                tag="play_button",
            )
            dpg.add_button(
                label="[skip]",
                pos=[window_width - 78, window_height - 50],
                **config.button,
                callback=player.skip_song,
            )

        default_volume = 5
        player.update_volume("", default_volume, "")

        slider = dpg.add_slider_int(
            label="",
            pos=[window_width - 33, 8],
            min_value=0,
            max_value=50,
            default_value=default_volume,
            callback=player.update_volume,
            width=0,
            tag="volume_slider",
            show=False,
            vertical=True,
            format="",
        )

        create_elements()

        dpg.bind_item_theme(slider, "slider_theme")

        volume_icon = dpg.add_image(
            "volume_icon_texture",
            tag="volume_icon",
            pos=[window_width - 33, 8],
        )

        with dpg.handler_registry():
            dpg.add_mouse_move_handler(callback=lambda: check_hover())

    dpg.bind_item_handler_registry(volume_icon, "slider_handler")

    # FONT STUFF

    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_dir, "0xProtoNerdFontPropo-Regular.ttf")

    with dpg.font_registry():
        default_font = dpg.add_font(font_path, 18)
    window_height, window_width = (
        config.main_window["height"],
        config.main_window["width"] + 16,
    )

    dpg.bind_font(default_font)
    dpg.create_viewport(
        title="Music Player", width=window_width, height=window_height, resizable=False
    )
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.start_dearpygui()

    while dpg.is_dearpygui_running():
        move_text(title)
        pr = player.percentage_played(player.song_length)
        # dpg.delete_item(drawlist_id, children_only=True)
        if pr:
            pr = round(pr * 20)
            val = str("[" + pr * "*" + (20 - pr) * "-" + "]")
            dpg.set_value("progress_bar", val)
        dpg.render_dearpygui_frame()


dpg.destroy_context()
