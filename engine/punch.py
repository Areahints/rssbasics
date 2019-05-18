# author: Nwaezuoke Kenechukwu
# MIT License

# --------------------------
#  Punch Scraping
# --------------------------

import requests 
from bs4 import BeautifulSoup

from . import engine

# Global variables
CACHE       = 3 # minutes
url_punch      = 'https://www.punchng.com'
raw_html    = 'scrapes/news/punch.html'
output_html = 'output/news/punchrss.html'
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}     

class Punch:
    _url   = ''
    _data  = ''
    _log  = None
    _soup  = None 
    
    def __init__(self, url, log):
        self._url  = url 
        self._log = log 
    
    def retrieve_webpage(self):
        try:
            html = requests.get(self._url)
        except Exception as e:
            print (e)
            self._log.report(str(e))
        else:
            self._data = html.read()
            if len(self._data) > 0:
                print ("Retrieved successfully")
            
    def write_webpage_as_html(self, filepath=raw_html, data=''):
        if data is '':
            data = self._data
        engine.write_webpage_as_html(filepath, data)
            
    def read_webpage_from_html(self, filepath=raw_html):
        self._data = engine.read_webpage_from_html(filepath)
            
    def change_url(self, url):
        self._url = url
            
    def print_data(self):
        print (self._data)
    
    def convert_data_to_bs4(self):
        self._soup = BeautifulSoup(self._data, "html.parser")
        
    def parse_soup_to_simple_html(self):
        news_list = self._soup.find_all(['a']) # a
        
        #print (news_list)
        
        htmltext = '''
<html>
    <head><title>Simple News Link Scrapper</title></head>
    <body>
        {NEWS_LINKS}
    </body>
</html>
'''
        
        news_links = '<ol>'
        
        for tag in news_list:
            if tag.parent.get('href'):
                # print (self._url + tag.parent.get('href'), tag.string)
                link  = self._url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)
                
        news_links += '</ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)
        
        # print(htmltext)
        self.write_webpage_as_html(filepath=output_html, data=htmltext.encode())
    
    
    def print_beautiful_soup(self):
        # print (self._soup.title.string)
        news_list = self._soup.find_all(['h1', 'h2', 'h4']) # h1
        
        #print (news_list)
        for tag in news_list:
            if tag.parent.get('href'):
                print (self._url + tag.parent.get('href'), tag.string)
    
