sudo apt -y install openbox plank rofi tint2 xcompmgr pcmanfm nitrogen spacefm
sudo apt -y install blueman network-manager
sudo apt -y install firefox gnome-terminal
sudo apt -y install gnome-icon-theme-full
sudo apt -y install python-tk
sudo apt -y install python3-tk

sudo rm -r /usr/share/openbox_autostart_config_menu
sudo cp -R ./config_menu /usr/share/openbox_autostart_config_menu
sudo rm /usr/share/applications/openbox_autostart_config_menu.desktop
sudo touch  /usr/share/applications/openbox_autostart_config_menu.desktop
echo "[Desktop Entry]" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Encoding=UTF-8" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Version=1.0" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Type=Application" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Terminal=false" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Exec=python3 /usr/share/openbox_autostart_config_menu/menu.py" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Path=/usr/share/openbox_autostart_config_menu/" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Type=Application" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Name=openbox autostart configurations menu" >> /usr/share/applications/openbox_autostart_config_menu.desktop
echo "Icon=/usr/share/openbox_autostart_config_menu/config_icon.png" >> /usr/share/applications/openbox_autostart_config_menu.desktop


sudo rm -r /usr/share/openbox_config_center
sudo cp -R ./config_center /usr/share/openbox_config_center
sudo rm /usr/share/applications/openbox_config_center.desktop
sudo touch  /usr/share/applications/openbox_config_center.desktop
echo "[Desktop Entry]" >> /usr/share/applications/openbox_config_center.desktop
echo "Encoding=UTF-8" >> /usr/share/applications/openbox_config_center.desktop
echo "Version=1.0" >> /usr/share/applications/openbox_config_center.desktop
echo "Type=Application" >> /usr/share/applications/openbox_config_center.desktop
echo "Terminal=false" >> /usr/share/applications/openbox_config_center.desktop
echo "Exec=python3 /usr/share/openbox_config_center/center.py" >> /usr/share/applications/openbox_config_center.desktop
echo "Path=/usr/share/openbox_config_center/" >> /usr/share/applications/openbox_config_center.desktop
echo "Type=Application" >> /usr/share/applications/openbox_config_center.desktop
echo "Name=openbox configurations center" >> /usr/share/applications/openbox_config_center.desktop
echo "Icon=/usr/share/openbox_config_center/config_icon.png" >> /usr/share/applications/openbox_config_center.desktop





rm -r ~/.config/nitrogen
rm -r ~/.config/spacefm
rm -r ~/.config/openbox
rm -r ~/.config/plank
rm -r ~/.config/rofi
rm -r ~/.config/tint2
sudo rm -r /usr/share/themes/Nightmare-02-improved



cp -R ./config_menu/config/nitrogen ~/.config
cp -R ./config_menu/config/spacefm ~/.config
cp -R ./config_menu/config/openbox ~/.config
cp -R ./config_menu/config/plank ~/.config
cp -R ./config_menu/config/rofi ~/.config
cp -R ./config_menu/config/tint2 ~/.config
