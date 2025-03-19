import customtkinter as ctk
from .main_screen import app


class Frame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk):
        ctk.CTkFrame.__init__(
            self, 
            master,
            width = 800,
            height = 240,
            fg_color = "#51F683",
            border_width = 5,
            border_color = "white",
            corner_radius = 20,
        )
        self.place(x = 325, y = 430)

Frameapp = Frame(app)