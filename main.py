
import os
from src import func
import pyautogui
from datetime import datetime as dt

def main():
    todate = dt.now().strftime('%Y%m%d')
    work_dir = fr"{os.getcwd()}\{todate}"
    filename = "work_ss"
    os.makedirs(work_dir)
    while True:
        func.get_screenshot(work_dir,filename)
        pyautogui.sleep(900)

if __name__ == "__main__":
    main()