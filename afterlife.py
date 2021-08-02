#!/usr/bin/python
import time, psutil, GPUtil, gc
import subprocess as sp

from tkinter import *
from helpers.constants import *
from helpers.themes import *
from callbacks import *
from functools import partial
from collections import deque


CHOICE = 'og_blue'


class HUD:
    def __init__(self):
        self.left = Frame(root)
        self.right = Frame(root)
        self.intro = Frame(self.left)
        self.details = Frame(self.right, height=1)

        self.commands = Frame(self.right, width=80,
                                height=50, bg=THEMES[CHOICE]['root'], padx=2, pady=2)
        
        self.prompt = Text(self.left, bg=THEMES[CHOICE]['primary'], wrap=WORD, padx=20, pady=20,
                            fg=THEMES[CHOICE]['fg'], font=('noto mono', 11), width=50)

        self.welcome = Text(self.intro, bg=THEMES[CHOICE]['secondary'], 
                            fg=THEMES[CHOICE]['fg'], width=25, height=2, 
                            font=('noto mono', 13, 'bold'), padx=20, 
                            pady=20, wrap=WORD)

        self.agenda = Text(self.intro, bg=THEMES[CHOICE]['secondary'], 
                            fg=THEMES[CHOICE]['fg'], width=25, height=2, 
                            font=('noto mono', 13, 'bold'), wrap=WORD, 
                            insertbackground="white", padx=20, pady=20)

        
        self.clock = Label(self.right, bg=THEMES[CHOICE]['primary'], relief=GROOVE,
                            fg=THEMES[CHOICE]['fg'], height=2, width=20, 
                            font=('cursed timer ulil', 18, 'bold'))

        self.network = Text(self.details, bg=THEMES[CHOICE]['secondary'], 
                            fg=THEMES[CHOICE]['fg'], height=5, width=29, 
                            font=('noto mono', 12), padx=20)

        self.system = Text(self.details, bg=THEMES[CHOICE]['secondary'], 
                        fg=THEMES[CHOICE]['fg'], height=5, width=31, 
                        font=('noto mono', 12), padx=20)

        self.prompt_blocked = 0

        self.render_menu()
        self.render_widgets()
        self.start_widgets()
    
    def render_menu(self):
        menu_bar = Menu(root)
        menu_bar.add_command(label='About', command=about)

        for key, values in MENUS.items():

            menu_item = Menu(menu_bar)
            for value in values:
                if type(value) == list:
                    menu_item.add_command(label=value[0], command=partial(self.cmd_prompt, value[1]))
                else:
                    menu_item.add_separator()

            menu_bar.add_cascade(label=key, menu=menu_item)

        menu_bar.add_command(label='Clear Prompt', command=partial(self.cmd_prompt, " "))
        menu_bar.add_command(label='Exit', command=partial(destroy, root))

        root.config(menu=menu_bar)

    def render_widgets(self):
        self.left.pack(side=LEFT, fill=BOTH, expand=1)
        self.right.pack(side=RIGHT, fill=BOTH, expand=1)

        self.intro.pack(side=TOP, fill=BOTH, expand=1)
        self.welcome.pack(side=LEFT, fill=BOTH, expand=1)
        self.agenda.pack(side=RIGHT, fill=BOTH, expand=1)

        self.prompt.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.clock.pack(side=TOP, fill=BOTH, expand=0)

        self.details.pack(side=TOP, fill=BOTH, expand=1)
        self.network.pack(side=RIGHT, fill=BOTH, expand=1)
        self.system.pack(side=LEFT, fill=BOTH, expand=1)

        self.commands.pack(side=TOP, fill=BOTH, expand=1)  

        bg = deque([THEMES[CHOICE]['primary'], THEMES[CHOICE]['secondary']])
        for row in range(len(BUTTONS)):
            command_row = Frame(self.commands, bg=THEMES[CHOICE]['root'])
            command_row.pack(side=TOP, fill=BOTH, expand=1)
            for button in BUTTONS[row]:
                button = Button(command_row, text=button[0], font=('noto mono', 12), height=1, 
                                command=partial(universal_callback, url=button[1]),  width=6, 
                                relief=FLAT, overrelief=RAISED, bg=bg[0], fg=THEMES[CHOICE]['fg'], 
                                activebackground=THEMES[CHOICE]['root'], activeforeground="white")

                bg.rotate(1)
                button.pack(side=LEFT, fill=BOTH, expand=1)
        
    def start_widgets(self):
        self.welcome.insert(END, WELCOME.strip())
        self.welcome.config(state=DISABLED)

        self.agenda.insert(END, "Type your agenda here:")
        self.clock.config(text = time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))
        
        self.network.insert(END, NETWORK)
        self.network.config(state=DISABLED)

        self.cmd_prompt("subprocess systeminfo")

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()[2]
        gpu = GPUtil.getGPUs()
        battery = psutil.sensors_battery()
        self.system.insert(END, SYSTEM.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                            battery.percent, "Plugged In" if battery.power_plugged else "Not Plugged In"))
        self.system.config(state=DISABLED)

        self.update_widgets()

    def update_widgets(self):
        
        def loop():
        
            global start, update
            
            if (time.time()-update) > 60:
                update = time.time()
                self.clock.config(text = time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))

            self.system.config(state=NORMAL)
            self.system.delete('1.0', END)
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory()[2]
            gpu = GPUtil.getGPUs()
            battery = psutil.sensors_battery()
            self.system.insert(END, SYSTEM.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                                battery.percent, "(Charging)" if battery.power_plugged else " "))
            self.system.config(state=DISABLED)
            
            self.prompt.after(5000, loop)

        loop()

    def cmd_prompt(self, command):

        if command.startswith('start'):
            os.system("{}".format(command))
        else:
            self.prompt_blocked = 1

            process = command.split(' ', 1)[-1]

            response = sp.getoutput(process)

            self.prompt.config(state=NORMAL)
            self.prompt.delete('1.0', END)
            self.prompt.insert(END, response)
            self.prompt.config(state=DISABLED)



if __name__ == '__main__':
    gc.enable()

    root = Tk()
    root.config(bg=THEMES[CHOICE]['root'], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")

    start = time.time()
    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()