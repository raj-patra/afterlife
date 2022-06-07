import locale
import os
import subprocess as sp
import webbrowser
from tkinter import messagebox

import GPUtil
import psutil
import wikipedia
from application.helpers import constants

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

# Get local language code for wikipedia articles
lang_code = locale.getdefaultlocale()[0].split('_')[0]


def event_handler_callback(event: str=None, query: str=None):

    if event == "start_app":
        os.system(query)
        return None

    elif event == "execute_subprocess":
        response = sp.getoutput(query)
        return response

    elif event == "open_url":
        webbrowser.get('edge').open(query)
        return None

    elif event == "search_query":
        url = "https://duckduckgo.com/?q={}".format(query.strip())
        webbrowser.get('edge').open(url)
        return None

    elif event == "fetch_wiki":
        query = query.strip()
        try:
            wikipedia.set_lang(lang_code)
            page = wikipedia.page(query)
            return {
                "title": page.title,
                "url": page.url,
                "summary": page.summary,
                "error": False
            }
        except Exception:
            return {
                "title": "Error Occured",
                "url": "https://{lang_code}.wikipedia.org/wiki/{query}".format(lang_code=lang_code, query=query),
                "summary": "Error Occured in fetching the article. Seaching externally...",
                "error": True
            }

def pc_stats_callback():
    cpu = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    battery = psutil.sensors_battery()

    stats = dict(
        cpu_usage = cpu,

        virtual_memory_used = round(virtual_memory.used/1e9, 2),
        virtual_memory_total = round(virtual_memory.total/1e9, 2),
        virtual_memory_percent = virtual_memory.percent,

        disk_used = round(disk.used/1e12, 2),
        disk_total = round(disk.total/1e12, 2),
        disk_percent = disk.percent,

        battery_usage = battery.percent,
        battery_plugged = battery.power_plugged,

        boot_time = psutil.boot_time()
    )

    return stats

def about_dialog_callback():
    messagebox.showinfo('About', constants.ABOUT)

def destroy_root_callback(root):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def random_article_callback():
    try:
        return wikipedia.random(1)
    except Exception:
        return None
