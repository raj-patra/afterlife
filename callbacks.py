import  os, webbrowser, requests, wikipedia, random

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
        if web.startswith('url'):
            web = web.split(' ', 1)[-1]
            webbrowser.get('edge').open(web)
        
        if web.startswith('request'):
            url = web.split(' ', 1)[-1]

            if url == 'quote':
                response = requests.get(constants.QUOTE_API).json()
                return "{} \n\n- {}".format(response['content'], response['author'])

            if url == 'fact':
                response = requests.get(constants.FACTS_API).json()
                return "Did you know, \n\n{}".format(response['text'])

            if url == 'poem':
                response = random.choice(requests.get(constants.POEMS_API).json())
                return "{} \n\n{} \n\nBy {}".format(response['title'], response['content'], response['poet']['name'])

            if url == 'insult':
                response = requests.get(constants.INSULT_API).json()
                return "{}".format(response['insult'])

            if url == 'kanye':
                response = requests.get(constants.KANYE_API).json()
                return "Kanye REST once said, \n\n*{}*".format(response['quote'])

        if web.startswith('wiki'):
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
                "url": "NA",
                "summary": "Error Occured in fetching the article. Please make sure the search query does not have special characters except for whitespaces.\n\nTry again maybe?\nIf the issue presists, try any other combination for the search query."
            }
            

def about(event=None):
    messagebox.showinfo('About', constants.ABOUT)

def destroy(root):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()