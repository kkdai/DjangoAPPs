from django.http import HttpResponse
from django.shortcuts import render
from cam_qrcode.models import Camera

# Create your views here.

def index(request):
    latest_cam_list = Camera.objects.all()
    context = {'latest_cam_list': latest_cam_list}
    return render(request, 'cam_qrcode/index.html', context) 

def detail(request):
    return HttpResponse('detail')

def results(request):
    return HttpResponse('results')

def add(request):
    return render(request, 'cam_qrcode/add_form.html') 

def add_cam(request):
    print "in add_cam"
    cam_name = request.POST['cam_name']
    print cam_name
    xmpp_acc = request.POST['xmpp_account']
    print xmpp_acc
    xmpp_pw = request.POST['xmpp_password']
    print xmpp_pw
    cam_new_id = Camera.objects.all().count() + 1
    add_obj = Camera(camera_id=cam_new_id, camera_name=cam_name, camera_xmpp_account=xmpp_acc, camera_xmpp_password=xmpp_pw)
    add_obj.save()
    return HttpResponse('Add done')
