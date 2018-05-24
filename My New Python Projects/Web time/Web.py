import webbrowser as wb
import time
import pyautogui as py
import datetime
import os

def main1():
    while True:
        date = datetime.datetime.now().strftime("%H")
        if date == '4': #fajr
            #opens website
            wb.open_new('http://www.muslim.co.za/salaahtimes/capetown')
            time.sleep(10)
            #moves sidebar
            py.moveTo(1432, 851)
            py.click(button='left', clicks=4)
            os.system("Fajr.py")
            break
        if date == '13': #Thur
            #opens website
            wb.open_new('http://www.muslim.co.za/salaahtimes/capetown')
            time.sleep(10)
            #moves sidebar
            py.moveTo(1432, 851)
            py.click(button='left', clicks=4)
            os.system("Thur.py")
            break
        if date == '16': #Asr
            #opens website
            wb.open_new('http://www.muslim.co.za/salaahtimes/capetown')
            time.sleep(10)
            #moves sidebar
            py.moveTo(1432, 851)
            py.click(button='left', clicks=4)
            os.system("Asr.py")
            break
        if date == '19': #Magrib
            #opens website
            wb.open_new('http://www.muslim.co.za/salaahtimes/capetown')
            time.sleep(10)
            #moves sidebar
            py.moveTo(1432, 851)
            py.click(button='left', clicks=4)
            time.sleep(1)
            os.system("Magrib.py")
            break
        if date == '20': #Eshaai
            #opens website
            wb.open_new('http://www.muslim.co.za/salaahtimes/capetown')
            time.sleep(10)
            #moves sidebar
            py.moveTo(1432, 851)
            py.click(button='left', clicks=4)
            os.system("Eshaai.py")
            break
main1()


