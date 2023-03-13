import gc
from tkinter import Tk

from application.helpers import themes
from application.gui import Afterlife
from application.nicole import NicoleBot


def init_app():
    gc.enable()

    root = Tk()
    root.config(bg=themes.THEMES[themes.DEFAULT_THEME]["root"], bd=5)
    root.resizable(1, 1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("Afterlife")
    root.iconbitmap("assets/static/hud.ico")

    bot_kernel = NicoleBot()

    app = Afterlife(root=root, bot_kernel=bot_kernel)
    app.apply_position()
    app.apply_styles()
    app.init_widgets()
    app.init_keybinds()
    app.init_hovertips()

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

    gc.collect()
