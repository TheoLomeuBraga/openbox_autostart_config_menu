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

    def print_info(self):
        print("walpaper "+str(self.walpaper))
        print("window_compositor "+str(self.window_compositor))
        print("taskbar "+str(self.taskbar))
        print("dock "+str(self.dock))
        print("network_applet "+str(self.network_applet))
        print("audio_applet "+str(self.audio_applet))
        print("bluetooth_applet "+str(self.bluetooth_applet))

    def get(self):
        self.walpaper = bool(walpaper_cb_var.get())
        self.window_compositor = bool(window_compositor_cb_var.get())
        self.taskbar = bool(taskbar_cb_var.get())
        self.dock = bool(dock_cb_var.get())
        self.network_applet = bool(network_applet_cb_var.get())
        self.audio_applet = bool(audio_applet_cb_var.get())
        self.bluetooth_applet = bool(bluetooth_applet_cb_var.get())
        self.print_info()

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
    os.system("cp -R ./config/nitrogen ~/.config/nitrogen")
    os.system("cp -R ./config/openbox ~/.config/openbox")
    os.system("cp -R ./config/plank ~/.config/plank")
    os.system("cp -R ./config/rofi ~/.config/rofi")
    os.system("cp -R ./config/tint2 ~/.config/tint2")

#delete_configs()
#move_configs()

ob_conf = openbox_config()

window = Tk() 
window.title('openbox config')
window.geometry("300x300")




frame = Frame(window)
frame.pack( side = TOP )

Label( frame, text="openbox config menu:" ).pack( side = TOP )

#walpaper_cb
walpaper_cb_var = IntVar()
walpaper_cb = Checkbutton(frame, text='walpaper',variable=walpaper_cb_var, onvalue=1, offvalue=0,command=ob_conf.get)
walpaper_cb.select()
walpaper_cb.pack( side = TOP )

#window_compositor_cb
window_compositor_cb_var = IntVar()
window_compositor_cb = Checkbutton(frame, text='window compositor',variable=window_compositor_cb_var, onvalue=1, offvalue=0,command=ob_conf.get)
window_compositor_cb.select()
window_compositor_cb.pack( side = TOP )

#taskbar_cb
taskbar_cb_var = IntVar()
taskbar_cb = Checkbutton(frame, text='taskbar',variable=taskbar_cb_var, onvalue=1, offvalue=0,command=ob_conf.get)
taskbar_cb.select()
taskbar_cb.pack( side = TOP )

#dock_cb
dock_cb_var = IntVar()
dock_cb = Checkbutton(frame, text='dock',variable=dock_cb_var, onvalue=1, offvalue=0,command=ob_conf.get)
dock_cb.select()
dock_cb.pack( side = TOP )

#network_applet_cb
network_applet_cb_var = IntVar()
network_applet_cb = Checkbutton(frame, text='network applet',variable=network_applet_cb_var, onvalue=1, offvalue=0,command=ob_conf.get)
network_applet_cb.select()
network_applet_cb.pack( side = TOP )

#audio_applet_cb
audio_applet_cb_var = IntVar()
audio_applet_cb = Checkbutton(frame, text='audio applet',variable=audio_applet_cb_var, onvalue=1, offvalue=0,command=ob_conf.get)
audio_applet_cb.select()
audio_applet_cb.pack( side = TOP )

#bluetooth_applet_cb
bluetooth_applet_cb_var = IntVar()
bluetooth_applet_cb = Checkbutton(frame, text='bluetooth applet',variable=bluetooth_applet_cb_var, onvalue=1, offvalue=0,command=ob_conf.get)
bluetooth_applet_cb.select()
bluetooth_applet_cb.pack( side = TOP )


Button(frame,text='applay',command=ob_conf.save).pack( side = TOP )




window.mainloop()
