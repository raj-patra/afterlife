import  os, webbrowser, requests

from tkinter import messagebox
from helpers.constants import *

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def universal_callback(command=None, url=None):
    if command:
        if command.startswith('start'):
            os.system("{}".format(command))

        if command.startswith('subprocess'):
            process = command.split(' ', 1)[-1]
            response = sp.getoutput(process)
            return response
    
    if url:
        url = url.split(' ', 1)[-1]
        webbrowser.get('edge').open(url)

def about():
    messagebox.showinfo('About', ABOUT)

def destroy(root):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()