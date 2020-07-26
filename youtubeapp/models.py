from django.db import models
from django.contrib.auth.models import User



class Vedio(models.Model):
	Title 		= models.CharField(max_length=300)
	Discription = models.CharField(max_length=300)
	path		= models.FileField(upload_to='documents/')
	user        = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on	= models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
	text 		= models.CharField(max_length=300)
	user        = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on	= models.DateTimeField(auto_now_add=True)
	video 		= models.ForeignKey(Vedio, on_delete=models.CASCADE)
