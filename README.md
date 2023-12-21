### auto_copy_file_to_usb

1. usb-autorun.service修改 python脚本为当前系统的文件路径

2. usb_copy_script.py 修改需要拷贝的源目录source_folder

3. sudo ./start_autorun.sh 注册自动检测U盘并且配置执行python脚本

4. journalctl -fu usb-autorun.service 打印日志，测试自动检测U盘并且拷贝文件生效
