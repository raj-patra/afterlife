import time
import gc
from tkinter import Tk
from afterlife.helpers import commands, constants, schemes
from afterlife.hud import HUD

def init_app():
    gc.enable()

    root = Tk()
    root.config(bg=schemes.THEMES[schemes.DEFAULT_THEME_CHOICE]['root'], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")
    root.iconbitmap('static/hud.ico')

    hud = HUD(root=root)
    hud.render_menu()
    hud.render_widgets()
    hud.start_widgets()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()
