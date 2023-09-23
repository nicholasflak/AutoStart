import subprocess
import os
import time
import socket
import psutil

# Get the current working directory
current_directory = os.getcwd()

# Name of the .exe file you want to execute
exe_filename = "Aki.Server.exe"  # Replace with your .exe file's name
exe_filename2 = "Aki.Launcher.exe"
# Construct the full path to the .exe file
exe_path = os.path.join(current_directory, exe_filename)
exe_path2 = os.path.join(current_directory, exe_filename2)


def is_port_open(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect(("localhost", port))
        return True
    except (ConnectionRefusedError, TimeoutError):
        return False


try:
    first_program_process = subprocess.Popen(exe_filename)
except FileNotFoundError:
    exit()

while not is_port_open(6969):
    time.sleep(1)

try:
    subprocess.Popen(exe_filename2)
except FileNotFoundError:
    pass
