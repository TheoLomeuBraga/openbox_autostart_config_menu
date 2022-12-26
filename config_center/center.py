import sys
sys.path.append("/usr/share/openbox_config_center/")
import os
from tkinter import *



def open_openbox_configurations_menu():
    os.system("obconf %%f &")

def open_openbox_auto_start_configurations_menu():
    os.system("python3 /usr/share/config_center/center.py &")

def open_desktop_configurations_menu():
    os.system("pcmanfm --desktop-pref &")


ob_conf = openbox_config()

window = Tk() 
window.title('openbox config')
window.geometry("300x300")




frame = Frame(window)
frame.pack( side = TOP )

Label( frame, text="openbox configurations center:" ).pack( side = TOP )

#workspace_cb





window.mainloop()
