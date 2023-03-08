import gc
from tkinter import Tk

from application.helpers import schemes
from application.hud import HUD


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
    hud.initialize_widgets()
    hud.initialize_hovertips()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()
