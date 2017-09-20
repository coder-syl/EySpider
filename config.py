'''
config 配置文件
'''
#coding:utf-8

#headers
user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0"
headers={"User-agent":user_agent}

#phantomjs浏览器的所在位置
#例如'C:\Users\Administrator\Anaconda\phantomjs.exe',
phantomjs_driver_path=r"C:\mysoftware\anaconda"

#数据库配置文件
db_config={
    'host':'#',
    'port':3306,
    'user':'root',
    'password':'#',
    'database':'#',
    'charset':'UTF8',
}