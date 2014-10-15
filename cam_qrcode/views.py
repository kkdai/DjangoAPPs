from cam_qrcode.models import Camera
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
import simplejson as json2

# Create your views here.
main_url = "http://localhost:8000/cam_qrcode/"

def index(request):
    print "enter index"
    latest_cam_list = Camera.objects.all()
    context = {'latest_cam_list': latest_cam_list}
    return render(request, 'cam_qrcode/index.html', context) 

def json(request, cam_id):
    cam = get_object_or_404(Camera, pk=cam_id)
    response_data = {}
    response_data['cam_id'] =  cam.camera_id
    response_data['camera_name'] = cam.camera_name
    response_data['camera_xmpp_account'] = cam.camera_xmpp_account
    response_data['camera_xmpp_password'] = cam.camera_xmpp_password
    print "List data: ", response_data
    out_obj = json2.dumps(response_data)
    print "Json data: ", out_obj
    return HttpResponse(out_obj, content_type="application/json")

def detail(request, cam_id):
    print "enter detail on", cam_id
    global main_url
    json_url = main_url + str(cam_id)+ "/json"
    print json_url
    context = {'cam_url_id': cam_id, "full_url": json_url}
    return render(request, 'cam_qrcode/detail.html', context) 

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
    return HttpResponse('Add done <br><a href="/cam_qrcode">Home</a></br>')
