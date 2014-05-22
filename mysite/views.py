from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return HttpResponse('test1')