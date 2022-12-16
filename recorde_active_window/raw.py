
import sqlite3
import sys
sys.path.append('../')
from _config import config

class RecodeToDB:
    cnf = config.Config()
    def __init__(self) -> None:
        self.db_path = fr"{self.cnf.data_dir}\workss.db"
    
    def execute_select(self,MajorItem,MinorItem) -> set:
        sqlline = f"select id,time from awrecorde where MajorItem='{MajorItem}' and MinorItem='{MinorItem}';"
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(sqlline)
        tmp_result = c.fetchall()
        c.close()
        return set(tmp_result)
    
    def execute_select_all(self,sqlline = f"select id,time from awrecorde;") -> set:
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(sqlline)
        tmp_result = c.fetchall()
        c.close()
        return set(tmp_result)

    def execute_select_one(self,MajorItem,MinorItem) -> tuple:
        sqlline = f"select id,time from awrecorde where MajorItem='{MajorItem}' and MinorItem='{MinorItem}';"
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(sqlline)
        tmp_result = c.fetchone()
        c.close()
        return tmp_result
    
    def execute_select_by_id(self,id) -> tuple:
        sqlline = f"select id,time from awrecorde where id={id};"
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(sqlline)
        tmp_result = c.fetchone()
        c.close()
        return tmp_result
    
    def execute_sqlline(self,sqlline):
        conn = sqlite3.connect(self.db_path,isolation_level=None,)
        c = conn.cursor()
        c.execute(sqlline)
        tmp_result = c.fetchall()
        c.close()
        return tmp_result
    
    def execute_insert_sqlline(self,insertdata) -> None:
        conn = sqlite3.connect(self.db_path, isolation_level = None)
        c = conn.cursor()
        c.executemany('INSERT INTO awrecorde(MajorItem, MinorItem, time) VALUES (?,?,?)', insertdata)
        c.close()
     
    def show_table_data(self,mode=0):
        select_sqlline = "select * from awrecorde"
        if mode == 0:
            return self.execute_sqlline(select_sqlline)
        select_sqlline += " order by "
        binary_mode_number = bin(mode)
        if mode == 1:
            select_sqlline += "time"
        elif mode == 2:
            select_sqlline += "MajorItem,time"
        elif mode == 3:
            select_sqlline += "MajorItem,MinorItem"        
        return self.execute_sqlline(select_sqlline)
    
    def drop_db(self) -> None:
        drop_sql = "DROP TABLE awrecorde"
        self.execute_sqlline(drop_sql)
    
    def update_db(self,MajorItem,MinorItem,time):
        time=str(time)
        sqlline = f"update awrecorde set(time)={time} where MajorItem='{MajorItem}' and MinorItem='{MinorItem}'"
        self.execute_sqlline(sqlline)
        return self.execute_select(MajorItem,MinorItem)
        
    def update_db_by_id(self,id,time) -> tuple:
        sqlline = f"update awrecorde set(time)={time} where id={id}"
        self.execute_sqlline(sqlline)
        return self.execute_select_by_id(id)