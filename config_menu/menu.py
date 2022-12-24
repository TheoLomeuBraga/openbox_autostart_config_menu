import os
from tkinter import *

class openbox_config:
    def __init__(self):
        self.walpaper = True
        self.window_compositor = True
        self.taskbar = True
        self.dock = True
        self.network_applet = True
        self.audio_applet = True
        self.bluetooth_applet = True
    def save(self):
        print("")

def delete_configs():
    os.system("rm -r ~/.config/nitrogen")
    os.system("rm -r ~/.config/openbox")
    os.system("rm -r ~/.config/plank")
    os.system("rm -r ~/.config/rofi")
    os.system("rm -r ~/.config/tint2")

def move_configs():
    os.system("cp -R config/nitrogen ~/.config/nitrogen")
    os.system("cp -R config/openbox ~/.config/openbox")
    os.system("cp -R config/plank ~/.config/plank")
    os.system("cp -R config/rofi ~/.config/rofi")
    os.system("cp -R config/tint2 ~/.config/tint2")

delete_configs()
move_configs()

window = Tk() 