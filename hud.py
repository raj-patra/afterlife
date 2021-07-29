#!/usr/bin/python
import random, string, time, psutil, GPUtil

from tkinter import *
from constants import *

THEME = 'dark_blue'


class HUD:
    def __init__(self):
        self.left = Frame(root)
        self.right = Frame(root)
        self.intro = Frame(self.left)
        self.details = Frame(self.right)
        
        self.primary = Text(self.left, bg=theme[THEME]['primary'], 
                            fg=theme[THEME]['fg'], font=('ebrima', 8), width=80)

        self.welcome = Text(self.intro, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], width=30, height=2, 
                            font=('noto mono', 13, 'bold'), padx=20, 
                            pady=20, wrap=WORD)

        self.agenda = Text(self.intro, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], width=35, height=2, 
                            font=('noto mono', 13, 'bold'), wrap=WORD, 
                            insertbackground="white", padx=20, pady=20)

        
        self.clock = Label(self.right, bg=theme[THEME]['primary'], 
                            fg=theme[THEME]['fg'], height=2, width=20, 
                            font=('cursed timer ulil', 20, 'bold'))

        self.api = Text(self.right, bg=theme[THEME]['secondary'], 
                        fg=theme[THEME]['fg'], font=('noto mono', 10))

        self.network = Text(self.details, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], height=5, width=20, 
                            font=('noto mono', 12), padx=20)

        self.misc = Text(self.details, bg=theme[THEME]['secondary'], 
                        fg=theme[THEME]['fg'], height=5, width=20, 
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
        self.api.pack(side=TOP, fill=BOTH, expand=1)

        self.network.pack(side=RIGHT, fill=BOTH, expand=1)
        self.misc.pack(side=LEFT, fill=BOTH, expand=1)

    def initiate(self):
        self.welcome.insert(END, WELCOME.strip())
        self.welcome.config(state=DISABLED)

        self.agenda.insert(END, "Type your agenda here:")
        self.api.insert(END, FUN.strip().format(requests.get(FACTS_API).json()['text']))
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

                self.api.delete('1.0', END)
                self.api.insert(END, FUN.strip().format(requests.get(FACTS_API).json()['text']))

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