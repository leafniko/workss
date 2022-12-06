
import os
from src import func
import pyautogui
from datetime import datetime as dt
import win32gui

def main():
    data = {}
    todate = dt.now().strftime('%Y%m%d')
    work_dir = fr"{os.getcwd()}\{todate}"
    filename = "work_ss"
    os.makedirs(work_dir,exist_ok=True)
    csvname = fr"{work_dir}\active_window_metric.csv"
    count = 0
    if os.path.exists(csvname)==True:
        with open(csvname,"r",encoding='shift_jis') as f:
            tmp_txt = f.read().split("\n")
        for tt in tmp_txt:
            tmp_line = tt.split(",")
            data[tmp_line[0]] = tmp_line[1]
    while True:
        tmp_key = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        try:
            data[tmp_key] = str(1 + int(data[tmp_key]))
        except:
            data[tmp_key] = str(1)
        pyautogui.sleep(1)
        count += 1
        if (count%10==0):
            try:
                with open(csvname,'w',encoding='shift_jis') as f:
                    for k, v in data.items():
                        f.write(f'"{k}","{v}"\n')            
            except:
                pass
        if (count%900==0):
            func.get_screenshot(work_dir,filename)

if __name__ == "__main__":
    main()