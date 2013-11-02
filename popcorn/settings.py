# Scrapy settings for popcorn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'popcorn'

SPIDER_MODULES = ['popcorn.spiders']
NEWSPIDER_MODULE = 'popcorn.spiders'
JOBDIR='allmovies'


DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5 Avant Browser/1.2.789rel1 (http://www.avantbrowser.com) Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a Opera/7.50 (Windows XP; U) Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en)'
COOKIES_ENABLED = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'popcorn (+http://www.yourdomain.com)'
