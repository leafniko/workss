from . import raw

class HandleRaw(raw.RecodeToDB):
    def __init__(self) -> None:
        super().__init__()
    
    def create_table(self) -> None:
        select_sqlline = "select name from sqlite_master where type='table';"
        select_table_sqlline = "select * from sqlite_master where type='table' and name='awrecorde';"
        create_sqlline = "create table awrecorde(id integer PRIMARY KEY AUTOINCREMENT, MajorItem text, MinorItem text, time integer);"
        
        tmp_result = self.execute_select_all(select_sqlline)
        if tmp_result == None or 'awrecorde' not in tmp_result:
            try:
                self.execute_sqlline(create_sqlline)
            except:
                pass
        tmp_result = self.execute_select_all(select_table_sqlline)
        print(tmp_result)
    
    def update_data(self,MajorItem,MinorItem,time):
        result = self.execute_select_one(MajorItem,MinorItem)
        if result is None or len(result)==0:
            self.execute_insert_sqlline([(str(MajorItem),str(MinorItem),str(time)),])
        else:
            time = int(int(result[1]) + int(time))
            result = self.update_db(MajorItem,MinorItem,time)
            return result
    
    def output_db(self):
        all_data = self.show_table_data(mode=1)
        date = self.cnf.date_ymdhms()
        output_csv_name = fr"{self.cnf.work_dir()}\active_{date}.csv"
        column = ["id","major_item","minor_item","time"]
        with open(output_csv_name,mode="w",encoding="shift_jis",errors="ignore") as f:
            f.write(",".join(column))
            f.write("\n")
            for line in all_data:
                line = [str(i) for i in line]
                tmp_line = "'" + "','".join(line) + "'"
                f.write(tmp_line)
                f.write("\n")
        
            
    
    
    
    