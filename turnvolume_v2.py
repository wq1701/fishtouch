# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:22:55 2021

@author: Weiwei QI
"""

import time
import pyautogui
import tkinter as tk
import multiprocessing


def KeepUI():
    root = tk.Tk()
    # root.title("Keep-Me-Up")
    root.title("Caffeinate")

    # Set the window icon if desired (path to .ico or .gif)
    root.iconbitmap('./icon/fish.ico')

    label = tk.Label(root,
                     # text='Keep-Me-Up is now running.\nYou can keep it minimized, and it will continue running.\nClose it to disable it.'
                     text="Stay awake, little machine, for dreams are meant for humans.\n"
                          "\n"
                          "meh, what's life without whimsy"
                     )
    label.pack(pady=20, padx=20)

    # Start the dontsleep process
    p2 = multiprocessing.Process(target=dontsleep)
    p2.start()

    # Define the action to take when the window is closed
    def on_closing():
        if p2.is_alive():
            p2.terminate()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(180)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=KeepUI)
    p1.start()