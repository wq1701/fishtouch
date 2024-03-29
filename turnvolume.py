# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:22:55 2021

@author: Weiwei QI
"""


import time
import pyautogui
import PySimpleGUI as sg
import multiprocessing


def KeepUI():

    sg.theme('Dark')
    layout = [
        [sg.Text('Keep-Me-Up is now running.\nYou can keep it minised, and it will continue running.\nClose it to disable it.')]
    ]
    # window = sg.Window('Keep-Me-Up', layout, icon = "red_plus.ico")
    window = sg.Window('Keep-Me-Up', layout, icon = "fish.ico")

    p2 = multiprocessing.Process(target=dontsleep)
    p2.start()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            if p2.is_alive():
                p2.terminate()
            break


def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(300)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=KeepUI)
    p1.start()
