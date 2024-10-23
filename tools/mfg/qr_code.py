import os
from os import path
import sys
import webbrowser

display_qrcode = True

def set_display_qrcode(value):
    global display_qrcode
    display_qrcode = value

def display_qrcode_web(url):
    if display_qrcode == True:
        webbrowser.open_new_tab(url)
