'''
数据存储器 ；使用pymysql 封装mysql的基本操作
主要分装了插入操作
'''
#coding: utf-8
import pymysql
from config import db_config
class DataSave(object):
    def initDb(self):
        self.conn=pymysql.connect(host=db_config.host,user=db_config.user,
                                  password=db_config.password,port=db_config.port,
                                  database=db_config.database,charset=db_config.charset,
        )
        cur=self.conn.cursor()
        if not cur:
            raise(NameError,"数据库连接失败")
        return cur
    def ExecuteInsert(self,sql):
        cur=self.initDb()
        result=cur.execute(sql)
        if not result:
            raise (NameError,"插入数据失败")
        self.conn.commit()
        self.conn.close()


