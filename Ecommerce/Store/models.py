from django.db import models

# Create your models here.

class Additem(models.Model):
	Itname = models.CharField(max_length = 30)
	price = models.DecimalField(decimal_places=2,max_digits=8)
	itimg = models.ImageField(upload_to='itemimages/',default='ics.jpg')


	def __str__(self):
		return self.Itname
	
class Itemlist(models.Model):
	p = [('AV','available'),('NA','not available'),('DF','Select availability')]
	iname = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=2,max_digits=8)
	iimage = models.ImageField(upload_to='itemimages/',default='ics.jpg')
	itavailability = models.CharField(choices=p,default="DF",max_length=20)