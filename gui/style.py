import dearpygui.dearpygui as dpg


def load_themes():
    button_color = [55, 157, 240]
    button_hover_color = [128, 179, 255]
    background_color = [139, 197, 246]
    text_color = [255, 255, 255]
    slider_color = [55, 157, 240]
    outer_color = [16, 84, 132]

    with dpg.theme(tag="app_theme"):
        with dpg.theme_component():
            dpg.add_theme_color(
                dpg.mvThemeCol_WindowBg, background_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_Text, text_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_Border, text_color, category=dpg.mvThemeCat_Core
            )

    with dpg.theme(tag="button_theme"):
        with dpg.theme_component():
            dpg.add_theme_style(
                dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_Button, button_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ButtonHovered,
                button_hover_color,
                category=dpg.mvThemeCat_Core,
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ButtonActive, button_color, category=dpg.mvThemeCat_Core
            )

    with dpg.theme(tag="slider_theme"):
        with dpg.theme_component():
            dpg.add_theme_color(
                dpg.mvThemeCol_SliderGrab, background_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_SliderGrabActive,
                background_color,
                category=dpg.mvThemeCat_Core,
            )
            dpg.add_theme_style(
                dpg.mvStyleVar_GrabRounding, 10, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_style(
                dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core
            )

    with dpg.theme(tag="closed_menu_theme"):
        with dpg.theme_component():
            dpg.add_theme_style(
                dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_Button, button_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ButtonHovered,
                button_hover_color,
                category=dpg.mvThemeCat_Core,
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ButtonActive, button_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_Border, text_color, category=dpg.mvThemeCat_Core
            )


    with dpg.theme(tag="menu_theme"):
        with dpg.theme_component():
            dpg.add_theme_color(
                dpg.mvThemeCol_WindowBg, background_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_Text, text_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_style(
                dpg.mvStyleVar_WindowRounding, 10, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_Border, button_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ScrollbarBg, background_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ScrollbarGrab, text_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ScrollbarGrabHovered, text_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_ScrollbarGrabActive, text_color, category=dpg.mvThemeCat_Core
            )
            dpg.add_theme_color(
                dpg.mvThemeCol_TitleBgActive, button_color, category=dpg.mvThemeCat_Core
            )