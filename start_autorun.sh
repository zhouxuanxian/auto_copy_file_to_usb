sudo cp -f ./99-usb-autorun.rules /etc/udev/rules.d/99-usb-autorun.rules
sudo cp -f ./usb-autorun.service /etc/systemd/system/usb-autorun.service
sudo udevadm control --reload-rules
sudo systemctl start usb-autorun.service
