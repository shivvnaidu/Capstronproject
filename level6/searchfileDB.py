import sqlite3
class SearchDB():
    def __init__(self):
        self.connect = sqlite3.connect("c://sqlite//hcl.db")
        self.cur = self.connect.cursor()
    def searDB(self ,fil):
        #self.connect=sqlite3.connect("c://sqlite//hcl.db")
        #self.cur=self.connect.cursor()
        #sql="""select * from filelog where filename=?;"""
        self.f="filename"
        sql="""select *from filelog1 where filename like '%{0}'""".format(fil)
        self.cur.execute(sql)
        #args=(filename, )
        #self.cur.execute(sql,args)
        row=self.cur.fetchone()
        if row == None:
            return 0
        else:
            return row
    def insertDB(self,filename):
        sql="""insert into filelog1(filename)values(?);"""
        data=(filename,)
        self.cur.execute(sql,data)
        self.connect.commit()
        return "record added "


if __name__=='__main__':
    obj=SearchDB()
    print(obj.connect)
    print(obj.cur)