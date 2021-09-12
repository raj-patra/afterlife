#!/usr/bin/python
import time, psutil, GPUtil, gc, random

from tkinter import Tk, Text, Label, Entry, Button, Frame, Menu
from tkinter import filedialog, messagebox
from tkinter.constants import WORD, GROOVE, RAISED, FLAT, END
from tkinter.constants import LEFT, RIGHT, TOP, BOTTOM, BOTH, DISABLED, NORMAL

import helpers.constants as constants
import helpers.themes as scheme
from callbacks import universal_callback, about, destroy
from functools import partial
from collections import deque

CHOICE = random.choice(list(scheme.THEMES.keys()))


class HUD:
    def __init__(self):
        # Root Frames
        self.left = Frame(root)
        self.right = Frame(root)
        self.default_font = 'Maiandra GD'
        self.default_font = 'noto mono'
        self.timer_font = 'cursed timer ulil'

            # Widgets on root.left
        self.left_top = Frame(self.left)
        self.prompt = Text(self.left, bg=scheme.THEMES[CHOICE]['primary'], wrap=WORD, padx=20, pady=20,
                            fg=scheme.THEMES[CHOICE]['fg'], font=(self.default_font, 11), width=50)

                # Widgets on root.left.intro
        self.welcome = Text(self.left_top, bg=scheme.THEMES[CHOICE]['secondary'],
                            fg=scheme.THEMES[CHOICE]['fg'], width=25, height=2,
                            font=(self.default_font, 13), padx=20,
                            pady=20, wrap=WORD)
        self.cmd = Frame(self.left_top)

        self.cmd_title = Label(self.cmd, bg=scheme.THEMES[CHOICE]['secondary'], relief=GROOVE,
                            fg=scheme.THEMES[CHOICE]['fg'], height=2, width=28, padx=2, pady=2,
                            font=(self.default_font, 14), text="Integrated CMD / Wiki Search")
        self.cmd_input = Entry(self.cmd, bg=scheme.THEMES[CHOICE]['primary'], fg=scheme.THEMES[CHOICE]['fg'], bd=7,
                            width=28, font=(self.default_font, 12, 'bold'), insertbackground="white",)

        self.cmd_buttons = Frame(self.cmd)
        self.cmd_execute = Button(self.cmd_buttons, text="Execute Command", font=(self.default_font, 12), height=1,
                                command=partial(self.callback, command="cmd execute"), width=6,
                                relief=RAISED, overrelief=RAISED, bg=scheme.THEMES[CHOICE]['secondary'], fg=scheme.THEMES[CHOICE]['fg'],
                                activebackground=scheme.THEMES[CHOICE]['root'], activeforeground="white")
        self.cmd_external = Button(self.cmd_buttons, text="Execute External", font=(self.default_font, 12), height=1,
                                command=partial(self.callback, command="cmd external"), width=6,
                                relief=RAISED, overrelief=RAISED, bg=scheme.THEMES[CHOICE]['secondary'], fg=scheme.THEMES[CHOICE]['fg'],
                                activebackground=scheme.THEMES[CHOICE]['root'], activeforeground="white")
        
        self.wiki_buttons = Frame(self.cmd)
        self.wiki_execute = Button(self.cmd, text="Search Wikipedia", font=(self.default_font, 12), height=1,
                                command=partial(self.callback, command="wiki execute"), width=6,
                                relief=RAISED, overrelief=RAISED, bg=scheme.THEMES[CHOICE]['secondary'], fg=scheme.THEMES[CHOICE]['fg'],
                                activebackground=scheme.THEMES[CHOICE]['root'], activeforeground="white")
        self.wiki_external = Button(self.cmd, text="Search External", font=(self.default_font, 12), height=1,
                                command=partial(self.callback, command="wiki external"), width=6,
                                relief=RAISED, overrelief=RAISED, bg=scheme.THEMES[CHOICE]['secondary'], fg=scheme.THEMES[CHOICE]['fg'],
                                activebackground=scheme.THEMES[CHOICE]['root'], activeforeground="white")


            # Widgets on root.right
        self.clock = Label(self.right, bg=scheme.THEMES[CHOICE]['primary'], relief=GROOVE,
                            fg=scheme.THEMES[CHOICE]['fg'], height=2, width=20,
                            font=(self.timer_font, 18, 'bold'))
        self.info = Frame(self.right, height=1)
        self.buttons = Frame(self.right, width=80,
                                height=50, bg=scheme.THEMES[CHOICE]['root'], padx=2, pady=2)

                # Widgets on root.right.details
        self.network = Text(self.info, bg=scheme.THEMES[CHOICE]['secondary'],
                            fg=scheme.THEMES[CHOICE]['fg'], height=5, width=27,
                            font=(self.default_font, 12), padx=20)
        self.system = Text(self.info, bg=scheme.THEMES[CHOICE]['secondary'],
                        fg=scheme.THEMES[CHOICE]['fg'], height=5, width=33,
                        font=(self.default_font, 12), padx=20)

        self.render_menu()
        self.render_widgets()
        self.start_widgets()
    
    def render_menu(self):
        menu_bar = Menu(root, tearoff=0)

        menu_item = Menu(menu_bar, tearoff=0)
        menu_item.add_command(label='About', command=about, accelerator='F1')
        menu_item.add_separator()
        menu_item.add_command(label='Save', command=self.save_prompt_content, accelerator='Ctrl+S')
        menu_item.add_separator()
        menu_item.add_command(label='Clear Prompt', command=partial(self.callback, "clear"), accelerator='Ctrl+Del')
        menu_item.add_command(label='Exit', command=partial(destroy, root), accelerator='Alt+F4')
        menu_bar.add_cascade(label='Application', menu=menu_item)

        for key, values in constants.MENUS.items():
            menu_item = Menu(menu_bar, tearoff=0)
            for value in values:
                if type(value) == list:
                    menu_item.add_command(label=value[0], command=partial(self.callback, value[1]))
                else:
                    menu_item.add_separator()
            menu_bar.add_cascade(label=key, menu=menu_item)

        theme_choice = Menu(menu_bar, tearoff=0)
        theme_choice.add_command(label="Random Theme", command=self.set_theme, accelerator='Ctrl+T')
        theme_choice.add_separator()

        for category, themes in scheme.THEME_TYPES.items():
            theme_category = Menu(theme_choice, tearoff=0)

            for theme in themes:
                theme_category.add_command(label=theme, command=partial(self.set_theme, theme))
            theme_choice.add_cascade(label=category, menu=theme_category)

        menu_bar.add_cascade(label="Themes", menu=theme_choice)

        root.config(menu=menu_bar)

    def render_widgets(self):
        self.left.pack(side=LEFT, fill=BOTH, expand=1)
        self.right.pack(side=RIGHT, fill=BOTH, expand=1)

        self.left_top.pack(side=TOP, fill=BOTH, expand=1)
        self.welcome.pack(side=LEFT, fill=BOTH, expand=1)
        self.cmd.pack(side=RIGHT, fill=BOTH, expand=1)

        self.cmd_title.pack(side=TOP, fill=BOTH, expand=0)
        self.cmd_input.pack(side=TOP, fill=BOTH, expand=1)

        self.cmd_buttons.pack(side=TOP, fill=BOTH, expand=0)
        self.cmd_execute.pack(side=LEFT, fill=BOTH, expand=1)
        self.cmd_external.pack(side=LEFT, fill=BOTH, expand=1)

        self.wiki_buttons.pack(side=TOP, fill=BOTH, expand=0)
        self.wiki_execute.pack(side=LEFT, fill=BOTH, expand=1)
        self.wiki_external.pack(side=LEFT, fill=BOTH, expand=1)

        self.prompt.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.clock.pack(side=TOP, fill=BOTH, expand=0)

        self.info.pack(side=TOP, fill=BOTH, expand=1)
        self.network.pack(side=RIGHT, fill=BOTH, expand=1)
        self.system.pack(side=LEFT, fill=BOTH, expand=1)

        self.buttons.pack(side=TOP, fill=BOTH, expand=1)  

        bg = deque([scheme.THEMES[CHOICE]['primary'], scheme.THEMES[CHOICE]['secondary']])
        self.action_items = []
        self.button_frames = []

        for row in range(len(constants.BUTTONS)):
            command_row = Frame(self.buttons, bg=scheme.THEMES[CHOICE]['root'], pady=1)
            command_row.pack(side=TOP, fill=BOTH, expand=1)
            self.button_frames.append(command_row)
            for button in constants.BUTTONS[row]:
                button = Button(command_row, text=button[0], font=(self.default_font, 12), height=1, 
                                command=partial(self.callback, command=button[1]),  width=6, 
                                relief=FLAT, overrelief=RAISED, bg=bg[0], fg=scheme.THEMES[CHOICE]['fg'], 
                                activebackground=scheme.THEMES[CHOICE]['root'], activeforeground="white")

                self.action_items.append(button)
                bg.rotate(1)
                button.pack(side=LEFT, fill=BOTH, expand=1)
        
    def start_widgets(self):
        self.welcome.insert(END, constants.WELCOME.lstrip()+constants.CURRENT_THEME.format(CHOICE))
        self.welcome.config(state=DISABLED)

        self.cmd_input.insert(END, "> ")
        self.clock.config(text = time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))
        
        self.network.insert(END, constants.NETWORK)
        self.network.config(state=DISABLED)

        self.cmd_input.bind('<Return>', partial(self.callback, "cmd execute"))
        root.bind('<Control-s>', self.save_prompt_content)
        root.bind('<Control-S>', self.save_prompt_content)
        root.bind('<Control-t>', partial(self.set_theme, None))
        root.bind('<Control-T>', partial(self.set_theme, None))
        root.bind('<Control-Delete>', partial(self.callback, 'clear'))
        root.bind('<F1>', about)

        self.callback("subprocess systeminfo")

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()[2]
        gpu = GPUtil.getGPUs()
        battery = psutil.sensors_battery()

        if len(gpu) > 0:
            self.system.insert(END, constants.SYSTEM.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                            battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
        else:
            self.system.insert(END, constants.SYSTEM.format(  cpu, ram, 'No GPU found', 0,
                                            battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
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
            if len(gpu) > 0:
                self.system.insert(END, constants.SYSTEM.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                                battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
            else:
                self.system.insert(END, constants.SYSTEM.format(  cpu, ram, 'No GPU found', 0,
                                                battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
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

        elif command.startswith('request'):
            self.prompt.delete('1.0', END)
            response = universal_callback(web=command)
            self.prompt.insert(END, response)

        elif command.startswith('url'):
            universal_callback(web=command)

        elif command.startswith('cmd') or command.startswith('wiki'):
            query = self.cmd_input.get()
            if ">" in query:
                query = query.split('>')[-1]
                
            if command == 'cmd execute':
                self.prompt.delete('1.0', END)
                response = universal_callback(command="subprocess "+query)
                self.prompt.insert(END, response)
            elif command == 'cmd external':
                universal_callback(command="start cmd /k "+query)

            elif command == 'wiki execute':
                response = universal_callback(web="wiki "+query)
                self.prompt.delete('1.0', END)
                self.prompt.insert(END, constants.WIKI.format(*response.values()))
            elif command == 'wiki external':
                response = universal_callback(web="wiki "+query)
                universal_callback(web='url '+response['url'])
            
            self.cmd_input.delete(0, END)
            self.cmd_input.insert(END, "> ")

        else:
            self.prompt.delete('1.0', END)
            
        self.prompt.config(state=DISABLED)

    def set_theme(self, theme=None, event=None):
        if theme == None:
            theme = random.choice(list(scheme.THEMES.keys()))

        root.config(bg=scheme.THEMES[theme]['root'])

        self.prompt.config(bg=scheme.THEMES[theme]['primary'], fg=scheme.THEMES[theme]['fg'])
        self.clock.config(bg=scheme.THEMES[theme]['primary'], fg=scheme.THEMES[theme]['fg'])
        
        self.welcome.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'])

        self.cmd_title.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'])
        self.cmd_input.config(bg=scheme.THEMES[theme]['primary'], fg=scheme.THEMES[theme]['fg'])
        self.cmd_execute.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'], activebackground=scheme.THEMES[theme]['root'])
        self.cmd_external.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'], activebackground=scheme.THEMES[theme]['root'])
        self.wiki_execute.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'], activebackground=scheme.THEMES[theme]['root'])
        self.wiki_external.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'], activebackground=scheme.THEMES[theme]['root'])

        self.network.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'])
        self.system.config(bg=scheme.THEMES[theme]['secondary'], fg=scheme.THEMES[theme]['fg'])

        self.buttons.config(bg=scheme.THEMES[theme]['root'])
        colors = deque([scheme.THEMES[theme]['primary'], scheme.THEMES[theme]['secondary']])

        for frame in self.button_frames:
            frame.config(bg=scheme.THEMES[theme]['root'])

        for button in self.action_items:
            button.config(bg=colors[0], fg=scheme.THEMES[theme]['fg'], activebackground=scheme.THEMES[theme]['root'])
            colors.rotate(1)

        self.welcome.config(state=NORMAL)
        self.welcome.delete('1.0', END)
        self.welcome.insert(END, constants.WELCOME.lstrip()+constants.CURRENT_THEME.format(theme))
        self.welcome.config(state=DISABLED)

    def save_prompt_content(self, event=None):
        handle = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes = [('Text', '*.txt'),('All files', '*')])
        if handle != None:
            handle.write(self.prompt.get('1.0', 'end'))
            handle.close()
            messagebox.showinfo('Info', 'The contents of the Text Widget has been saved.')

if __name__ == '__main__':
    gc.enable()

    root = Tk()
    root.config(bg=scheme.THEMES[CHOICE]['root'], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")
    root.iconbitmap('static/hud.ico')

    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()