# -*- coding: utf-8 -*-
import feedparser
from html2bbcode import parser
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

try:
    from pyquery import PyQuery as pq
except ImportError:
    print "pip install pyquery"
    sys.exit(1)


'''
Force decode for string codec for input string (file or web)
'''
def force_decode(string, codecs=['utf8', 'big5']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
            pass
'''
Display encode for string display from utf8 to other (Mac UTF-8/ Windows CP950(big5))
if  sys.stdout.encoding == sys.getdefaultencoding():
    it means stdout could display string correctly
else:
    encode from utf8 to stdout.encoding set
'''
def display_encode(string):
    global is_std_default_equal_encoding
    try:
        is_std_default_equal_encoding
    except NameError:
        is_std_default_equal_encoding = 0
    #else:
        #print "sure, it was defined."

    if not is_std_default_equal_encoding:
        encoding_str1 = sys.stdout.encoding.upper()
        #print encoding_str1
        encoding_str2 = sys.getdefaultencoding().upper()
        #print encoding_str2
        is_std_default_equal_encoding = encoding_str1 == encoding_str2
        #print is_std_default_equal_encoding

        encode_id = sys.stdout.encoding
        #print "encode id is", encode_id
        if encode_id != None:
            #print 'using encoding'
            return string.encode(encode_id)
        else:
            return string
    else:
        #print 'skip encodoing'
        return string

def get_latest_article_from_rss_source(rss_source):
    feed = feedparser.parse(rss_source)
    rss_titles = []
    rss_descriptions = []
    if not feed:
        print "no result"
        return (0, 0)
    else:
        #print feed["url"], feed[ "version"], feed.modified
        #feed.etag/modified only support modified wordpress other might not.
        for feed_item in feed["items"]:
            print display_encode(feed_item["title"])
            rss_titles.append(feed_item["title"])
            rss_descriptions.append(feed_item["description"])
            break;
            #print feed_item["description"]
        return (rss_titles, rss_descriptions)

class feeds_content(object):
  def __init__(self, y0, y1, y2):
     self.title = y0
     self.content = y1
     self.link = y2

def get_all_article_from_rss_source(rss_source):
    feed = feedparser.parse(rss_source)
    return_values = []
    rss_descriptions = []
    if not feed:
        print "no result"
        return feeds_content(0, 0, 0)
    else:
        for feed_item in feed["items"]:
            feed_class = feeds_content(feed_item["title"], feed_item["description"], feed_item["link"])
            return_values.append(feed_class)
        return return_values

def get_site_title_from_rss_source(rss_source):
    feeds = feedparser.parse(rss_source)
    return feeds['channel']['title']

def transfer_html_to_bbcode(html_data):
    parser_html = parser.HTML2BBCode()
    #return display_encode(str(parser_html.feed(html_data)))
    return str(parser_html.feed(html_data))
    
if __name__ == "__main__":
    is_std_default_equal_encoding = 1
    rss_url1 = "http://www.evanlin.com/blog/?feed=rss2"
    rss_url2 = "http://www.mesotw.com/bbs/rss.php?fid=25&auth=XC%2BJZQY%2FS4nZo8sf%2F2iTWyoL%2FMb7Hk5bzA"
    rss_url3 = "http://blogs.myoops.org/lucifer.php?tempskin=_rss2"
    rss_url4 = "http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=9388&obs=1&fc=1&warn=1"
    print "----------------Print system data---------------"
    print 'stdout encoding =', sys.stdout.encoding
    print 'default encoding =', sys.getdefaultencoding()
    print "-------------------------------------------------"
    print "Parsing rss data ....."
    my_result = get_all_article_from_rss_source(rss_url2)
    #print 'tota; have ', len(my_result[0]), 'feeds'
    #for each in my_result[0]:
    #print my_result[0][0].encode('utf-8')
    #print display_encode(my_result[1][0])        
    
    #for item in my_result[1]:
    #    print item
    for item in my_result:
        #print item.title
        #print transfer_html_to_bbcode(item.content)
        print item.link
        print 'request from link'
        d=pq(url=item.link)
        #print d.html()
        print '----------------------------'
        #print d('body')
        print d('body').hasClass('t_msgfont') #find specific class in whole body
        #print d('body').find('table').html() #find first table and pass back it's value
        for each_table in d('body').find('table'):
            print each_table #find first table and pass back it's value
            print '########'
        print '----------------------------'
        break        
    #print transfer_html_to_bbcode(my_result[1][0])
