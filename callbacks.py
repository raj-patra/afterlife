import GPUtil
import locale
import os
import psutil
import subprocess as sp
import webbrowser
from tkinter import messagebox

import wikipedia

import helpers.constants as constants

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

# Get local language code for wikipedia articles
lang_code = locale.getdefaultlocale()[0].split('_')[0]

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
                wikipedia.set_lang(lang_code)
                page = wikipedia.page(query)
                return {
                    "title": page.title,
                    "url": page.url,
                    "summary": page.summary
            }
            except Exception:
                return {
                "title": "Error Occured",
                "url": "https://{lang_code}.wikipedia.org/wiki/{query}".format(lang_code=lang_code, query=query),
                "summary": "Error Occured in fetching the article. Please try any other combination for the search query."
            }

def pc_stats_callback():
    stats = dict(
        cpu_usage = psutil.cpu_percent(),
        ram_usage = psutil.virtual_memory().percent,
        battery_usage = psutil.sensors_battery().percent,
        battery_plugged = psutil.sensors_battery().power_plugged,
        gpu_name = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "No GPU found",
        gpu_usage = GPUtil.getGPUs()[0].memoryUtil*100 if GPUtil.getGPUs() else 0.0
    )

    return stats

def about(event=None):
    messagebox.showinfo('About', constants.ABOUT)

def destroy(root):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
