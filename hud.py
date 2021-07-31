#!/usr/bin/python
import random, string, time, psutil, GPUtil, gc
import subprocess as sp

from tkinter import *
from constants import *
from callbacks import *
from functools import partial

CHOICE = 'dark_blue'


class HUD:
    def __init__(self):
        self.left = Frame(root)
        self.right = Frame(root)
        self.intro = Frame(self.left)
        self.details = Frame(self.right, height=1)

        self.commands = Frame(self.right, width=80,
                                height=50, bg=THEME[CHOICE]['root'], padx=5, pady=5)
        
        self.prompt = Text(self.left, bg=THEME[CHOICE]['primary'], wrap=WORD,
                            fg=THEME[CHOICE]['fg'], font=('noto mono', 12), width=40)

        self.welcome = Text(self.intro, bg=THEME[CHOICE]['secondary'], 
                            fg=THEME[CHOICE]['fg'], width=25, height=2, 
                            font=('noto mono', 13, 'bold'), padx=20, 
                            pady=20, wrap=WORD)

        self.agenda = Text(self.intro, bg=THEME[CHOICE]['secondary'], 
                            fg=THEME[CHOICE]['fg'], width=25, height=2, 
                            font=('noto mono', 13, 'bold'), wrap=WORD, 
                            insertbackground="white", padx=18, pady=20)

        
        self.clock = Label(self.right, bg=THEME[CHOICE]['primary'], relief=GROOVE,
                            fg=THEME[CHOICE]['fg'], height=3, width=20, 
                            font=('cursed timer ulil', 18, 'bold'))

        self.network = Text(self.details, bg=THEME[CHOICE]['secondary'], 
                            fg=THEME[CHOICE]['fg'], height=5, width=30, 
                            font=('noto mono', 12), padx=20)

        self.system = Text(self.details, bg=THEME[CHOICE]['secondary'], 
                        fg=THEME[CHOICE]['fg'], height=5, width=30, 
                        font=('noto mono', 12), padx=20)

        self.prompt_blocked = 0

        self.render_menu()
        self.render_widgets()
        self.initiate()
    
    def render_menu(self):
        menu_bar = Menu(root)
        menu_bar.add_command(label='About', command=partial(universal_callback, "start cmd"))

        for key, values in MENUS.items():

            menu_item = Menu(menu_bar)
            for value in values:
                if type(value) == list:
                    menu_item.add_command(label=value[0], command=partial(self.cmd_prompt, value[1]))
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

        self.prompt.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.clock.pack(side=TOP, fill=BOTH, expand=0)

        self.details.pack(side=TOP, fill=BOTH, expand=1)
        self.network.pack(side=RIGHT, fill=BOTH, expand=1)
        self.system.pack(side=LEFT, fill=BOTH, expand=1)

        self.commands.pack(side=TOP, fill=BOTH, expand=1)  

        for row in range(len(BUTTONS)):
            command_row = Frame(self.commands, bg=THEME[CHOICE]['root'])
            command_row.pack(side=TOP, fill=BOTH, expand=1)

            for button in BUTTONS[row]:
                button = Button(command_row, text=button[0], font=('noto mono', 12), 
                                command=partial(universal_callback, url=button[1]), height=2, 
                                width=6, relief=GROOVE, overrelief=GROOVE, 
                                bg=THEME[CHOICE]['primary'], fg=THEME[CHOICE]['fg'])
                button.pack(side=LEFT, fill=BOTH, expand=1)
        
    def initiate(self):
        self.welcome.insert(END, WELCOME.strip())
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
                self.clock.config(text = time.strftime(" %I:%M %p | %A %n %d %B %Y", time.localtime()))

            if (time.time()-start) > 10:
                start = time.time()
    
                if not self.prompt_blocked:
                    self.prompt.delete('1.0', END)

                self.system.config(state=NORMAL)
                self.system.delete('1.0', END)
                cpu = psutil.cpu_percent()
                ram = psutil.virtual_memory()[2]
                gpu = GPUtil.getGPUs()
                battery = psutil.sensors_battery()
                self.system.insert(END, MISC.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                                    battery.percent, "Plugged In" if battery.power_plugged else "Not Plugged In"))
                self.system.config(state=DISABLED)

            if not self.prompt_blocked:
                self.prompt.insert(CURRENT, ''.join(random.choice(string.printable)))
                self.prompt.after(10, loop)

        loop()

    def cmd_prompt(self, command):

        if command.startswith('start'):
            os.system("{}".format(command))
        else:
            self.prompt_blocked = 1

            response = sp.getoutput(command)

            self.prompt.config(state=NORMAL)
            self.prompt.delete('1.0', END)
            self.prompt.insert(END, response)
            self.prompt.config(state=DISABLED)



if __name__ == '__main__':
    gc.enable()

    root = Tk()
    root.config(bg=THEME[CHOICE]['root'], bd=5)
    root.resizable(1, 1)
    root.title("Afterlife")

    start = time.time()
    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()