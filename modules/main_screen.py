import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, name: str, width: int, weight: int):
        ctk.CTk.__init__(
            self = self,
                    fg_color = "#0BAD67"
            )
        self.title(name)
        self.geometry(f'{width}x{weight}')

app = App('Minecraft SUPERSIMGASMAPPER335MAKTRAHERBOTS', 1280, 720)