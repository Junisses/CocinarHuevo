import tkinter as tk
from backend.huevo_data import EGG_TYPES
from backend.timer_logic import countdown
import threading
from tkinter import messagebox

class EggDetailPage(tk.Frame):
    def __init__(self, parent, go_back_callback):
        super().__init__(parent)

        self.label_title = tk.Label(self, text="", font=("Helvetica", 18))
        self. label_title.pack(pady=10)

        self.label_ingredients = tk.Label(self, text="", wraplength=300)
        self.label_ingredients.pack(pady=10)

        self.label_timer = tk.Label(self, text="00:00", font=("Helvetica", 32))
        self.label_timer.pack(pady=10)

        self.btn_start = tk.Button(self, text="Iniciar", command=self.start_timer)
        self.btn_start.pack(pady=10)

        self.btn_back = tk.Button(self, text="Volver", command=go_back_callback)
        self.btn_back.pack(pady=5)
    
    def load_egg(self, egg_name):
        self.egg_name = egg_name
        self.label_title.config(text=egg_name)
        ings = EGG_TYPES[egg_name]["ingredientes"]
        self.label_ingredients.config(text="Ingredientes: " + ", ".join(ings))
        self.label_timer.config(text="00:00")
    
    def update_time(self, seconds_left):
        m, s = divmod(seconds_left, 60)
        self.label_timer.config(text=f"{m:02}:{s:02}")
    
    def timer_done(self):
        messagebox.showinfo("¡Listo!", "El huevo está listo")
    
    def start_timer(self):
        duration = EGG_TYPES[self.egg_name]["tiempo"]
        threading.Thread(
            target=countdown,
            args=(duration, self.update_time, self.timer_done),
            daemon=True
        ).start()

