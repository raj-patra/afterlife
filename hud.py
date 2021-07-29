#!/usr/bin/python
import random, string, time, psutil, GPUtil, os

from tkinter import *
from constants import *
from callbacks import *

THEME = 'dark_blue'


class HUD:
    def __init__(self):
        self.left = Frame(root)
        self.right = Frame(root)
        self.intro = Frame(self.left)
        self.details = Frame(self.right, height=1)

        self.commands = Frame(self.right, width=80,
                                height=50, bg=theme[THEME]['root'], padx=10, pady=10)

        self.commands_r1 = Frame(self.commands, bg=theme[THEME]['root'])
        self.commands_r2 = Frame(self.commands, bg=theme[THEME]['root'])
        self.commands_r3 = Frame(self.commands, bg=theme[THEME]['root'])
        self.commands_r4 = Frame(self.commands, bg=theme[THEME]['root'])
        
        self.primary = Text(self.left, bg=theme[THEME]['primary'], 
                            fg=theme[THEME]['fg'], font=('ebrima', 8), width=60)

        self.welcome = Text(self.intro, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], width=30, height=2, 
                            font=('noto mono', 13, 'bold'), padx=20, 
                            pady=20, wrap=WORD)

        self.agenda = Text(self.intro, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], width=25, height=2, 
                            font=('noto mono', 13, 'bold'), wrap=WORD, 
                            insertbackground="white", padx=18, pady=20)

        
        self.clock = Label(self.right, bg=theme[THEME]['primary'], 
                            fg=theme[THEME]['fg'], height=2, width=20, 
                            font=('cursed timer ulil', 18, 'bold'))


        self.cmd = Button(self.commands_r1, text="CMD", font=('noto mono', 15), command=cmd, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.bash = Button(self.commands_r1, text="Bash", font=('noto mono', 15), command=bash, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.powershell = Button(self.commands_r1, text="Powershell", font=('noto mono', 15), command=powershell, height=2, width=10, relief=GROOVE,  overrelief=GROOVE, bg=theme[THEME]['primary'],  fg=theme[THEME]['fg'])

        self.browser = Button(self.commands_r2, text="Browser", font=('noto mono', 15), command=browser, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.github = Button(self.commands_r2, text="Github", font=('noto mono', 15), command=github, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.youtube = Button(self.commands_r2, text="Youtube", font=('noto mono', 15), command=youtube, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])

        self.docs = Button(self.commands_r3, text="Google Docs", font=('noto mono', 15), command=gdocs, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.sheets = Button(self.commands_r3, text="Google Sheets", font=('noto mono', 15), command=gsheets, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.slides = Button(self.commands_r3, text="Google Slides", font=('noto mono', 15), command=gslides, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        
        self.insta = Button(self.commands_r4, text="Instagram", font=('noto mono', 15), command=insta, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.reddit = Button(self.commands_r4, text="Reddit", font=('noto mono', 15), command=reddit, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        self.linkedin = Button(self.commands_r4, text="Linkedin", font=('noto mono', 15), command=linkedin, height=2, width=10, relief=GROOVE, overrelief=GROOVE, bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
        

        self.network = Text(self.details, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], height=5, width=25, 
                            font=('noto mono', 12), padx=20)

        self.misc = Text(self.details, bg=theme[THEME]['secondary'], 
                        fg=theme[THEME]['fg'], height=5, width=25, 
                        font=('noto mono', 12), padx=20)

        self.pack()
        self.initiate()

    def pack(self):
        self.left.pack(side=LEFT, fill=BOTH, expand=1)
        self.right.pack(side=RIGHT, fill=BOTH, expand=1)

        self.intro.pack(side=TOP, fill=BOTH, expand=1)
        self.primary.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.welcome.pack(side=LEFT, fill=BOTH, expand=1)
        self.agenda.pack(side=RIGHT, fill=BOTH, expand=1)

        self.clock.pack(side=TOP, fill=BOTH, expand=1)
        self.details.pack(side=TOP, fill=BOTH, expand=1)
        self.commands.pack(side=TOP, fill=BOTH, expand=1)
        # self.api.pack(side=TOP, fill=BOTH, expand=1)

        self.commands_r1.pack(side=TOP, fill=BOTH, expand=1)
        self.commands_r2.pack(side=TOP, fill=BOTH, expand=1)
        self.commands_r3.pack(side=TOP, fill=BOTH, expand=1)
        self.commands_r4.pack(side=TOP, fill=BOTH, expand=1)

        self.network.pack(side=RIGHT, fill=BOTH, expand=1)
        self.misc.pack(side=LEFT, fill=BOTH, expand=1)


        self.cmd.pack(side=LEFT, fill=BOTH, expand=1)
        self.bash.pack(side=LEFT, fill=BOTH, expand=1)
        self.powershell.pack(side=LEFT, fill=BOTH, expand=1)

        self.browser.pack(side=LEFT, fill=BOTH, expand=1)
        self.github.pack(side=LEFT, fill=BOTH, expand=1)
        self.youtube.pack(side=LEFT, fill=BOTH, expand=1)

        self.docs.pack(side=LEFT, fill=BOTH, expand=1)
        self.sheets.pack(side=LEFT, fill=BOTH, expand=1)
        self.slides.pack(side=LEFT, fill=BOTH, expand=1)

        self.insta.pack(side=LEFT, fill=BOTH, expand=1)
        self.reddit.pack(side=LEFT, fill=BOTH, expand=1)
        self.linkedin.pack(side=LEFT, fill=BOTH, expand=1)
        

    def initiate(self):
        self.welcome.insert(END, WELCOME.strip())
        self.welcome.config(state=DISABLED)

        self.agenda.insert(END, "Type your agenda here:")
        # self.api.insert(END, FUN.strip().format(requests.get(FACTS_API).json()['text']))
        self.clock.config(text = time.strftime(" %I:%M %p | %A %n %d %B %Y", time.localtime()))
        
        self.network.insert(END, NETWORK)
        self.network.config(state=DISABLED)

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()[2]
        gpu = GPUtil.getGPUs()
        battery = psutil.sensors_battery()
        self.misc.insert(END, MISC.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                            battery.percent, "Plugged In" if battery.power_plugged else "Not Plugged In"))
        self.misc.config(state=DISABLED)
    
        self.recursive()

    def recursive(self):
        def loop():
            global start, update
            
            if (time.time()-update) > 60:
                update = time.time()

                # self.api.delete('1.0', END)
                # self.api.insert(END, FUN.strip().format(requests.get(FACTS_API).json()['text']))

                self.clock.config(text = time.strftime(" %I:%M %p | %A %n %d %B %Y", time.localtime()))

                
            if (time.time()-start) > 10:
                start = time.time()
                self.primary.delete('1.0', END)

                self.misc.config(state=NORMAL)
                self.misc.delete('1.0', END)
                cpu = psutil.cpu_percent()
                ram = psutil.virtual_memory()[2]
                gpu = GPUtil.getGPUs()
                battery = psutil.sensors_battery()
                self.misc.insert(END, MISC.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                                    battery.percent, "Plugged In" if battery.power_plugged else "Not Plugged In"))
                self.misc.config(state=DISABLED)
            
            self.primary.insert(CURRENT, ''.join(random.choice(string.printable)))
            self.primary.after(2, loop)

        loop()


if __name__ == '__main__':
    root = Tk()
    root.config(bg=theme[THEME]['root'], bd=5)
    root.resizable(1, 1)
    root.title("Afterlife")

    start = time.time()
    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()