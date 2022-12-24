sudo apt -y install openbox plank rofi tint2 xcompmgr 
sudo apt -y install blueman network-manager
sudo apt -y install firefox thunar gnome-icon-theme-full gnome-terminal
sudo apt -y install python-tk
sudo apt -y install python3-tk

sudo rm -r /usr/share/openbox_config_menu
sudo cp -R ./config_menu /usr/share/openbox_config_menu

sudo rm /usr/share/applications/openbox_config_menu.desktop
sudo touch  /usr/share/applications/openbox_config_menu.desktop
sudo cat <<EOT >> /usr/share/applications/openbox_config_menu.desktop
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=python3 /usr/share/openbox_config_menu/config_menu/menu.py
Name=openbox config menu
Icon=/usr/share/openbox_config_menu/config_menu/config_icon.png
EOT
