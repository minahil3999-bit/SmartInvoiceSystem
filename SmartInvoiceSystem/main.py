import customtkinter as ctk

from config import *

from database.db import Database

from gui.dashboard import Dashboard


ctk.set_appearance_mode(THEME)

ctk.set_default_color_theme(COLOR_THEME)


class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(APP_NAME)

        self.geometry("1200x700")

        self.db = Database()

        Dashboard(self)


if __name__ == "__main__":

    app = App()

    app.mainloop()