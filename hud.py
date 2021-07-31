#!/usr/bin/python
import random, string, time, psutil, GPUtil, gc

from tkinter import *
from constants import *
from callbacks import *
from functools import partial

THEME = 'dark_blue'


class HUD:
    def __init__(self):
        self.left = Frame(root)
        self.right = Frame(root)
        self.intro = Frame(self.left)
        self.details = Frame(self.right, height=1)

        self.commands = Frame(self.right, width=80,
                                height=50, bg=theme[THEME]['root'], padx=5, pady=5)
        
        self.gibberish = Text(self.left, bg=theme[THEME]['primary'], 
                            fg=theme[THEME]['fg'], font=('ebrima', 8), width=60)

        self.welcome = Text(self.intro, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], width=30, height=2, 
                            font=('noto mono', 13, 'bold'), padx=20, 
                            pady=20, wrap=WORD)

        self.agenda = Text(self.intro, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], width=25, height=2, 
                            font=('noto mono', 13, 'bold'), wrap=WORD, 
                            insertbackground="white", padx=18, pady=20)

        
        self.clock = Label(self.right, bg=theme[THEME]['primary'], relief=GROOVE,
                            fg=theme[THEME]['fg'], height=2, width=20, 
                            font=('cursed timer ulil', 18, 'bold'))

        self.network = Text(self.details, bg=theme[THEME]['secondary'], 
                            fg=theme[THEME]['fg'], height=5, width=25, 
                            font=('noto mono', 12), padx=20)

        self.system = Text(self.details, bg=theme[THEME]['secondary'], 
                        fg=theme[THEME]['fg'], height=5, width=25, 
                        font=('noto mono', 12), padx=20)

        self.render_menu()
        self.render_widgets()
        self.initiate()
    
    def render_menu(self):
        menu_bar = Menu(root)
        menu_bar.add_command(label='About', command=partial(universal_callback, "start cmd"))

        for key, values in menus.items():

            menu_item = Menu(menu_bar)
            for value in values:
                if type(value) == list:
                    menu_item.add_command(label=value[0], command=partial(universal_callback, value[1]))
                else:
                    menu_item.add_separator()

            menu_bar.add_cascade(label=key, menu=menu_item)
        menu_bar.add_command(label='Exit', command=quit)

        root.config(menu=menu_bar)

    def render_widgets(self):
        self.left.pack(side=LEFT, fill=BOTH, expand=1)
        self.right.pack(side=RIGHT, fill=BOTH, expand=1)

        self.intro.pack(side=TOP, fill=BOTH, expand=1)
        self.welcome.pack(side=LEFT, fill=BOTH, expand=1)
        self.agenda.pack(side=RIGHT, fill=BOTH, expand=1)

        self.gibberish.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.clock.pack(side=TOP, fill=BOTH, expand=1)

        self.details.pack(side=TOP, fill=BOTH, expand=1)
        self.network.pack(side=RIGHT, fill=BOTH, expand=1)
        self.system.pack(side=LEFT, fill=BOTH, expand=1)

        self.commands.pack(side=TOP, fill=BOTH, expand=1)  

        for i in range(4):
            command_row = Frame(self.commands, bg=theme[THEME]['root'])
            command_row.pack(side=TOP, fill=BOTH, expand=1)

            for j in buttons[i]:
                button = Button(command_row, text=j[0], font=('noto mono', 15), 
                                command=partial(universal_callback, url=j[1]), height=2, 
                                width=10, relief=GROOVE, overrelief=GROOVE, 
                                bg=theme[THEME]['primary'], fg=theme[THEME]['fg'])
                button.pack(side=LEFT, fill=BOTH, expand=1)
        
    def initiate(self):
        self.welcome.insert(END, WELCOME_START.strip())
        self.welcome.config(state=DISABLED)

        self.agenda.insert(END, "Type your agenda here:")
        self.clock.config(text = time.strftime(" %I:%M %p | %A %n %d %B %Y", time.localtime()))
        
        self.network.insert(END, NETWORK)
        self.network.config(state=DISABLED)

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()[2]
        gpu = GPUtil.getGPUs()
        battery = psutil.sensors_battery()
        self.system.insert(END, MISC.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                            battery.percent, "Plugged In" if battery.power_plugged else "Not Plugged In"))
        self.system.config(state=DISABLED)
    
        self.recursive()

    def recursive(self):
        def loop():
            global start, update
            
            if (time.time()-update) > 60:
                update = time.time()
                
                self.welcome.config(state=NORMAL)
                self.welcome.delete('1.0', END)
                self.welcome.insert(END, WELCOME_RECURSIVE.strip())
                self.welcome.config(state=DISABLED)
                
                self.clock.config(text = time.strftime(" %I:%M %p | %A %n %d %B %Y", time.localtime()))
                
            if (time.time()-start) > 10:
                start = time.time()
                self.gibberish.delete('1.0', END)

                self.system.config(state=NORMAL)
                self.system.delete('1.0', END)
                cpu = psutil.cpu_percent()
                ram = psutil.virtual_memory()[2]
                gpu = GPUtil.getGPUs()
                battery = psutil.sensors_battery()
                self.system.insert(END, MISC.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                                    battery.percent, "Plugged In" if battery.power_plugged else "Not Plugged In"))
                self.system.config(state=DISABLED)
            
            self.gibberish.insert(CURRENT, ''.join(random.choice(string.printable)))
            self.gibberish.after(2, loop)

        loop()


if __name__ == '__main__':
    gc.enable()

    root = Tk()
    root.config(bg=theme[THEME]['root'], bd=5)
    root.resizable(1, 1)
    root.title("Afterlife")

    start = time.time()
    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()