# -*- coding: utf-8 -*-
"""
Created on Fri May 08 2026

@author: Weiwei QI, Cursor/Gemini 3.1 Pro
"""

import time
import pyautogui
import tkinter as tk
import multiprocessing


def KeepUI():
    root = tk.Tk()
    root.title("Caffeinate")

    # Set the window icon if desired (path to .ico or .gif)
    try:
        root.iconbitmap('./icon/fish.ico')
    except Exception:
        pass

    label = tk.Label(root,
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
        try:
            pyautogui.press('volumedown')
            time.sleep(1)
            pyautogui.press('volumeup')
            time.sleep(180)
        except pyautogui.FailSafeException:
            # If PyAutoGUI fail-safe triggers (mouse in screen corner),
            # we simply catch the exception, pause briefly, and resume the loop.
            # This prevents the process from crashing completely!
            time.sleep(5)


if __name__ == '__main__':
    # freeze_support is good practice for multiprocessing on Windows
    multiprocessing.freeze_support()
    p1 = multiprocessing.Process(target=KeepUI)
    p1.start()
