#!/usr/bin/python
from gc import callbacks
import random
import time
from collections import deque
from functools import partial
from tkinter import (Button, Entry, Frame, Label, Menu, Text, filedialog,
                     messagebox)
from tkinter.constants import (BOTH, BOTTOM, DISABLED, END, FLAT, GROOVE, LEFT,
                               NORMAL, NW, RAISED, RIGHT, TOP, WORD, E, W, X,
                               Y)

from application.helpers import commands, constants, schemes
from application.helpers.callbacks import (about_dialog_callback, destroy_root_callback, event_handler_callback, pc_stats_callback,
                                         universal_callback, random_article_callback)


class HUD:
    timer_font = 'cursed timer ulil'
    default_font_old = 'Noto Mono'
    default_font = 'Cascadia Mono'

    def __init__(self, root=None):

        self.root = root
        self.current_theme = dict(
            theme=schemes.DEFAULT_THEME_CHOICE,
            primary=dict(
                bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['primary'],
                fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
                font=(HUD.default_font, 12),
            ),
            secondary=dict(
                bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['secondary'],
                fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
                font=(HUD.default_font, 12),
            ),
            root=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['root'],
            fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
            primary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['primary'],
            secondary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['secondary'],
        )
        # Root Frame - Bottom
        self.status_bar_frame = Frame(root)

        # Root Frames - Left
        self.left_section_frame = Frame(root)
        self.integrated_exe_frame = Frame(self.left_section_frame)

        # Root Frames - Right
        self.right_section_frame = Frame(root)
        self.info_frame = Frame(self.right_section_frame, height=1)
        self.action_centre_frame = Frame(self.right_section_frame,
            width=80, height=50,
            bg=self.current_theme['root'], padx=2, pady=2)

        # Widgets on root.left
        self.prompt_text = Text(self.left_section_frame,
            **self.current_theme["primary"], wrap=WORD,
            width=50, padx=20, pady=20,
        )
        self.welcome_label = Label(self.left_section_frame,
            **self.current_theme["primary"], text="", anchor=W,
            relief=FLAT, height=2, width=20, padx=20, pady=2,
        )

        self.iexe_query_entry = Entry(self.integrated_exe_frame,
            **self.current_theme["secondary"],
            bd=5, width=28, insertbackground="white",
        )
        self.iexe_search_button = Button(self.integrated_exe_frame,
            **self.current_theme["secondary"], text="Duck Duck Go!",
            activebackground=self.current_theme['root'], activeforeground="white",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.event_handler, event="search_query", query=None),
        )
        self.iexe_execute_button = Button(self.integrated_exe_frame,
            **self.current_theme["secondary"], text="Execute Command",
            activebackground=self.current_theme['root'], activeforeground="white",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.event_handler, event="execute_cmd", query=None),
        )
        self.iexe_wiki_button = Button(self.integrated_exe_frame,
            **self.current_theme["secondary"], text="Search Wikipedia",
            activebackground=self.current_theme['root'], activeforeground="white",
            height=1, width=6, relief=RAISED, overrelief=RAISED,
            command=partial(self.event_handler, event="fetch_wiki", query=None),
        )

        self.left_status_label = Label(self.status_bar_frame,
            **self.current_theme["secondary"], text="", anchor=W,
            relief=FLAT, height=1, padx=3, pady=2,
        )
        self.left_status_label.config(font=(HUD.default_font, 10))

        # Widgets on root.right
        self.clock_label = Label(self.right_section_frame,
            **self.current_theme["primary"], text="", anchor=E,
            relief=FLAT, height=2, width=20, padx=20, pady=2,
        )
        self.network_text = Text(self.info_frame,
            **self.current_theme["secondary"], height=5, width=25, padx=20,
        )
        self.system_text = Text(self.info_frame,
            **self.current_theme["secondary"], height=5, width=35, padx=20,
        )

    def render_menu(self):
        menu_bar = Menu(self.root, tearoff=0)

        menu_item = Menu(menu_bar, tearoff=0)
        menu_item.add_command(label='About', command=about_dialog_callback)
        menu_item.add_separator()
        menu_item.add_command(label='Save Prompt', command=self.save_prompt_content, accelerator='Ctrl+S')
        menu_item.add_command(label='Clear Prompt', command=partial(self.event_handler, event="clear_prompt"), accelerator='Ctrl+Del')
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
        menu_item.add_command(label='Send Feedback', command=partial(self.event_handler, "open_url", "https://github.com/raj-patra/afterlife/issues/new"))
        menu_item.add_command(label='Exit', command=partial(destroy_root_callback, self.root), accelerator='Alt+F4')
        menu_bar.add_cascade(label='Application', menu=menu_item)

        app_choice = Menu(menu_bar, tearoff=0)
        for app_type, apps in commands.NATIVE_APPS.items():
            app_category = Menu(app_choice, tearoff=0)
            for app in apps:
                app_category.add_command(label=app["label"], command=partial(self.event_handler, app["event"], app["query"]))
            app_choice.add_cascade(label=app_type, menu=app_category)

        menu_bar.add_cascade(label="Native Apps", menu=app_choice)

        for label, actions in commands.MENUS.items():
            item = Menu(menu_bar, tearoff=0)
            for action in actions:
                if type(action) == dict:
                    item.add_command(label=action["label"], command=partial(self.event_handler, action["event"], action["query"]))
                else:
                    item.add_separator()
            menu_bar.add_cascade(label=label, menu=item)

        self.root.config(menu=menu_bar)

    def render_widgets(self):
        self.status_bar_frame.pack(side=BOTTOM, fill=X, expand=0)
        self.left_section_frame.pack(side=LEFT, fill=BOTH, expand=1)
        self.right_section_frame.pack(side=LEFT, fill=BOTH, expand=1)

        self.welcome_label.pack(side=TOP, fill=BOTH, expand=0)
        self.integrated_exe_frame.pack(side=TOP, fill=BOTH, expand=1)
        self.prompt_text.pack(side=TOP, fill=BOTH, expand=1)
        self.left_status_label.pack(side=TOP, fill=BOTH, expand=1)

        self.iexe_query_entry.pack(side=TOP, fill=BOTH, expand=1)
        self.iexe_execute_button.pack(side=LEFT, fill=BOTH, expand=1)
        self.iexe_search_button.pack(side=LEFT, fill=BOTH, expand=1)
        self.iexe_wiki_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.clock_label.pack(side=TOP, fill=BOTH, expand=0)
        self.action_centre_frame.pack(side=TOP, fill=BOTH, expand=1)
        self.info_frame.pack(side=TOP, fill=BOTH, expand=1)

        self.network_text.pack(side=RIGHT, fill=BOTH, expand=1)
        self.system_text.pack(side=LEFT, fill=BOTH, expand=1)

        bg = deque([self.current_theme['primary_bg'], self.current_theme['secondary_bg']])
        self.action_items = []
        self.button_frames = []

        for row in commands.ACTIONS.keys():

            action_row = Frame(self.action_centre_frame, bg=self.current_theme['root'], pady=1)
            action_row.pack(side=TOP, fill=BOTH, expand=1)
            self.button_frames.append(action_row)

            for action in commands.ACTIONS[row]:
                button = Button(action_row,
                    bg=bg[0], fg=self.current_theme['fg'],
                    activebackground=self.current_theme['root'], activeforeground="white",
                    font=(HUD.default_font, 12), text=action["label"],
                    height=1, width=6, relief=FLAT, overrelief=RAISED,
                    command=partial(self.event_handler, event=action["event"], query=action["query"]),
                )
                self.action_items.append(button)
                bg.rotate(1)
                button.pack(side=LEFT, fill=BOTH, expand=1)

    def start_widgets(self):

        self.welcome_label.config(text=constants.WELCOME)
        self.iexe_query_entry.insert(END, "> "+random_article_callback())
        self.clock_label.config(text=time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))
        self.network_text.insert(END, constants.NETWORK)

        self.iexe_query_entry.bind('<Return>', partial(self.event_handler, "search_query"))
        self.iexe_query_entry.bind('<Control-Return>', partial(self.event_handler, "execute_cmd"))
        self.iexe_query_entry.bind('<Shift-Return>', partial(self.event_handler, "fetch_wiki"))

        self.root.bind('<Control-s>', self.save_prompt_content)
        self.root.bind('<Control-S>', self.save_prompt_content)
        self.root.bind('<Control-t>', partial(self.update_widget_theme, None))
        self.root.bind('<Control-T>', partial(self.update_widget_theme, None))
        self.root.bind('<Control-Delete>', partial(self.event_handler, "clear_prompt"))

        self.network_text.config(state=DISABLED)
        self.system_text.config(state=DISABLED)

        self.event_handler(event="fetch_wiki")
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
                    "🔌" if pc_stats["battery_plugged"] else "🔋",
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
            self.prompt_text.insert(END, response.strip())

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

    def event_handler(self, event: str=None, query: str=None):

        if event == "start_app":
            response = event_handler_callback(event=event, query=query)

        elif event == "open_url":
            response = event_handler_callback(event=event, query=query)
            
        elif event == "clear_prompt":
            self.prompt_text.config(state=NORMAL)
            self.prompt_text.delete('1.0', END)
            self.prompt_text.config(state=DISABLED)

        elif event == "execute_subprocess":
            self.prompt_text.config(state=NORMAL)
            self.prompt_text.delete('1.0', END)
            response = event_handler_callback(event=event, query=query)
            self.prompt_text.insert(END, response.strip())
            self.prompt_text.config(state=DISABLED)

        elif event in ["search_query", "execute_cmd", "fetch_wiki"]:
            query = self.iexe_query_entry.get()
            if ">" in query:
                query = query.split('>')[-1]

            if event == "execute_cmd":
                response = event_handler_callback(event="start_app", query="start cmd /k "+query)

            elif event == "fetch_wiki":
                self.prompt_text.config(state=NORMAL)
                self.prompt_text.delete('1.0', END)
                response = event_handler_callback(event=event, query=query)
                if response["error"]:
                    self.prompt_text.insert(END, constants.WIKI.format(*response.values()))
                    self.event_handler(event="open_url", query=response['url'])
                else:
                    self.prompt_text.insert(END, constants.WIKI.format(*response.values()))
                self.prompt_text.config(state=DISABLED)

            else:
                response = event_handler_callback(event=event, query=query)
                
            self.iexe_query_entry.delete(0, END)
            self.iexe_query_entry.insert(END, "> ")

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

        self.root.config(bg=self.current_theme['root'])

        self.prompt_text.config(**self.current_theme["primary"])
        self.clock_label.config(**self.current_theme["primary"])
        self.welcome_label.config(**self.current_theme["primary"])

        self.iexe_query_entry.config(**self.current_theme["secondary"])
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
                "🔌" if pc_stats["battery_plugged"] else "🔋",
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
