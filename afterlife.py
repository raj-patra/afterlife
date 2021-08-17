#!/usr/bin/python
import time, psutil, GPUtil, gc, random

from tkinter import *
from helpers.constants import *
from helpers.themes import *
from callbacks import *
from functools import partial
from collections import deque

CHOICE = random.choice(list(THEMES.keys()))


class HUD:
    def __init__(self):
        # Root Frames
        self.left = Frame(root)
        self.right = Frame(root)

            # Widgets on root.left
        self.left_top = Frame(self.left)
        self.prompt = Text(self.left, bg=THEMES[CHOICE]['primary'], wrap=WORD, padx=20, pady=20,
                            fg=THEMES[CHOICE]['fg'], font=('noto mono', 11), width=50)
                
                # Widgets on root.left.intro
        self.welcome = Text(self.left_top, bg=THEMES[CHOICE]['secondary'], 
                            fg=THEMES[CHOICE]['fg'], width=25, height=2, 
                            font=('noto mono', 13, 'bold'), padx=20, 
                            pady=20, wrap=WORD)
        self.cmd = Frame(self.left_top)

        self.cmd_title = Label(self.cmd, bg=THEMES[CHOICE]['secondary'], relief=GROOVE,
                            fg=THEMES[CHOICE]['fg'], height=2, width=28, padx=2, pady=2,
                            font=('noto mono', 14), text="Integrated Command Prompt")
        self.cmd_input = Entry(self.cmd, bg=THEMES[CHOICE]['primary'], fg=THEMES[CHOICE]['fg'], bd=7,
                            width=28, font=('noto mono', 12, 'bold'), insertbackground="white",)
        self.cmd_submit = Button(self.cmd, text="Execute", font=('noto mono', 12), height=1, 
                                command=partial(self.callback, command="command"),  width=6, 
                                relief=FLAT, overrelief=RAISED, bg=THEMES[CHOICE]['secondary'], fg=THEMES[CHOICE]['fg'], 
                                activebackground=THEMES[CHOICE]['root'], activeforeground="white")
        

            # Widgets on root.right
        self.clock = Label(self.right, bg=THEMES[CHOICE]['primary'], relief=GROOVE,
                            fg=THEMES[CHOICE]['fg'], height=2, width=20,
                            font=('cursed timer ulil', 18, 'bold'))
        self.info = Frame(self.right, height=1)
        self.buttons = Frame(self.right, width=80,
                                height=50, bg=THEMES[CHOICE]['root'], padx=2, pady=2)
        
                # Widgets on root.right.details
        self.network = Text(self.info, bg=THEMES[CHOICE]['secondary'], 
                            fg=THEMES[CHOICE]['fg'], height=5, width=28, 
                            font=('noto mono', 12), padx=20)
        self.system = Text(self.info, bg=THEMES[CHOICE]['secondary'], 
                        fg=THEMES[CHOICE]['fg'], height=5, width=32, 
                        font=('noto mono', 12), padx=20)

        self.render_menu()
        self.render_widgets()
        self.start_widgets()
    
    def render_menu(self):
        menu_bar = Menu(root, tearoff=0)
        menu_bar.add_command(label='About', command=about)

        for key, values in MENUS.items():
            menu_item = Menu(menu_bar, tearoff=0)
            for value in values:
                if type(value) == list:
                    menu_item.add_command(label=value[0], command=partial(self.callback, value[1]))
                else:
                    menu_item.add_separator()
            menu_bar.add_cascade(label=key, menu=menu_item)

        theme_choice = Menu(menu_bar, tearoff=0)
        theme_choice.add_command(label="Random Theme", command=self.set_theme)
        theme_choice.add_separator()

        for category, themes in THEME_TYPES.items():
            theme_category = Menu(theme_choice, tearoff=0)

            for theme in themes:
                theme_category.add_command(label=theme, command=partial(self.set_theme, theme))
            theme_choice.add_cascade(label=category, menu=theme_category)

        menu_bar.add_cascade(label="Themes", menu=theme_choice)

        menu_bar.add_command(label='Clear Prompt', command=partial(self.callback, "clear"))
        menu_bar.add_command(label='Exit', command=partial(destroy, root))

        root.config(menu=menu_bar)

    def render_widgets(self):
        self.left.pack(side=LEFT, fill=BOTH, expand=1)
        self.right.pack(side=RIGHT, fill=BOTH, expand=1)

        self.left_top.pack(side=TOP, fill=BOTH, expand=1)
        self.welcome.pack(side=LEFT, fill=BOTH, expand=1)
        self.cmd.pack(side=RIGHT, fill=BOTH, expand=1)

        self.cmd_title.pack(side=TOP, fill=BOTH, expand=0)
        self.cmd_input.pack(side=TOP, fill=BOTH, expand=1)
        self.cmd_submit.pack(side=TOP, fill=BOTH, expand=0)

        self.prompt.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.clock.pack(side=TOP, fill=BOTH, expand=0)

        self.info.pack(side=TOP, fill=BOTH, expand=1)
        self.network.pack(side=RIGHT, fill=BOTH, expand=1)
        self.system.pack(side=LEFT, fill=BOTH, expand=1)

        self.buttons.pack(side=TOP, fill=BOTH, expand=1)  

        bg = deque([THEMES[CHOICE]['primary'], THEMES[CHOICE]['secondary']])
        self.action_items = []

        for row in range(len(BUTTONS)):
            command_row = Frame(self.buttons, bg=THEMES[CHOICE]['root'])
            command_row.pack(side=TOP, fill=BOTH, expand=1)
            for button in BUTTONS[row]:
                button = Button(command_row, text=button[0], font=('noto mono', 12), height=1, 
                                command=partial(self.callback, command=button[1]),  width=6, 
                                relief=FLAT, overrelief=RAISED, bg=bg[0], fg=THEMES[CHOICE]['fg'], 
                                activebackground=THEMES[CHOICE]['root'], activeforeground="white")

                self.action_items.append(button)
                bg.rotate(1)
                button.pack(side=LEFT, fill=BOTH, expand=1)
        
    def start_widgets(self):
        self.welcome.insert(END, WELCOME.strip())
        self.welcome.config(state=DISABLED)

        self.cmd_input.insert(END, "> ")
        self.clock.config(text = time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))
        
        self.network.insert(END, NETWORK)
        self.network.config(state=DISABLED)

        self.cmd_input.bind('<Return>', partial(self.callback, "command"))

        self.callback("subprocess systeminfo")

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
        
            global update
            
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
            
            self.system.after(5000, loop)

        loop()

    def callback(self, command, event=None):
        self.prompt.config(state=NORMAL)
        
        if command.startswith('start'):
            universal_callback(command=command)
        
        elif command.startswith('subprocess'):
            self.prompt.delete('1.0', END)
            response = universal_callback(command=command)
            self.prompt.insert(END, response)

        elif command.startswith('url'):
            universal_callback(http=command)

        elif command.startswith('request'):
            self.prompt.delete('1.0', END)
            response = universal_callback(http=command)
            self.prompt.insert(END, response)
        
        else:
            self.prompt.delete('1.0', END)
            command = self.cmd_input.get()   

            if ">" in command:
                command = command.split('>')[-1]

            response = universal_callback(command="subprocess "+command)
            self.prompt.insert(END, response)

            self.cmd_input.delete(0, END)
            self.cmd_input.insert(END, "> ")
            
        self.prompt.config(state=DISABLED)

    def set_theme(self, theme=None):
        if theme == None:
            theme = random.choice(list(THEMES.keys()))

        root.config(bg=THEMES[theme]['root'])

        self.prompt.config(bg=THEMES[theme]['primary'], fg=THEMES[theme]['fg'])
        self.clock.config(bg=THEMES[theme]['primary'], fg=THEMES[theme]['fg'])
        
        self.welcome.config(bg=THEMES[theme]['secondary'], fg=THEMES[theme]['fg'])

        self.cmd_title.config(bg=THEMES[theme]['secondary'], fg=THEMES[theme]['fg'])
        self.cmd_input.config(bg=THEMES[theme]['primary'], fg=THEMES[theme]['fg'])
        self.cmd_submit.config(bg=THEMES[theme]['secondary'], fg=THEMES[theme]['fg'], activebackground=THEMES[theme]['root'])

        self.network.config(bg=THEMES[theme]['secondary'], fg=THEMES[theme]['fg'])
        self.system.config(bg=THEMES[theme]['secondary'], fg=THEMES[theme]['fg'])

        self.buttons.config(bg=THEMES[theme]['root'])
        colors = deque([THEMES[theme]['primary'], THEMES[theme]['secondary']])

        for button in self.action_items:
            button.config(bg=colors[0], fg=THEMES[theme]['fg'], activebackground=THEMES[theme]['root'])
            colors.rotate(1)


if __name__ == '__main__':
    gc.enable()

    root = Tk()
    root.config(bg=THEMES[CHOICE]['root'], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")
    root.iconbitmap('static/hud.ico')

    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()