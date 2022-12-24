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
        os.system("rm ~/.config/openbox/autostart")
        os.system("touch ~/.config/openbox/autostart")
        if self.walpaper :
            os.system('echo "nitrogen --restore &" >> ~/.config/openbox/autostart')
        if self.window_compositor :
            os.system('echo "xcompmgr -t5 -l5 -r4.2 -o.55  &" >> ~/.config/openbox/autostart')
        if self.taskbar :
            os.system('echo "tint2 &" >> ~/.config/openbox/autostart')
        if self.dock :
            os.system('echo "plank &" >> ~/.config/openbox/autostart')
        if self.network_applet :
            os.system('echo "nm-applet &" >> ~/.config/openbox/autostart')
        if self.audio_applet :
            os.system('echo "pnmixer &" >> ~/.config/openbox/autostart')
        if self.bluetooth_applet :
            os.system('echo "blueman-applet &" >> ~/.config/openbox/autostart')
        

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