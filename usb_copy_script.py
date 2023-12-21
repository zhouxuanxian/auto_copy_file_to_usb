import os
import shutil
import subprocess
import platform
import glob
import time

def identify_usb_drives():
    if platform.system() == 'Windows':
        drives = [drive[0] for drive in os.popen('wmic logicaldisk get caption').read().split('\n')[1:] if drive]
        usb_drives = [drive for drive in drives if os.path.exists(os.path.join(drive, 'VolumeInformation'))]
    elif platform.system() == 'Linux':
        usb_drives = [drive for drive in glob.glob('/media/*/*') if os.path.ismount(drive)]
    else:
        print("Unsupported operating system.")
        return []

    return usb_drives

def rename_usb(usb_drive, new_name):
    if platform.system() == 'Linux':
        
        # Get the device file associated with the mount point
        device_path = subprocess.check_output(['df', '--output=source', usb_drive]).decode('utf-8').split('\n')[1]

        # Unmount the USB drive
        subprocess.run(['umount', usb_drive])
        
        # Format the device file using mkfs.vfat
        subprocess.run(['mkfs.vfat', '-n', new_name, device_path])

        usb_drive = usb_drive.replace(os.path.basename(usb_drive), new_name)

        # Mount the USB drive
        subprocess.run(['mkdir', '-p', usb_drive])

        subprocess.run(['sudo', 'mount', device_path, usb_drive])

        return usb_drive
    else:
        print("Unsupported operating system.")
        return

def copy_folder(source_folder, usb_drive):

    
    # Copy the folder to the USB drive
    # destination_folder = os.path.join(usb_drive, os.path.basename(source_folder))
    shutil.copytree(source_folder, usb_drive, dirs_exist_ok=True)
    

def main():
    source_folder = '/home/xuanxianzhou/Desktop/auto_copy_file_to_usb/app'
    new_name = 'PVMED'
    usb_drives = identify_usb_drives()
    if not usb_drives:
        print("No USB drives found.")
        return

    for usb_drive in usb_drives:
        start_time = time.time()
        # usb_drive = rename_usb(usb_drive, new_name)
        print('usb_drive:', usb_drive)
        copy_folder(source_folder, usb_drive)
        subprocess.run(['umount', usb_drive])
        end_time = time.time()
        # 计算函数执行时间
        execution_time = end_time - start_time
        print(f'----------格式化并且拷贝文件完成, 耗时：{execution_time:.2f} seconds----------')
    # subprocess.run(["paplay", "--volume=32768", "--latency-msec=1500", "/home/xuanxianzhou/auto_copy_to_usb/5809.wav"])
    # os.system("paplay --volume=32768 --latency-msec=1 /usr/share/sounds/freedesktop/stereo/complete.oga")

if __name__ == "__main__":
    main()
    

