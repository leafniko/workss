from recorde_active_window import handle_raw
import win32gui
import pyautogui
import threading
from src import func

class WorkSS:
    dbh = handle_raw.HandleRaw()
    fc = func.Func()
    def __init__(self) -> None:
        self.dbh.create_table()
        self.status = "start"
    
    def chk_active_window(self):
        filename = "work_ss"
        count = 0
        while True:
            if self.status == "stop":
                break
            tmp_key = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            tmp_key = tmp_key.replace("\u200e","")
            screenshotinterval = self.dbh.cnf.screenshotinterval
            if (count%screenshotinterval==0):
                self.fc.get_screenshot(self.dbh.cnf.work_dir(),filename)
            pyautogui.sleep(1)
            count += 1
            awitem = tmp_key.split(" - ")
            MajorItem = awitem[-1]
            MinorItem = tmp_key
            self.dbh.update_data(MajorItem,MinorItem,1)
            
    def main(self):
        moniter_thread = threading.Thread(target=self.chk_active_window)
        moniter_thread.start()
        while True:
            print("1: output the data")
            print("2:watch current data")
            print("3: drop one data by id")
            command = input("0:stop this process")
            if command == "0":
                self.status = "stop"
                break
            
            if command == "1":
                self.dbh.output_db()
            elif command == "2":
                result = self.dbh.show_table_data(mode=2)
                for _ in result:
                    print(_)
            elif command == "3":
                id = input("please input the id:")
                try:
                    self.dbh.delete_by_id(id)
                except:
                    print("failed to delete the data")

if __name__ == "__main__":
    instance = WorkSS()
    instance.main()
