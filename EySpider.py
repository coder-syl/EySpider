'''
爬虫调度器
'''
#coding:utf-8
from URLManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
class EySpider(object):
    def __init__(self):
        self.manager=UrlManager()
        self.downloader=HtmlDownloader()
        self.parser=HtmlParser()
    def urlsCrawl(self,root_url):
        #主要用来获取链接
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url并且可以规定爬取url的数量
        #self.manager.old_url_size()<***
        while(self.manager.has_new_url()):
            try :
                #从url管理器中取出未爬取的连接
                new_url=self.manager.get_new_url()
                #下载页面
                html=self.downloader.staticPageDownload(new_url)
                #获取到新的urls
                urls=self.parser.urlsparser(html)
                self.manager.add_new_urls_to_old(new_url)
            except:
                print("爬取链接失败")

    def keywordsCrawl(self):
        while (self.manager.has_new_url()):
            try:
                # 从url管理器中取出未爬取的连接
                new_url = self.manager.get_new_url()
                # 下载页面
                html = self.downloader.staticPageDownload(new_url)
                # 获取到新的urls
                keywords= self.parser.Parser(html)
                self.manager.add_new_urls_to_old(new_url)
            except:
                print("爬取关键字失败")
if __name__=="__main__":
    EySpiderTest=EySpider()
    root_url=""
    EySpiderTest.urlsCrawl(root_url)
    EySpiderTest.keywordsCrawl()

