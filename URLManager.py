'''
URl管理器，主要是获取待爬取的链接，主要使用
'''
#coding:utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls=set()#已爬取的url
        self.old_urls=set()#未爬取的url
    def has_new_url(self):
        #判断是否还有未爬取的url
        return self.new_urls_size()!=0
    def get_new_url(self):
        #去除一个未爬取的url
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,url):
        #将新的url放入为未爬取的Url集合中
        #单条url
        if url  is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls_to_old(self,urls):
        # 将新的url放入为未爬取的Url集合中
        # url集合
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.new_urls.add(url)
    def new_urls_size(self):
        #获取未爬取url的大小
        return len(self.new_urls)
    def old_url_size(self):
        # 获取已爬取url的大小
        return len(self.old_urls)





