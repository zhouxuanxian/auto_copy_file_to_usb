#!/bin/bash

service_name="usb-autorun.service"

# 停止并禁用服务
sudo systemctl stop $service_name
sudo systemctl disable $service_name

# 删除服务文件
sudo rm /etc/systemd/system/$service_name

# 重新加载 systemd
sudo systemctl daemon-reload


# 重新加载 udev 规则
sudo udevadm control --reload-rules
