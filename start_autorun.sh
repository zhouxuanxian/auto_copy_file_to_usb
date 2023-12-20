sudo cp ./99-usb-autorun.rules /etc/udev/rules.d/99-usb-autorun.rules
sudo cp ./usb-autorun.service /etc/systemd/system/usb-autorun.service
sudo udevadm control --reload-rules
systemctl start usb-autorun.service
