import uuid
import psutil
import os

def menu():
        strs = ('Enter 1 get the MAC address\n'
                'Enter 2 get the RAM and CPU details.\n'
                'Enter 3 get the OS information\n'
                'Enter 4 to exit : ')
        choice = raw_input(strs)
        return int(choice) 

while True:          
    choice = menu()
    if choice == 1:
        print (hex(uuid.getnode()))
    elif choice == 2:
        print('The CPU usage is: ', psutil.cpu_percent(4))
    elif choice == 3:
        os_info = os.uname()
        print(os_info) 
    elif choice == 4:
        break