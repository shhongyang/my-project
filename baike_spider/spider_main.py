# -*- coding: utf-8 -*-

from baike_spider import html_downloader, html_parser, html_outputer, url_manager
class SpyderMain(object):
    def __init__(self):     #初始化四个对象，管理器，下载器，解析器和输出器                       
        self.urls = url_manager.UrlManager()    #点前对象，点后方法
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:    
                new_url = self.urls.get_new_url()
                print 'crawl %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                    
                if count == 1000:
                    break
                
                count += 1
            except:
                print ('carwl failed')              
        self.outputer.output_html()    
    
if __name__ ==  "__main__":
    root_url="http://baike.baidu.com/item/Python"
    obj_spider = SpyderMain()
    obj_spider.crawl(root_url)
    