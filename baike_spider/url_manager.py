# -*- coding: utf-8 -*-

class UrlManager(object): 
    def __init__(self):        #需要维护两个列表，未爬和已爬列表
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self,url): #向管理器中添加一个新URL
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
                   
    def add_new_urls(self,urls):    #批量添加URL
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
           
    def has_new_url(self):      #判断管理器中是否有新的未爬URL
        return len(self.new_urls)!= 0
                            
    def get_new_url(self):      #从URL管理器中获取一个未爬URL
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
 

    
   
     
    
    
    
    
    
    
    



