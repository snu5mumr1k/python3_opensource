# -*- coding: utf-8 -*-

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        def color_changer(color="white"):
            def change_color():
                self.configure(background=color)
            return change_color

        self.red = tk.Button(self, command=color_changer("red"), text="Turn red")
        self.red.pack(side="right")
        self.green = tk.Button(self, command=color_changer("green"), text="Turn green")
        self.green.pack(side="top")
        self.blue = tk.Button(self, command=color_changer("blue"), text="Turn blue")
        self.blue.pack(side="left")
        self.quit = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    app = Application(master=root)
    app.run()
