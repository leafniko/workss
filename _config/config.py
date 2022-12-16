import os
from datetime import datetime as dt

class Config:
    def __init__(self) -> None:
        todate = self.date_ymd()
        work_dir = fr"{os.getcwd()}\{todate}"
        self.set_work_dir(work_dir)
        self.data_dir = fr"{os.getcwd()}\data"
        self.setting_file = fr"{self.data_dir}\setting.txt"
        os.makedirs(self.data_dir,exist_ok=True)
        self.read_setting_file()
    
    def date_ymd(self):
        return dt.now().strftime('%Y%m%d')

    def date_ymdhms(self):
        return dt.now().strftime('%Y%m%d%H%M%S')

    def set_work_dir(self,work_dir) -> None:
        os.makedirs(work_dir,exist_ok=True)
        self.__work_dir = work_dir
    
    def work_dir(self) -> str:
        return self.__work_dir
    
    def read_setting_file(self) -> None:
        if os.path.exists(self.setting_file)==False:
            setting_txt = self.make_setting_file()
        else:
            try:
                with open(self.setting_file,"r",encoding="shift_jis") as f:
                    setting_txt = f.read()
            except Exception as e:
                print(e)
                print("設定ファイルが何らかの理由で読み込みできません。")
                waiting = input("解決後にEnterで処理を再開します。:")
                self.read_setting_file()                
        setting_txt = setting_txt.split("\n")
        screenshotinterval = [i for i in setting_txt if i.find("screenshotinterval:")==0]
        if len(screenshotinterval) == 0:
            self.screenshotinterval = 900
        else:
            try:
                self.screenshotinterval = int(screenshotinterval[0].split(":")[1])
            except:
                print("設定内のscreenshotintervalの値の指定方法が誤っています。暫定で900に指定しています。")
                self.screenshotinterval = 900

    def make_setting_file(self) -> str:
        setting_text = """# 作業フォルダを指定できます(無指定時は実行場所)
work_dir:
# スクリーンショット取得の間隔時間(second)
screenshotinterval:900
"""
        try:
            with open(self.setting_file,"w",encoding="shift_jis") as f:
                f.write(setting_text)
            return setting_text
        except Exception as e:
            print(e)
            waiting = input(f"{self.setting_file} が何らかの事情で使用できません。解決の上でEnterをおして処理を再開してください。")
            self.make_setting_file()
    