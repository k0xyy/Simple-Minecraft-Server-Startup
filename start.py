import os
import sys
from sys import platform
from subprocess import call

if platform == "linux" or platform == "linux2":
    os.system('clear')

if platform == "linux" or platform == "linux2":
    terminal_title = "Made by: k0xyy on GitHub"
    print(f'\33]0;{terminal_title}\a', end='', flush=True)


print("Simple yet 1337 AF Minecraft Server Launcher\n")
print("   [1] Launch Existing Minecraft Server With Ngrok\n")
print("   [2] Launch Existing Minecraft Server\n")
option = int(input(">>> "))

if option == 1:

    if platform == "linux" or platform == "linux2":
        os.system('clear')

    mem_option_ngrok = str(input("\n   How Much Memory(Mb)?\n\n>>> "))
    mem_option_ngrok_check = str(input("\n   Are you sure you want to give this server " + mem_option_ngrok + "Mb of Memory? (Y/n)\n\n>>> "))

    if mem_option_ngrok_check == "y" or "Y":

        if platform == "linux" or platform == "linux2":
            os.system('clear')

        if platform == "linux" or platform == "linux2":
            call(["gnome-terminal", "-x", "sh", "-c", "sudo ngrok tcp 25565; bash"])
        elif platform == "win32":
            call('start ngrok.exe tcp 25565', shell=True)

        if platform == "linux" or platform == "linux2":
            terminal_title2 = "MC Server"
            print(f'\33]0;{terminal_title2}\a', end='', flush=True)
        
        if platform == "linux" or platform == "linux2":
            os.system('sudo java -Xmx' + mem_option_ngrok + 'M -Xms' + mem_option_ngrok + 'M -jar server.jar nogui')
        elif platform == "win32":
            os.system('java -Xmx' + mem_option_ngrok + 'M -Xms' + mem_option_ngrok + 'M -jar server.jar')

    if mem_option_ngrok_check == "n" or "N":

        if platform == "linux" or platform == "linux2":
            os.system('clear')

        mem_option_ngrok = str(input("\n   How Much Memory(Mb)?\n\n>>> "))

        if platform == "linux" or platform == "linux2":
            call(["gnome-terminal", "-x", "sh", "-c", "sudo ngrok tcp 25565; bash"])
        elif platform == "win32":
            call('start ngrok.exe tcp 25565', shell=True)

        if platform == "linux" or platform == "linux2":
            terminal_title2 = "MC Server"
            print(f'\33]0;{terminal_title2}\a', end='', flush=True)

        if platform == "linux" or platform == "linux2":
            os.system('sudo java -Xmx' + mem_option_ngrok + 'M -Xms' + mem_option_ngrok + 'M -jar server.jar nogui')
        elif platform == "win32":
            os.system('java -Xmx' + mem_option_ngrok + 'M -Xms' + mem_option_ngrok + 'M -jar server.jar')

if option == 2:

    if platform == "linux" or platform == "linux2":
        os.system('clear')

    mem_option = str(input("\n   How Much Memory(Mb)?\n\n>>> "))
    mem_option_check = str(input("\n   Are you sure you want to give this server " + mem_option + "Mb of Memory? (Y/n)\n\n>>> "))

    if mem_option_check == "y" or "Y":

        if platform == "linux" or platform == "linux2":
            os.system('clear')

        if platform == "linux" or platform == "linux2":
            terminal_title2 = "MC Server"
            print(f'\33]0;{terminal_title2}\a', end='', flush=True)

        if platform == "linux" or platform == "linux2":
            os.system('sudo java -Xmx' + mem_option + 'M -Xms' + mem_option + 'M -jar server.jar nogui')
        elif platform == "win32":
            os.system('java -Xmx' + mem_option + 'M -Xms' + mem_option + 'M -jar server.jar')

    if mem_option_check == "n" or "N":

        if platform == "linux" or platform == "linux2":
            os.system('clear')

        mem_option = str(input("\n   How Much Memory(Mb)?\n\n>>> "))

        if platform == "linux" or platform == "linux2":
            terminal_title2 = "MC Server"
            print(f'\33]0;{terminal_title2}\a', end='', flush=True)
        
        if platform == "linux" or platform == "linux2":
            os.system('sudo java -Xmx' + mem_option + 'M -Xms' + mem_option + 'M -jar server.jar nogui')
        elif platform == "win32":
            os.system('java -Xmx' + mem_option + 'M -Xms' + mem_option + 'M -jar server.jar')


