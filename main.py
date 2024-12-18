################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema:
#
# Lihtne muusikamängija kasutades pygame, dearpygui ja tkinteri teeke
# Proovime lisada playlistide, equalizeri ja ka pealkirjast metaandmete
# võtmise funktsioonid. See on esialgne plaan, aga kui peaksime hoogu sattuma, teeme rohkem
# Praegu on GUI väga kole, aga loodetavasti teeme selle talutavaks
#
# Autorid:
# Madis Miikael Arro
# Artur Üleoja
#
# mõningane eeskuju:
#
# Puudub, teeme tunde järgi
#
# Lisakommentaar (nt käivitusjuhend):
#
# Jooksuta main.py fail
##################################################
import gui.gui as gui
import player.player as player
import threading

if __name__ == "__main__":
    # Loob uue threadi, et paralleelselt gui haldamisega mängida playlistist lugusid
    threading.Thread(target=player.is_playing, daemon=True).start()

    gui.create_gui()
