import  os, webbrowser, wikipedia

from tkinter import messagebox
import helpers.constants as constants
import subprocess as sp

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def universal_callback(command=None, web=None):
    if command:
        if command.startswith('start'):
            os.system("{}".format(command))

        if command.startswith('subprocess'):
            process = command.split(' ', 1)[-1]
            response = sp.getoutput(process)
            return response
    
    if web:
        if web.startswith('search'):
            url = "https://duckduckgo.com/?q={}".format(web.split(' ', 1)[-1].strip())
            webbrowser.get('edge').open(url)

        elif web.startswith('url'):
            web = web.split(' ', 1)[-1]
            webbrowser.get('edge').open(web)

        elif web.startswith('wiki'):
            web = web.split(' ', 1)[-1]
            query = ''.join(web.split(' '))
            try:
                page = wikipedia.page(query)
                return {
                "title": page.title,
                "url": page.url,
                "summary": page.summary
            }
            except Exception:
                return {
                "title": "Error Occured",
                "url": "https://en.wikipedia.org/wiki/{}".format(query),
                "summary": "Error Occured in fetching the article. Please make sure the search query does not have special characters except for whitespaces.\n\nTry again maybe?\nIf the issue presists, try any other combination for the search query."
            }

def about(event=None):
    messagebox.showinfo('About', constants.ABOUT)

def destroy(root):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
