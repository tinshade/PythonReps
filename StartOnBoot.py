"""
Adding Script to Boot with Windows

Author: Abhishek Iyengar
GitHub: tinshade
YouTube: Annoying Errors

This script is a module that can be added to a main code that needs to boot with the Windows OS.
This simply adds the script's path to the registry that is in-charge of botting startup applications when Windows boots up.

"""

import os,sys #To identify path and string formatting with slashes
import winreg as reg #To add registry keys

#Function to start script on Windows boot
def addStartup():  
    fp = os.path.dirname(os.path.realpath(__file__)) #Getting the real path to the current script
    file_name = sys.argv[0].split('\\')[-1] #Formatting the path to get the filename
    new_file_path = fp + '\\' + file_name #Generating new file path
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run' #2nd half of registry key in Registry Editor
    key2change = reg.OpenKey(reg.HKEY_CURRENT_USER, keyVal, 0, reg.KEY_ALL_ACCESS) #Adding keys with 1st and 2nd halves of the registry
    reg.SetValueEx(key2change, 'PresenceAutoShut', 0, reg.REG_SZ,new_file_path) #Setting path in the registry and finishing the addition


addStartup()