#!/usr/bin/python
import time, psutil, GPUtil, gc, random

from tkinter import Tk, Text, Label, Entry, Button, Frame, Menu
from tkinter import filedialog, messagebox
from tkinter.constants import WORD, GROOVE, RAISED, FLAT, END
from tkinter.constants import LEFT, RIGHT, TOP, BOTTOM, BOTH, DISABLED, NORMAL
from tkinter.constants import E, W, NW

from helpers import applications, constants, schemes
from callbacks import universal_callback, about, destroy
from functools import partial
from collections import deque

THEME_CHOICE = "gotham"


class HUD:
    def __init__(self):

        self.default_font = 'Noto Mono'
        self.timer_font = 'cursed timer ulil'

        # Root Frames
        self.left_frame = Frame(root)
        self.left_top_frame = Frame(self.left_frame)
        self.integrated_exe_frame = Frame(self.left_top_frame)

        self.right_frame = Frame(root)
        self.info_frame = Frame(self.right_frame, height=1)
        self.action_centre_frame = Frame(self.right_frame,
            width=80, height=50,
            bg=schemes.THEMES[THEME_CHOICE]['root'], padx=2, pady=2)

        # Widgets on root.left
        self.prompt_text = Text(self.left_frame,
            bg=schemes.THEMES[THEME_CHOICE]['primary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.default_font, 11), wrap=WORD,
            width=50, padx=20, pady=20,
        )
        self.left_status_label = Label(self.left_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.default_font, 10), text="☀", anchor=W,
            relief=FLAT, height=1, padx=3, pady=2,
        )

        # Widgets on root.left.intro
        self.welcome_text = Text(self.left_top_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.default_font, 13), wrap=WORD,
            width=25, height=2, padx=20, pady=20,
        )

        self.iexe_title_label = Label(self.integrated_exe_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.default_font, 14), text="Integrated Search",
            relief=FLAT, height=2, width=28, padx=2, pady=2,
        )
        self.iexe_query_entry = Entry(self.integrated_exe_frame,
            bg=schemes.THEMES[THEME_CHOICE]['primary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.default_font, 12, 'bold'),
            bd=5, width=28, insertbackground="white",
        )

        self.iexe_search_button = Button(self.integrated_exe_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            activebackground=schemes.THEMES[THEME_CHOICE]['root'], activeforeground="white",
            font=(self.default_font, 12), text="Duck Duck Go!",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.callback, command="iexe search"),
        )
        self.iexe_execute_button = Button(self.integrated_exe_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            activebackground=schemes.THEMES[THEME_CHOICE]['root'], activeforeground="white",
            font=(self.default_font, 12), text="Execute Command",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.callback, command="iexe execute"),
        )
        self.iexe_wiki_button = Button(self.integrated_exe_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            activebackground=schemes.THEMES[THEME_CHOICE]['root'], activeforeground="white",
            font=(self.default_font, 12), text="Search Wikipedia",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.callback, command="iexe wiki"),
        )

        self.clock_label = Label(self.right_frame,
            bg=schemes.THEMES[THEME_CHOICE]['primary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.timer_font, 18, 'bold'),
            height=2, width=20, relief=GROOVE,
        )
        self.network_text = Text(self.info_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.default_font, 12),
            height=5, width=25, padx=20,
        )
        self.system_text = Text(self.info_frame,
            bg=schemes.THEMES[THEME_CHOICE]['secondary'], fg=schemes.THEMES[THEME_CHOICE]['fg'],
            font=(self.default_font, 12),
            height=5, width=35, padx=20,
        )

        self.render_menu()
        self.render_widgets()
        self.start_widgets()

    def render_menu(self):
        menu_bar = Menu(root, tearoff=0)

        menu_item = Menu(menu_bar, tearoff=0)
        menu_item.add_command(label='About', command=about, accelerator='F1')
        menu_item.add_separator()
        menu_item.add_command(label='Save Prompt', command=self.save_prompt_content, accelerator='Ctrl+S')
        menu_item.add_command(label='Clear Prompt', command=partial(self.callback, "clear"), accelerator='Ctrl+Del')
        menu_item.add_separator()

        theme_choice = Menu(menu_bar, tearoff=0)
        theme_choice.add_command(label="Random Theme", command=self.set_theme, accelerator='Ctrl+T')
        theme_choice.add_separator()

        for category, themes in schemes.THEME_TYPES.items():
            theme_category = Menu(theme_choice, tearoff=0)

            for theme in themes:
                theme_category.add_command(label=theme, command=partial(self.set_theme, theme))
            theme_choice.add_cascade(label=category, menu=theme_category)

        menu_item.add_cascade(label="Themes", menu=theme_choice)
        menu_item.add_separator()
        menu_item.add_command(label='Send Feedback', command=partial(self.callback, "start mailto:rajpatra.kishore@gmail.com"), accelerator='Ctrl+F')
        menu_item.add_command(label='Exit', command=partial(destroy, root), accelerator='Alt+F4')
        menu_bar.add_cascade(label='Application', menu=menu_item)

        app_choice = Menu(menu_bar, tearoff=0)
        for app_type, apps in applications.NATIVE_APPS.items():
            app_category = Menu(app_choice, tearoff=0)
            for app in apps:
                app_category.add_command(label=app["label"], command=partial(self.callback, app["command"]))
            app_choice.add_cascade(label=app_type, menu=app_category)

        menu_bar.add_cascade(label="Native Apps", menu=app_choice)

        for label, actions in applications.MENUS.items():
            item = Menu(menu_bar, tearoff=0)
            for action in actions:
                if type(action) == dict:
                    item.add_command(label=action["label"], command=partial(self.callback, action["command"]))
                else:
                    item.add_separator()
            menu_bar.add_cascade(label=label, menu=item)

        root.config(menu=menu_bar)

    def render_widgets(self):
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=1)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=1)

        self.left_top_frame.pack(side=TOP, fill=BOTH, expand=1)
        self.prompt_text.pack(side=TOP, fill=BOTH, expand=1)
        self.left_status_label.pack(side=TOP, fill=BOTH, expand=0)

        self.welcome_text.pack(side=LEFT, fill=BOTH, expand=1)
        self.integrated_exe_frame.pack(side=RIGHT, fill=BOTH, expand=1)

        self.iexe_title_label.pack(side=TOP, fill=BOTH, expand=0)
        self.iexe_query_entry.pack(side=TOP, fill=BOTH, expand=1)
        self.iexe_search_button.pack(side=TOP, fill=BOTH, expand=0)
        self.iexe_execute_button.pack(side=LEFT, fill=BOTH, expand=1)
        self.iexe_wiki_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.clock_label.pack(side=TOP, fill=BOTH, expand=0)
        self.info_frame.pack(side=TOP, fill=BOTH, expand=1)

        self.network_text.pack(side=RIGHT, fill=BOTH, expand=1)
        self.system_text.pack(side=LEFT, fill=BOTH, expand=1)

        self.action_centre_frame.pack(side=TOP, fill=BOTH, expand=1)

        bg = deque([schemes.THEMES[THEME_CHOICE]['primary'], schemes.THEMES[THEME_CHOICE]['secondary']])
        self.action_items = []
        self.button_frames = []

        for row in applications.ACTIONS.keys():
            action_row = Frame(self.action_centre_frame, bg=schemes.THEMES[THEME_CHOICE]['root'], pady=1)
            action_row.pack(side=TOP, fill=BOTH, expand=1)
            self.button_frames.append(action_row)

            for action in applications.ACTIONS[row]:
                button = Button(action_row,
                    bg=bg[0], fg=schemes.THEMES[THEME_CHOICE]['fg'],
                    activebackground=schemes.THEMES[THEME_CHOICE]['root'], activeforeground="white",
                    font=(self.default_font, 12), text=action["label"],
                    height=1, width=6, relief=FLAT, overrelief=RAISED,
                    command=partial(self.callback, command=action["command"]),
                )
                self.action_items.append(button)
                bg.rotate(1)
                button.pack(side=LEFT, fill=BOTH, expand=1)

    def start_widgets(self):
        self.welcome_text.insert(END, constants.WELCOME.lstrip()+constants.CURRENT_THEME.format(THEME_CHOICE))
        self.welcome_text.config(state=DISABLED)
        self.left_status_label.config(text=constants.LEFT_STATUS_LABEL.format(THEME_CHOICE))

        self.iexe_query_entry.insert(END, "> ")
        self.clock_label.config(text = time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))

        self.network_text.insert(END, constants.NETWORK)
        self.network_text.config(state=DISABLED)

        self.iexe_query_entry.bind('<Return>', partial(self.callback, "iexe search"))
        self.iexe_query_entry.bind('<Control-Return>', partial(self.callback, "iexe execute"))
        self.iexe_query_entry.bind('<Shift-Return>', partial(self.callback, "iexe wiki"))

        root.bind('<Control-s>', self.save_prompt_content)
        root.bind('<Control-S>', self.save_prompt_content)
        root.bind('<Control-t>', partial(self.set_theme, None))
        root.bind('<Control-T>', partial(self.set_theme, None))
        root.bind('<Control-f>', partial(self.callback, "start mailto:rajpatra.kishore@gmail.com"))
        root.bind('<Control-F>', partial(self.callback, "start mailto:rajpatra.kishore@gmail.com"))
        root.bind('<Control-Delete>', partial(self.callback, 'clear'))
        root.bind('<F1>', about)

        self.callback("subprocess systeminfo")

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()[2]
        gpu = GPUtil.getGPUs()
        battery = psutil.sensors_battery()

        if len(gpu) > 0:
            self.system_text.insert(END, constants.SYSTEM.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                            battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
        else:
            self.system_text.insert(END, constants.SYSTEM.format(  cpu, ram, 'No GPU found', 0,
                                            battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
        self.system_text.config(state=DISABLED)

        self.update_widgets()

    def update_widgets(self):

        def loop():

            global update

            if (time.time()-update) > 60:
                update = time.time()
                self.clock_label.config(text = time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))

            self.system_text.config(state=NORMAL)
            self.system_text.delete('1.0', END)
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory()[2]
            gpu = GPUtil.getGPUs()
            battery = psutil.sensors_battery()
            if len(gpu) > 0:
                self.system_text.insert(END, constants.SYSTEM.format(  cpu, ram, gpu[0].name, gpu[0].memoryUtil*100,
                                                battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
            else:
                self.system_text.insert(END, constants.SYSTEM.format(  cpu, ram, 'No GPU found', 0,
                                                battery.percent, "(Plugged In)" if battery.power_plugged else "(Not Plugged In)"))
            self.system_text.config(state=DISABLED)

            self.system_text.after(5000, loop)

        loop()

    def callback(self, command, event=None):
        self.prompt_text.config(state=NORMAL)

        if command.startswith('start'):
            universal_callback(command=command)

        elif command.startswith('subprocess'):
            self.prompt_text.delete('1.0', END)
            response = universal_callback(command=command)
            self.prompt_text.insert(END, response)

        elif command.startswith('request'):
            self.prompt_text.delete('1.0', END)
            response = universal_callback(web=command)
            self.prompt_text.insert(END, response)

        elif command.startswith('url'):
            universal_callback(web=command)

        elif command.startswith('iexe'):
            query = self.iexe_query_entry.get()
            if ">" in query:
                query = query.split('>')[-1]

            if command == "iexe search":
                universal_callback(web='search '+query)

            if command == 'iexe execute':
                universal_callback(command="start cmd /k "+query)

            elif command == 'iexe wiki':
                response = universal_callback(web="wiki "+query)
                self.prompt_text.delete('1.0', END)
                self.prompt_text.insert(END, constants.WIKI.format(*response.values()))
                universal_callback(web='url '+response['url'])

            self.iexe_query_entry.delete(0, END)
            self.iexe_query_entry.insert(END, "> ")

        else:
            self.prompt_text.delete('1.0', END)

        self.prompt_text.config(state=DISABLED)

    def set_theme(self, theme=None, event=None):
        if theme == None:
            theme = random.choice(list(schemes.THEMES.keys()))

        root.config(bg=schemes.THEMES[theme]['root'])
        
        primary_bg_theme = dict(
            bg=schemes.THEMES[theme]['primary'],
            fg=schemes.THEMES[theme]['fg'],
        )
        secondary_bg_theme = dict(
            bg=schemes.THEMES[theme]['secondary'],
            fg=schemes.THEMES[theme]['fg'],
        )

        self.prompt_text.config(**primary_bg_theme)
        self.clock_label.config(**primary_bg_theme)
        self.welcome_text.config(**secondary_bg_theme)

        self.iexe_title_label.config(**secondary_bg_theme)
        self.iexe_query_entry.config(**primary_bg_theme)
        
        self.iexe_search_button.config(
            **secondary_bg_theme,
            activebackground=schemes.THEMES[theme]['root']
        )
        self.iexe_execute_button.config(
            **secondary_bg_theme,
            activebackground=schemes.THEMES[theme]['root']
        )
        self.iexe_wiki_button.config(
            **secondary_bg_theme,
            activebackground=schemes.THEMES[theme]['root']
        )

        self.network_text.config(**secondary_bg_theme)
        self.system_text.config(**secondary_bg_theme)

        self.action_centre_frame.config(
            bg=schemes.THEMES[theme]['root']
        )
        colors = deque([schemes.THEMES[theme]['primary'], schemes.THEMES[theme]['secondary']])

        for frame in self.button_frames:
            frame.config(bg=schemes.THEMES[theme]['root'])

        for button in self.action_items:
            button.config(
                bg=colors[0], 
                fg=schemes.THEMES[theme]['fg'], 
                activebackground=schemes.THEMES[theme]['root']
            )
            colors.rotate(1)

        self.welcome_text.config(state=NORMAL)
        self.welcome_text.delete('1.0', END)
        self.welcome_text.insert(END, constants.WELCOME.lstrip()+constants.CURRENT_THEME.format(theme))
        self.welcome_text.config(state=DISABLED)

    def save_prompt_content(self, event=None):
        handle = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes = [('Text', '*.txt'),('All files', '*')])
        if handle != None:
            handle.write(self.prompt_text.get('1.0', 'end'))
            handle.close()
            messagebox.showinfo('Info', 'The contents of the Text Widget has been saved.')

if __name__ == '__main__':
    gc.enable()

    root = Tk()
    root.config(bg=schemes.THEMES[THEME_CHOICE]['root'], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")
    root.iconbitmap('static/hud.ico')

    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()
