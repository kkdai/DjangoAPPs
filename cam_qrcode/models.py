from django.db import models

# Create your models here.

class Camera(models.Model):
    camera_id = models.CharField(max_length=200)
    camera_name = models.CharField(max_length=200)
    camera_xmpp_account = models.CharField(max_length=200)
    camera_xmpp_password = models.CharField(max_length=200)
 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
 
    def __unicode__(self):
        return self.camera_name