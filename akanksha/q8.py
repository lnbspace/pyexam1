import subprocess
devices= subprocess.check_output(['netsh','wlan','show','network'])
devices=devices.decode('ascii')
devices=devices.replace("\r","")
print(devices)
