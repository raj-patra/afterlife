import gc
from tkinter import Tk

from application.helpers import schemes
from application.hud import HUD
from application.nicole import NicoleBot


def init_app():
    gc.enable()

    root = Tk()
    root.config(bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]["root"], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")
    root.iconbitmap("assets/static/hud.ico")

    bot_kernel = NicoleBot()

    hud = HUD(root=root, bot_kernel=bot_kernel)
    hud._render_menu()
    hud.apply_position()
    hud.apply_styles()
    hud.init_widgets()
    hud.init_keybinds()
    hud.init_hovertips()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()
