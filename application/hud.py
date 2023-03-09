#!/usr/bin/python
import random
import time
import turtle
from collections import deque
from functools import partial
from tkinter import (Button, Canvas, Entry, Frame, Label, Menu, Text,
                     filedialog, messagebox, ttk)
from tkinter.constants import (BOTH, BOTTOM, CENTER, DISABLED, END, FLAT,
                               GROOVE, LEFT, NORMAL, NW, RAISED, RIDGE, RIGHT,
                               TOP, WORD, E, W, X, Y, HORIZONTAL)

from idlelib.tooltip import Hovertip

from application.graphics import bytedesign, chaos, yinyang
from application.helpers import commands, constants, schemes
from application.helpers.callbacks import (about_dialog_callback,
                                           destroy_root_callback,
                                           event_handler_callback,
                                           pc_stats_callback,
                                           random_article_callback)


class HUD:
    timer_font = 'cursed timer ulil'
    default_font_old = 'Noto Mono'
    default_font = 'Cascadia Mono'

    def __init__(self, root=None):

        self.root = root
        self.theme = dict(
            theme=schemes.DEFAULT_THEME_CHOICE,
            root=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['root'],
            primary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['primary'],
            secondary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['secondary'],
            fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
            font=(HUD.default_font, 10),
        )
        self.current_theme = dict(
            theme=schemes.DEFAULT_THEME_CHOICE,
            primary=dict(
                bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['primary'],
                fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
                font=(HUD.default_font, 10),
            ),
            secondary=dict(
                bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['secondary'],
                fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
                font=(HUD.default_font, 10),
            ),
            root=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['root'],
            fg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['fg'],
            primary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['primary'],
            secondary_bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['secondary'],
        )

        # Root - Frames
        self.header = dict(frame=Frame(self.root))
        self.left_section_frame = Frame(self.root)
        self.side_bar = dict(frame=Frame(self.left_section_frame, bg=self.current_theme['primary_bg'], bd=5))
        self.iexe_widgets = dict(frame=Frame(self.left_section_frame))
        self.right_section_frame = Frame(self.root)
        self.canvas_widgets = dict(frame=Frame(self.right_section_frame))
        self.action_centre_frame = Frame(self.right_section_frame, bg=self.current_theme['root'])
        self.status_bar = dict(frame=Frame(self.root, bd=1))

        # Widgets on root.header
        self.header.update(
            left_label = ttk.Label(self.header["frame"], text="hello world",
                style="Primary.TLabel", anchor=W),
            right_label = ttk.Label(self.header["frame"], text="clock",
                style="Primary.TLabel", anchor=E)
        )

        # Widgets on root.left
        self.prompt_text = Text(self.left_section_frame,
            **self.current_theme["primary"], wrap=WORD,
            width=50, padx=20, pady=20,
        )
        self.iexe_widgets.update(
            query_entry = Entry(self.iexe_widgets["frame"],
                **self.current_theme["secondary"],
                bd=5, width=28, insertbackground="white",
            ),
            search_button = ttk.Button(self.iexe_widgets["frame"], text="🔎 Search Online",
                style="Secondary.TButton", command=partial(self._event_handler, event="search_query", query=None),
            ),
            execute_button = ttk.Button(self.iexe_widgets["frame"], text="▶ Execute Command",
                style="Secondary.TButton", command=partial(self._event_handler, event="execute_cmd", query=None),
            ),
            wiki_button = ttk.Button(self.iexe_widgets["frame"], text="📖 Wiki Article",
                style="Secondary.TButton", command=partial(self._event_handler, event="fetch_wiki", query=None),
            ),
        )

        # Widgets on root.right
        self.canvas_widgets.update(
            header_label = Label(self.canvas_widgets["frame"],
                **self.current_theme["secondary"], text="Canvas by Afterlife 🎨", anchor=W,
                relief=GROOVE, height=2, width=20, padx=10, pady=2,
            ),
            canvas = Canvas(self.canvas_widgets["frame"],
                bg=self.current_theme["secondary_bg"],
                relief=FLAT, highlightthickness=0,
            ),
            draw_button = ttk.Button(self.canvas_widgets["frame"], text="🖊 Doodle",
                style="Secondary.TButton", command=partial(self._canvas_event_handler, type="bind_pencil"),
            ),
            turtle_button = ttk.Button(self.canvas_widgets["frame"], text="🐢 Turtle",
                style="Secondary.TButton", command=partial(self._canvas_event_handler, type="turtle"),
            ),
            clear_button = ttk.Button(self.canvas_widgets["frame"], text="🗑 Clear Canvas",
                style="Secondary.TButton", command=partial(self._canvas_event_handler, type="clear"),
            ),
        )
        self.screen = turtle.TurtleScreen(self.canvas_widgets["canvas"])
        self.screen.bgcolor(self.current_theme["secondary_bg"])
        self.canvas_widgets["header_label"].config(font=(HUD.default_font, 10, "bold italic"))

        button_styles = deque(["Primary.TButton", "Secondary.TButton"])
        self.dashboard_actions = []
        self.dashboard_frames = []

        for action_idx in range(len(commands.DASHBOARD_ACTIONS)):
            action_row = Frame(self.action_centre_frame, bg=self.current_theme["primary_bg"], pady=1)
            action_row.pack(side=TOP, fill=BOTH, expand=1)
            self.dashboard_frames.append(action_row)

            for action in commands.DASHBOARD_ACTIONS[action_idx]:
                button = ttk.Button(action_row, text=action["label"],
                    style=button_styles[0], command=partial(self._event_handler, event=action["event"], query=action["query"]),
                )
                self.dashboard_actions.append(button)
                button_styles.rotate(1)

        # Widgets on root.side_bar
        self.side_bar.update(actions = [])

        for action in commands.SIDE_BAR_ACTIONS:
            button = ttk.Button(self.side_bar["frame"], text=action["icon"],
                style="Primary.TButton", command=partial(self._event_handler, event=action["event"], query=action["query"]),
            )
            self.side_bar["actions"].append(button)

        # Widgets on root.status_bar
        self.status_bar.update(
            left_label = ttk.Label(self.status_bar["frame"], text="", style="Primary.TLabel", anchor=W),
            right_label = ttk.Label(self.status_bar["frame"], text="", style="Primary.TLabel", anchor=E,),
            actions = []
        )

        for action in commands.STATUS_BAR_ACTIONS:
            button = ttk.Button(self.status_bar["frame"], text=action["icon"],
                style="Primary.TButton", command=partial(self._event_handler, event=action["event"], query=action["query"]),
            )
            self.status_bar["actions"].append(button)

    def render_styles(self):
        """Render styles for all ttk based components"""

        self.custom_styles = ttk.Style()
        self.custom_styles.theme_use("clam")

        self.custom_styles.configure("Primary.TLabel",
            background=self.theme["primary_bg"], foreground=self.theme["fg"],
            font=self.theme["font"], relief=FLAT, width=20, padding=10,
        )

        self.custom_styles.configure("Secondary.TLabel",
            background=self.theme["secondary_bg"], foreground=self.theme["fg"],
            font=self.theme["font"], relief=FLAT, width=20, padding=10,
        )

        self.custom_styles.configure("Primary.TButton",
            background=self.theme["primary_bg"], foreground=self.theme["fg"],
            font=self.theme["font"], width=3, anchor=CENTER, justify=CENTER, cursor="hand1"
        )
        self.custom_styles.map("Primary.TButton",
            background=[("active", self.theme["primary_bg"]), ("pressed", self.theme["primary_bg"])],
            relief=[('pressed', FLAT), ('!pressed', FLAT)],
            borderwidth=[("active", 6)],
        )

        self.custom_styles.configure("Secondary.TButton",
            background=self.theme["secondary_bg"], foreground=self.theme["fg"],
            font=self.theme["font"], width=3, anchor=CENTER, justify=CENTER
        )
        self.custom_styles.map("Secondary.TButton",
            background=[("active", self.theme["secondary_bg"]), ("pressed", self.theme["secondary_bg"])],
            relief=[('pressed', FLAT), ('!pressed', RIDGE)],
            borderwidth=[("active", 5)],
        )

    def render_menu(self):
        menu_bar = Menu(self.root, tearoff=0)

        menu_item = Menu(menu_bar, tearoff=0)
        menu_item.add_command(label='About', command=about_dialog_callback)
        menu_item.add_separator()
        menu_item.add_command(label='Save Prompt', command=self._save_prompt_content, accelerator='Ctrl+S')
        menu_item.add_command(label='Clear Prompt', command=partial(self._event_handler, event="clear_prompt"), accelerator='Ctrl+Del')
        menu_item.add_separator()

        theme_choice = Menu(menu_bar, tearoff=0)
        theme_choice.add_command(label="Random Theme", command=self._update_widget_theme, accelerator='Ctrl+T')
        theme_choice.add_separator()

        for category, themes in schemes.THEME_TYPES.items():
            theme_category = Menu(theme_choice, tearoff=0)

            for theme in themes:
                theme_category.add_command(label=theme, command=partial(self._update_widget_theme, theme))
            theme_choice.add_cascade(label=category, menu=theme_category)

        menu_item.add_cascade(label="Themes", menu=theme_choice)
        menu_item.add_separator()
        menu_item.add_command(label='Send Feedback', command=partial(self._event_handler, "open_url", "https://github.com/raj-patra/afterlife/issues/new"))
        menu_item.add_command(label='Exit', command=partial(destroy_root_callback, self.root), accelerator='Alt+F4')
        menu_bar.add_cascade(label='Application', menu=menu_item)

        for label, actions in commands.MENUS.items():
            item = Menu(menu_bar, tearoff=0)
            for action in actions:
                if type(action) == dict:
                    item.add_command(label=action["label"], command=partial(self._event_handler, action["event"], action["query"]))
                else:
                    item.add_separator()
            menu_bar.add_cascade(label=label, menu=item)

        self.root.config(menu=menu_bar)

    def render_widgets(self):
        self.header["frame"].pack(side=TOP, fill=X, expand=0)
        self.status_bar["frame"].pack(side=BOTTOM, fill=X, expand=0)

        self.header["left_label"].pack(side=LEFT, fill=BOTH, expand=1)
        self.header["right_label"].pack(side=LEFT, fill=BOTH, expand=1)

        self.left_section_frame.pack(side=LEFT, fill=BOTH, expand=1)
        self.right_section_frame.pack(side=LEFT, fill=BOTH, expand=1)

        self.side_bar["frame"].pack(side=LEFT, fill=Y, expand=0)
        self.iexe_widgets["frame"].pack(side=TOP, fill=BOTH, expand=1)
        self.prompt_text.pack(side=TOP, fill=BOTH, expand=1)

        for action in self.status_bar["actions"]:
            action.pack(side=RIGHT, fill=BOTH, expand=0)

        for action in self.side_bar["actions"]:
            action.pack(side=TOP, fill=BOTH, expand=0, ipady=3)

        self.iexe_widgets["query_entry"].pack(side=TOP, fill=BOTH, expand=1)
        self.iexe_widgets["search_button"].pack(side=LEFT, fill=BOTH, expand=1)
        self.iexe_widgets["execute_button"].pack(side=LEFT, fill=BOTH, expand=1)
        self.iexe_widgets["wiki_button"].pack(side=LEFT, fill=BOTH, expand=1)

        self.canvas_widgets["frame"].pack(side=TOP, fill=BOTH, expand=1)
        self.canvas_widgets["header_label"].pack(side=TOP, fill=BOTH, expand=0)
        self.canvas_widgets["canvas"].pack(side=TOP, fill=BOTH, expand=1)
        self.canvas_widgets["draw_button"].pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas_widgets["turtle_button"].pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas_widgets["clear_button"].pack(side=LEFT, fill=BOTH, expand=1)

        self.action_centre_frame.pack(side=TOP, fill=BOTH, expand=1)

        for action in self.dashboard_actions:
            action.pack(side=LEFT, fill=BOTH, expand=1)

        self.status_bar["left_label"].pack(side=LEFT, fill=BOTH, expand=1)
        self.status_bar["right_label"].pack(side=LEFT, fill=BOTH, expand=1)

    def init_widgets(self):

        random_wiki_article = random_article_callback()
        if random_wiki_article:
            self.iexe_widgets["query_entry"].insert(END, "> "+random_wiki_article)
            self._event_handler(event="fetch_wiki")
        else:
            self.iexe_widgets["query_entry"].insert(END, "> ")
            self._event_handler(event="execute_subprocess", query="systeminfo")

        self.header["left_label"].config(text=constants.WELCOME_MSG)
        self.header["right_label"].config(text=time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))

        self.update_widget_content()

    def init_keybinds(self):

        self.iexe_widgets["query_entry"].bind('<Return>', partial(self._event_handler, "search_query"))
        self.iexe_widgets["query_entry"].bind('<Control-Return>', partial(self._event_handler, "execute_cmd"))
        self.iexe_widgets["query_entry"].bind('<Shift-Return>', partial(self._event_handler, "fetch_wiki"))

        self.root.bind('<Control-s>', self._save_prompt_content)
        self.root.bind('<Control-S>', self._save_prompt_content)
        self.root.bind('<Control-t>', partial(self._update_widget_theme, None))
        self.root.bind('<Control-T>', partial(self._update_widget_theme, None))
        self.root.bind('<Control-Delete>', partial(self._event_handler, "clear_prompt"))

    def init_hovertips(self):
        """Initializes hovertips for required widgets"""

        # Hovertips for iexe widgets
        Hovertip(anchor_widget=self.iexe_widgets["search_button"],
            text=self.iexe_widgets["search_button"]["text"]+" (Enter)", hover_delay=100
        )
        Hovertip(anchor_widget=self.iexe_widgets["execute_button"],
            text=self.iexe_widgets["execute_button"]["text"]+" (Ctrl+Enter)", hover_delay=100
        )
        Hovertip(anchor_widget=self.iexe_widgets["wiki_button"],
            text=self.iexe_widgets["wiki_button"]["text"]+" (Shift+Enter)", hover_delay=100
        )

        # Hovertips for status bar action widgets
        for action_idx in range(len(self.status_bar["actions"])):
            Hovertip(anchor_widget=self.status_bar["actions"][action_idx],
                text=commands.STATUS_BAR_ACTIONS[action_idx]["label"], hover_delay=100
            )

        # Hovertips for side bar action widgets
        for action_idx in range(len(self.side_bar["actions"])):
            Hovertip(anchor_widget=self.side_bar["actions"][action_idx],
                text=commands.SIDE_BAR_ACTIONS[action_idx]["label"], hover_delay=100
            )

    def update_widget_content(self):

        def loop():

            pc_stats = pc_stats_callback()

            self.header["right_label"].config(text=time.strftime(" %I:%M %p - %A - %d %B %Y", time.localtime()))

            self.status_bar["left_label"].config(
                text=constants.LEFT_STATUS_LABEL.format(
                    self.current_theme["theme"],
                    pc_stats["cpu_usage"],

                    pc_stats["virtual_memory_used"],
                    pc_stats["virtual_memory_total"],
                    pc_stats["virtual_memory_percent"],

                    pc_stats["disk_used"],
                    pc_stats["disk_total"],
                    pc_stats["disk_percent"],
                )
            )
            self.status_bar["right_label"].config(
                text=constants.RIGHT_STATUS_LABEL.format(
                    time.strftime("%Hhrs %Mmin", time.localtime(time.time() - pc_stats["boot_time"])),
                    "🔌" if pc_stats["battery_plugged"] else "🔋",
                    pc_stats["battery_usage"],
                )
            )
            self.root.after(5000, loop)

        loop()

    def _event_handler(self, event: str=None, query: str=None):

        if event in ["start_app", "open_url"]:
            event_handler_callback(event=event, query=query)

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
            query = self.iexe_widgets["query_entry"].get()
            if ">" in query:
                query = query.split('>')[-1]

            if event == "execute_cmd":
                event_handler_callback(event="start_app", query="start cmd /k "+query)

            elif event == "fetch_wiki":
                self.prompt_text.config(state=NORMAL)
                self.prompt_text.delete('1.0', END)
                response, error = event_handler_callback(event=event, query=query)
                if error:
                    self.prompt_text.insert(END, constants.WIKI.format(*response.values()))
                    self._event_handler(event="open_url", query=response['url'])
                else:
                    self.prompt_text.insert(END, constants.WIKI.format(*response.values()))
                self.prompt_text.config(state=DISABLED)

            else:
                event_handler_callback(event=event, query=query)

            self.iexe_widgets["query_entry"].delete(0, END)
            self.iexe_widgets["query_entry"].insert(END, "> ")

    def _update_widget_theme(self, theme=None, event=None):

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

        self.header["left_label"].config(**self.current_theme["primary"])
        self.header["right_label"].config(**self.current_theme["primary"])

        self.prompt_text.config(**self.current_theme["primary"])

        self.iexe_widgets["query_entry"].config(**self.current_theme["secondary"])
        self.iexe_widgets["search_button"].config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme["secondary_bg"],
            activeforeground=self.current_theme["fg"],
        )
        self.iexe_widgets["execute_button"].config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme["secondary_bg"],
            activeforeground=self.current_theme["fg"],
        )
        self.iexe_widgets["wiki_button"].config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme["secondary_bg"],
            activeforeground=self.current_theme["fg"],
        )


        self.canvas_widgets["header_label"].config(**self.current_theme["secondary"])
        self.canvas_widgets["canvas"].config(bg=self.current_theme["secondary_bg"])
        self.canvas_widgets["draw_button"].config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme["secondary_bg"],
            activeforeground=self.current_theme["fg"],
        )
        self.canvas_widgets["turtle_button"].config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme["secondary_bg"],
            activeforeground=self.current_theme["fg"],
        )
        self.canvas_widgets["clear_button"].config(
            **self.current_theme["secondary"],
            activebackground=self.current_theme["secondary_bg"],
            activeforeground=self.current_theme["fg"],
        )

        self.action_centre_frame.config(
            bg=self.current_theme['root']
        )
        colors = deque([self.current_theme['primary_bg'], self.current_theme['secondary_bg']])

        for frame in self.dashboard_frames:
            frame.config(bg=self.current_theme['root'])

        for button in self.dashboard_actions:
            button.config(
                bg=colors[0],
                fg=self.current_theme['fg'],
                activebackground=colors[0],
                activeforeground=self.current_theme['fg'],
            )
            colors.rotate(1)

        for action in self.status_bar["actions"]:
            action.config(
                **self.current_theme["secondary"],
                activebackground=self.current_theme["secondary_bg"],
                activeforeground=self.current_theme["fg"],
            )

        self.side_bar["frame"].config(bg=self.current_theme["primary_bg"])
        for action in self.side_bar["actions"]:
            action.config(
                **self.current_theme["primary"],
                activebackground=self.current_theme["primary_bg"],
                activeforeground=self.current_theme["fg"],
            )

        pc_stats = pc_stats_callback()
        self.status_bar["left_label"].config(
            **self.current_theme["secondary"],
            text=constants.LEFT_STATUS_LABEL.format(
                theme,
                pc_stats["cpu_usage"],

                pc_stats["virtual_memory_used"],
                pc_stats["virtual_memory_total"],
                pc_stats["virtual_memory_percent"],

                pc_stats["disk_used"],
                pc_stats["disk_total"],
                pc_stats["disk_percent"],
            )
        )
        self.status_bar["right_label"].config(
            **self.current_theme["secondary"],
            text=constants.RIGHT_STATUS_LABEL.format(
                time.strftime("%Hhrs %Mmin", time.localtime(time.time() - pc_stats["boot_time"])),
                "🔌" if pc_stats["battery_plugged"] else "🔋",
                pc_stats["battery_usage"],
            )
        )

        # Clear Canvas content
        self.canvas_widgets["canvas"].delete("all")

    def _save_prompt_content(self, event=None):
        handle = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes = [('Text', '*.txt'),('All files', '*')])
        if handle != None:
            handle.write(self.prompt_text.get('1.0', 'end'))
            handle.close()
            messagebox.showinfo('Info', 'The contents of the Text Widget has been saved.')

    def _canvas_event_handler(self, event=None, type=None):

        if type == "bind_pencil":
            self._canvas_event_handler(type="clear")
            self.canvas_widgets["draw_button"].config(state=DISABLED)
            self.canvas_widgets["canvas"].bind("<B1-Motion>", self._canvas_doodle)

        elif type == "turtle":
            self._canvas_event_handler(type="clear")
            self.canvas_widgets["turtle_button"].config(state=DISABLED)
            self.canvas_widgets["canvas"].unbind("<B1-Motion>")

            cursor = turtle.RawTurtle(self.screen, shape="turtle")
            chaos.main(cursor, self.screen)

        elif type == "clear":
            self.screen._RUNNING = False
            self.canvas_widgets["canvas"].delete("all")
            self.canvas_widgets["canvas"].unbind("<B1-Motion>")
            self.canvas_widgets["draw_button"].config(state=NORMAL)
            self.canvas_widgets["turtle_button"].config(state=NORMAL)

    def _canvas_doodle(self, event=None):
        x1, y1 = ( event.x - 2 ), ( event.y - 2 )
        x2, y2 = ( event.x + 2 ), ( event.y + 2 )
        self.canvas_widgets["canvas"].create_oval( x1, y1, x2, y2, fill=self.current_theme["root"])
