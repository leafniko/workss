
import pyautogui
from glob import glob

class Func:
    def __init__(self) -> None:
         pass
     
    def get_screenshot(self,work_dir,filename):
        try:
            base_path = fr"{work_dir}\{filename}"
            files = glob(f"{base_path}*")
            file_number = [i.split("_")[-1].split(".")[0] for i in files if i.find(f"{base_path}_")>-1]
            new_number = str(len(file_number) + 1)
            file_path = f"{base_path}_{new_number}.png"
            screen_shot = pyautogui.screenshot() 
            screen_shot.save(file_path)
        except Exception as e:
                text = f"Failed to save the screenshot: {file_path}"
                print(e)
                raise Exception
