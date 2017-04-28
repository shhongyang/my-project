# -*- coding: utf-8 -*-
'''
Created on 2017年4月26日

@author: Administrator
'''
import urllib2

class HtmlDownloader(object):
                
    def download(self,url):
        if url is None:
            return "url is None"
        response=urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return "request failed"
        else:
            return response.read()
        
    



