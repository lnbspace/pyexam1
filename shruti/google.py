import webbrowser
import time

url1 = input("Enter your web1: ")
url2 = input("Enter your web2: ")
url3 = input("Enter your web3: ")
 
webbrowser.open(url1) 
time.sleep(3) 
webbrowser.open_new_tab(url2) 
time.sleep(3) 
webbrowser.open_new_tab(url3) 
time.sleep(3) 