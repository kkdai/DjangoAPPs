from cam_qrcode.models import Camera
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
import simplejson as json2

# Create your views here.
main_url = "http://evan-web-apis.herokuapp.com/cam_qrcode/"

def index(request):
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
    out_obj = json2.dumps(response_data)
    return HttpResponse(out_obj, content_type="application/json")

def detail(request, cam_id):
    global main_url
    json_url = main_url + str(cam_id)+ "/json"
    
    cam = get_object_or_404(Camera, pk=cam_id)
    context = {'cam_url_id': cam_id, "full_url": json_url, "camera_name":cam.camera_name, "camera_xmpp_account":cam.camera_xmpp_account, "camera_xmpp_password": cam.camera_xmpp_password}
    return render(request, 'cam_qrcode/detail.html', context) 

def remove(request, cam_id):
    instance = Camera.objects.get(id=cam_id)
    instance.delete()
    return HttpResponse('Remove Done <br><a href="/cam_qrcode">Home</a></br>')

def add(request):
    return render(request, 'cam_qrcode/add_form.html') 

def add_cam(request):
    cam_name = request.POST['cam_name']
    xmpp_acc = request.POST['xmpp_account']
    xmpp_pw = request.POST['xmpp_password']
    cam_new_id = Camera.objects.all().count() + 1
    add_obj = Camera(camera_id=cam_new_id, camera_name=cam_name, camera_xmpp_account=xmpp_acc, camera_xmpp_password=xmpp_pw)
    add_obj.save()
    return HttpResponse('Add done <br><a href="/cam_qrcode">Home</a></br>')
