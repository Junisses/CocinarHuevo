import tkinter as tk
from frontend.components.egg_select_page import EggSelectPage
from frontend.components.egg_detail_page import EggDetailPage

def launch_app():
    root = tk.Tk()
    root.title("Cocina tú huevo")
    root.geometry("350x400")
    root.resizable(False,False)

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    def show_frame(name):
        frames[name].tkraise()
    
    def show_detail(egg_name):
        frames["detail"].load_egg(egg_name)
        show_frame("detail")
    
    def go_back():
        show_frame("select")

    frames = {
        "select": EggSelectPage(container, show_detail),
        "detail": EggDetailPage(container, go_back)
    }

    for frame in frames.values():
        frame.grid(row=0, column=0, sticky="nsew")

    show_frame("select")
    root.mainloop()