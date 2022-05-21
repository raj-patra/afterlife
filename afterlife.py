#!/usr/bin/python
import time, psutil, GPUtil, gc, random

from tkinter import Tk, Text, Label, Entry, Button, Frame, Menu
from tkinter import filedialog, messagebox
from tkinter.constants import WORD, GROOVE, RAISED, FLAT, END
from tkinter.constants import LEFT, RIGHT, TOP, BOTTOM, BOTH, DISABLED, NORMAL
from tkinter.constants import E, W, NW

from helpers import applications, constants, schemes
from callbacks import pc_stats_callback, universal_callback, about, destroy
from functools import partial
from collections import deque


class HUD:
    timer_font = 'cursed timer ulil'
    default_font = 'Noto Mono'

    def __init__(self):

        self.current_theme = dict(
            theme=schemes.DEFAULT_THEME_CHOICE,
            primary=dict(
                bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['primary'],
                fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
            ),
            secondary=dict(
                bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['secondary'],
                fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
            ),
            root=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['root'],
            fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
            primary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['primary'],
            secondary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['secondary'],
        )

        # Root Frames
        self.left_frame = Frame(root)
        self.left_top_frame = Frame(self.left_frame)
        self.integrated_exe_frame = Frame(self.left_top_frame)

        self.right_frame = Frame(root)
        self.info_frame = Frame(self.right_frame, height=1)
        self.action_centre_frame = Frame(self.right_frame,
            width=80, height=50,
            bg=self.current_theme['root'], padx=2, pady=2)

        # Widgets on root.left
        self.prompt_text = Text(self.left_frame,
            **self.current_theme["primary"], font=(HUD.default_font, 11), wrap=WORD,
            width=50, padx=20, pady=20,
        )
        self.left_status_label = Label(self.left_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 10), text="☀", anchor=W,
            relief=FLAT, height=1, padx=3, pady=2,
        )

        # Widgets on root.left.intro
        self.welcome_text = Text(self.left_top_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 13), wrap=WORD,
            width=25, height=2, padx=20, pady=20,
        )

        self.iexe_title_label = Label(self.integrated_exe_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 14), text="Integrated Search",
            relief=FLAT, height=2, width=28, padx=2, pady=2,
        )
        self.iexe_query_entry = Entry(self.integrated_exe_frame,
            **self.current_theme["primary"], font=(HUD.default_font, 12, 'bold'),
            bd=5, width=28, insertbackground="white",
        )

        self.iexe_search_button = Button(self.integrated_exe_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 12), text="Duck Duck Go!",
            activebackground=self.current_theme['root'], activeforeground="white",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.callback, command="iexe search"),
        )
        self.iexe_execute_button = Button(self.integrated_exe_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 12), text="Execute Command",
            activebackground=self.current_theme['root'], activeforeground="white",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.callback, command="iexe execute"),
        )
        self.iexe_wiki_button = Button(self.integrated_exe_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 12), text="Search Wikipedia",
            activebackground=self.current_theme['root'], activeforeground="white",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.callback, command="iexe wiki"),
        )

        self.clock_label = Label(self.right_frame,
            **self.current_theme["primary"], font=(HUD.timer_font, 18, 'bold'),
            height=2, width=20, relief=GROOVE,
        )
        self.network_text = Text(self.info_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 12),
            height=5, width=25, padx=20,
        )
        self.system_text = Text(self.info_frame,
            **self.current_theme["secondary"], font=(HUD.default_font, 12),
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
        theme_choice.add_command(label="Random Theme", command=self.update_widget_theme, accelerator='Ctrl+T')
        theme_choice.add_separator()

        for category, themes in schemes.THEME_TYPES.items():
            theme_category = Menu(theme_choice, tearoff=0)

            for theme in themes:
                theme_category.add_command(label=theme, command=partial(self.update_widget_theme, theme))
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

        bg = deque([self.current_theme['primary_bg'], self.current_theme['secondary_bg']])
        self.action_items = []
        self.button_frames = []

        for row in applications.ACTIONS.keys():

            action_row = Frame(self.action_centre_frame, bg=self.current_theme['root'], pady=1)
            action_row.pack(side=TOP, fill=BOTH, expand=1)
            self.button_frames.append(action_row)

            for action in applications.ACTIONS[row]:
                button = Button(action_row,
                    bg=bg[0], fg=self.current_theme['fg'],
                    activebackground=self.current_theme['root'], activeforeground="white",
                    font=(HUD.default_font, 12), text=action["label"],
                    height=1, width=6, relief=FLAT, overrelief=RAISED,
                    command=partial(self.callback, command=action["command"]),
                )
                self.action_items.append(button)
                bg.rotate(1)
                button.pack(side=LEFT, fill=BOTH, expand=1)

    def start_widgets(self):

        self.welcome_text.insert(END, constants.WELCOME.lstrip())
        self.iexe_query_entry.insert(END, "> ")
        self.clock_label.config(text=time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))
        self.network_text.insert(END, constants.NETWORK)

        self.iexe_query_entry.bind('<Return>', partial(self.callback, "iexe search"))
        self.iexe_query_entry.bind('<Control-Return>', partial(self.callback, "iexe execute"))
        self.iexe_query_entry.bind('<Shift-Return>', partial(self.callback, "iexe wiki"))

        root.bind('<Control-s>', self.save_prompt_content)
        root.bind('<Control-S>', self.save_prompt_content)
        root.bind('<Control-t>', partial(self.update_widget_theme, None))
        root.bind('<Control-T>', partial(self.update_widget_theme, None))
        root.bind('<Control-f>', partial(self.callback, "start mailto:rajpatra.kishore@gmail.com"))
        root.bind('<Control-F>', partial(self.callback, "start mailto:rajpatra.kishore@gmail.com"))
        root.bind('<Control-Delete>', partial(self.callback, 'clear'))
        root.bind('<F1>', about)

        self.welcome_text.config(state=DISABLED)
        self.network_text.config(state=DISABLED)
        self.system_text.config(state=DISABLED)

        self.callback("subprocess systeminfo")

        self.update_widget_content()

    def update_widget_content(self):

        def loop():

            pc_stats = pc_stats_callback()

            self.clock_label.config(text=time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))
            self.system_text.config(state=NORMAL)
            self.system_text.delete('1.0', END)

            self.system_text.insert(END,
                constants.SYSTEM.format(
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(pc_stats["boot_time"])),
                    pc_stats["cpu_usage"], pc_stats["ram_usage"],
                    pc_stats["gpu_name"], pc_stats["gpu_usage"],
                    pc_stats["battery_usage"],
                    "(Plugged In)" if pc_stats["battery_plugged"] else "(Not Plugged In)"
                )
            )
            self.system_text.config(state=DISABLED)

            self.left_status_label.config(
                text=constants.LEFT_STATUS_LABEL.format(
                    self.current_theme["theme"],
                    pc_stats["cpu_usage"],
                    pc_stats["ram_usage"],
                    "🔋" if pc_stats["battery_plugged"] else "🔌",
                    pc_stats["battery_usage"],
                    pc_stats["gpu_name"],
                    pc_stats["gpu_usage"]
                )
            )

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

    def update_widget_theme(self, theme=None, event=None):

        if not theme:
            theme = random.choice(list(schemes.THEMES.keys()))

        self.current_theme.update(
            dict(
                theme=theme,
                primary=dict(
                    bg=schemes.THEMES[theme]['primary'],
                    fg=schemes.THEMES[theme]['fg'],
                ),
                secondary=dict(
                    bg=schemes.THEMES[theme]['secondary'],
                    fg=schemes.THEMES[theme]['fg'],
                ),
                root=schemes.THEMES[theme]['root'],
                fg=schemes.THEMES[theme]['fg'],
                primary_bg=schemes.THEMES[theme]['primary'],
                secondary_bg=schemes.THEMES[theme]['secondary'],
            )
        )

        root.config(bg=self.current_theme['root'])

        self.prompt_text.config(**self.current_theme["primary"])
        self.clock_label.config(**self.current_theme["primary"])
        self.welcome_text.config(**self.current_theme["secondary"])

        self.iexe_title_label.config(**self.current_theme["secondary"])
        self.iexe_query_entry.config(**self.current_theme["primary"])

        self.iexe_search_button.config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme['root']
        )
        self.iexe_execute_button.config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme['root']
        )
        self.iexe_wiki_button.config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme['root']
        )

        self.network_text.config(**self.current_theme["secondary"])
        self.system_text.config(**self.current_theme["secondary"])

        self.action_centre_frame.config(
            bg=self.current_theme['root']
        )
        colors = deque([self.current_theme['primary_bg'], self.current_theme['secondary_bg']])

        for frame in self.button_frames:
            frame.config(bg=self.current_theme['root'])

        for button in self.action_items:
            button.config(
                bg=colors[0],
                fg=self.current_theme['fg'],
                activebackground=schemes.THEMES[theme]['root']
            )
            colors.rotate(1)

        pc_stats = pc_stats_callback()
        self.left_status_label.config(
            **self.current_theme["secondary"],
            text=constants.LEFT_STATUS_LABEL.format(
                theme,
                pc_stats["cpu_usage"],
                pc_stats["ram_usage"],
                "🔋" if pc_stats["battery_plugged"] else "🔌",
                pc_stats["battery_usage"],
                pc_stats["gpu_name"],
                pc_stats["gpu_usage"]
            )
        )

    def save_prompt_content(self, event=None):
        handle = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes = [('Text', '*.txt'),('All files', '*')])
        if handle != None:
            handle.write(self.prompt_text.get('1.0', 'end'))
            handle.close()
            messagebox.showinfo('Info', 'The contents of the Text Widget has been saved.')


if __name__ == '__main__':
    gc.enable()

    root = Tk()
    root.config(bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['root'], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")
    root.iconbitmap('static/hud.ico')

    update = time.time()

    hud = HUD()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()
