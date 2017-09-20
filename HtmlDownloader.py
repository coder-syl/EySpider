'''
HTMl 下载器
1. 针对静态网页，使用Requests库
2. 针对动态网页使用 selenium和phantomjs
'''
#coding:utf-8
from config import headers ,phantomjs_driver_path,user_agent
if user_agent is None:
    user_agent=input("请添加头部信息")
if phantomjs_driver_path is None:
    phantomjs_driver_path=input("请输入pantomjs所在位置")
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class HtmlDownloader(object):
    #静态网页下载
    def staticPageDownload(self,url):
        if url is None:
            return None
        r=requests.get(url,headers=headers)
        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None
    #动态网页下载
    def dynamicPageDownload(self,url):
        if url is None:
            return None
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] =user_agent
        driver = webdriver.PhantomJS(phantomjs_driver_path,desired_capabilities=dcap)
        driver.get(url)
        r= driver.page_source.encode('utf-8')
        driver.close()
        return r;




