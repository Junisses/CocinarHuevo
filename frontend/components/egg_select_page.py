import tkinter as tk
import os
from backend.huevo_data import EGG_TYPES

class EggSelectPage(tk.Frame):
    def __init__(self, parent, show_detail_callback):
        super().__init__(parent)

        tk.Label(self, text="Elige tu huevo", font=("Helvetica", 16)).pack(pady=10)
        self.img_refs = {}

        for egg_name in EGG_TYPES:
            img_path = os.path.join("assets", EGG_TYPES[egg_name]["imagen"])
            img = tk.PhotoImage(file = img_path)
            self.img_refs[egg_name] = img

            btn = tk.Button(
                self, image=img, text=egg_name, 
                compound="top", command=lambda name=egg_name: show_detail_callback(name)
            )
            btn.pack(pady=5)