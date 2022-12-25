sudo apt -y install openbox plank rofi tint2 xcompmgr 
sudo apt -y install blueman network-manager
sudo apt -y install firefox thunar gnome-terminal
sudo apt -y install gnome-icon-theme-full
sudo apt -y install python-tk
sudo apt -y install python3-tk

sudo rm -r /usr/share/openbox_config_menu
sudo cp -R ./config_menu /usr/share/openbox_config_menu

sudo rm /usr/share/applications/openbox_config_menu.desktop
sudo touch  /usr/share/applications/openbox_config_menu.desktop

echo "[Desktop Entry]" >> /usr/share/applications/openbox_config_menu.desktop
echo "Encoding=UTF-8" >> /usr/share/applications/openbox_config_menu.desktop
echo "Version=1.0" >> /usr/share/applications/openbox_config_menu.desktop
echo "Type=Application" >> /usr/share/applications/openbox_config_menu.desktop
echo "Terminal=true" >> /usr/share/applications/openbox_config_menu.desktop
echo "Exec=python3 /usr/share/openbox_config_menu/menu.py" >> /usr/share/applications/openbox_config_menu.desktop
echo "Path=/usr/share/openbox_config_menu/" >> /usr/share/applications/openbox_config_menu.desktop
echo "Type=Application" >> /usr/share/applications/openbox_config_menu.desktop
echo "Name=openbox config menu" >> /usr/share/applications/openbox_config_menu.desktop
echo "Icon=/usr/share/openbox_config_menu/config_menu/config_icon.ico" >> /usr/share/applications/openbox_config_menu.desktop




rm -r ~/.config/nitrogen
rm -r ~/.config/openbox
rm -r ~/.config/plank
rm -r ~/.config/rofi
rm -r ~/.config/tint2


cp -R ./config/nitrogen ~/.config/nitrogen
cp -R ./config/openbox ~/.config/openbox
cp -R ./config/plank ~/.config/plank
cp -R ./config/rofi ~/.config/rofi
cp -R ./config/tint2 ~/.config/tint2
