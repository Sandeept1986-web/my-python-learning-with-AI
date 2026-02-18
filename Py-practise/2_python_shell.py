import sys
#print("Python version", sys.api_version)
print("Python version", sys.version_info)
print("Python version", sys.version)
#shell command
# python --version

import os
print("Current Username:", os.getlogin())
print("current working directory:", os.getcwd())
print("Python version", os.popen('python --version').read().strip( ))

#shell command
# whoami

import psutil
print("CPU Count:", psutil.cpu_count(logical=True))
print("Total Memory (in GB):", round(psutil.virtual_memory().total / (1024**3), 2))
print("Available Memory (in GB):", round(psutil.virtual_memory().available / (1024**3), 2))
print("Used Memory (in GB):", round(psutil.virtual_memory().used / (1024**3), 2))
print("Memory Percentage:", psutil.virtual_memory().percent)

#shell command
#nproc
#vmstat
#top

import time
import datetime
boot_time_timestamp = psutil.boot_time()
bt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_time_timestamp))
print("Boot Time:", bt)
print(datetime.datetime.now())
print("*" * 50) # scalar multiplication

#shell command
#uptime

import subprocess

# Run the shell command 'dir' and capture the output
result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(result.stdout)


#shell command
#ls -l