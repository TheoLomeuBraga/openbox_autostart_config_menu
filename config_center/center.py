import sys
sys.path.append("/usr/share/openbox_config_center/")
import os
from tkinter import *



def open_openbox_configurations_menu():
    os.system("obconf %%f &")

def open_openbox_auto_start_configurations_menu():
    os.system("python3 /usr/share/openbox_autostart_config_menu/menu.py &")

def open_desktop_configurations_menu():
    os.system("spacefm --desktop-pref &")




window = Tk() 
window.title('openbox config')
window.geometry("400x300")




frame = Frame(window)
frame.pack( side = TOP )

Label( frame, text="openbox configurations center:" ).pack( side = TOP )

Button(frame, text ="open openbox configurations menu", command=open_openbox_configurations_menu).pack( side = TOP )

Button(frame, text ="open openbox auto start configurations menu", command=open_openbox_auto_start_configurations_menu).pack( side = TOP )

Button(frame, text ="open desktop configurations menu", command=open_desktop_configurations_menu).pack( side = TOP )

#workspace_cb





window.mainloop()
