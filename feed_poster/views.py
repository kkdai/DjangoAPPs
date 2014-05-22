from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from rssfeed import *
import sys


# Create your views here.
def index(request):
    return render(request, 'feed_poster/index.html') 

def feed_get(request):
    is_std_default_equal_encoding = 1
    url_name = request.POST['url_name']
    site_title = get_site_title_from_rss_source(url_name)
    my_result = get_all_article_from_rss_source(url_name)
   
    #for each in my_result[0]:
    #print my_result[0][0].encode('utf-8')
    #print display_encode(my_result[1][0])        
    feed_return = []
    bbcode_contents = []
    for item in my_result:
        #print item.content
        if item.content:
            item.content = transfer_html_to_bbcode(item.content)

    #print transfer_html_to_bbcode(my_result[1][0])
    context = {'site_title': site_title, 'feeds_result': my_result}
    #return HttpResponse(transfer_html_to_bbcode(my_result[1][0]))
    return render(request, 'feed_poster/feeds_list.html', context) 

