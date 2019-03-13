# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from tkinter import Tk, Button, CENTER
import sys


def run(args):
    root = Tk()
    root.attributes("-fullscreen", True)

    button = Button(text="Quit", command=lambda: sys.exit(0))
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()


if __name__ == "__main__":
    parser = ArgumentParser()
    args = parser.parse_args()

    run(args)
