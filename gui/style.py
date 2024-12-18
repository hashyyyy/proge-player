import dearpygui.dearpygui as dpg

def load_themes():
    button_color = [102, 153, 204]
    button_hover_color = [128, 179, 255]
    background_color = [25, 25, 25]
    text_color = [255, 255, 255] 
    slider_color = [153, 204, 255]

    with dpg.theme(tag='app_theme'):
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, background_color, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, text_color, category=dpg.mvThemeCat_Core)

    with dpg.theme(tag='button_theme'):
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, button_color, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, button_hover_color, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, button_color, category=dpg.mvThemeCat_Core)

    with dpg.theme(tag='slider_theme'):
        with dpg.theme_component():
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, slider_color, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, slider_color, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 10, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
   
