# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item

from popcorn.items import PopcornItem

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
 
class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
 
    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)
 
    #the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
    #for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]


class movieSpider(CrawlSpider):
    
    name = "popcorn"
    allowed_domains = ["imdb.com"]
    
    start_urls = ["http://www.imdb.com/title/tt1568338/",
    "http://www.imdb.com/title/tt1457767/",
    "http://www.imdb.com/title/tt1219289/",
    "http://www.imdb.com/title/tt0258463/?ref_=nm_knf_i1"
    ]
    
    rules = [
    #Rule(SgmlLinkExtractor(allow=('/title/tt\d{7}/$',)), callback='parse_imdb', follow=True),
    #Rule(SgmlLinkExtractor(allow=('/title/tt\d{7}/',)), follow=True),
    #Rule(SgmlLinkExtractor(allow=('/title/tt\d{7}/?ref_=nm_knf_i[1-9]$',)), callback='parse_imdb', follow=True),
    Rule(SgmlLinkExtractor(allow=('/title/tt\d{7}/\?ref_=tt_rec_tti$',)), callback='parse_imdb', follow=True),
    ]
    
    
    def parse_imdb(self, response):
        self.state['items_count'] = self.state.get('items_count', 0) + 1

        hxs = HtmlXPathSelector(response)
        item = PopcornItem()
        
        item['title'] = hxs.select('/html/body//h1/span[@itemprop="name"]/text()').extract()
        item['url'] = hxs.select('/html/head/link[1]/@href').extract()
        item['year'] = hxs.select('/html/body//h1/span[@class="nobr"]/a/text()').extract()
        item['genre'] = hxs.select('/html/body//div[@itemprop="genre"]/a/text()').extract()
        item['date'] = hxs.select('/html/body//div[contains(h4, "Release Date:")]/text()[2]').extract()        
        item['country'] = hxs.select('/html/body//div[starts-with(h4, "Country:")]/a/text()').extract()
        item['language'] = hxs.select('/html/body//div[starts-with(h4, "Language:")]/a/text()').extract()
        item['length'] = hxs.select('/html/body//div[starts-with(h4, "Runtime:")]/time/text()').extract()
        item['users'] = hxs.select('/html/body//span[@ itemprop="ratingCount"]/text()').extract()
        item['rating'] = hxs.select('/html/body//div[@class="titlePageSprite star-box-giga-star"]/text()').extract()
        item['storyline'] = hxs.select('/html/body//div[@id="titleStoryLine"]/div[@itemprop="description"]/p/text()').extract()
        item['filmingLocation'] = hxs.select('/html/body//div[starts-with(h4, "Filming Locations:")]/a/text()').extract()
        
        return item