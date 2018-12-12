from django.db import models
# Create your models here.
class EmfManager(models.Manager):
	def get_by_id(self,id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		else:
			return None

class Emf(models.Model):
	BIRTHDAY 		= 'BR'
	WEDDING 		= 'WD'
	DWEDDING 		= 'DW'
	ANNIVERSARY 	= 'AN'
	FESTIVE 		= 'FS'
	SPECIAL 		= 'SP'
	EVENT_CHOICES 	= (
			(BIRTHDAY,'Birthday'),
			(WEDDING,'Wedding'),
			(DWEDDING,'DWedding'),
			(ANNIVERSARY,'Anniversary'),
			(FESTIVE,'Festive'),
			(SPECIAL,'Special'),
		)

	title 		= models.CharField(max_length=60,blank=False,unique=True) #name of the firm
	city 		= models.CharField(max_length=25,blank=False) 	#main city of operation
	region 		= models.CharField(max_length=25)				#region of operation 
	email 		= models.EmailField(blank=True,					#email
									unique=True,
									max_length=25)
	phone 		= models.CharField(max_length=12,blank=False,unique=True,) #phone no (to be changed later)
	event       = models.CharField(max_length=2,choices=EVENT_CHOICES,default=BIRTHDAY) 
	events 	 	= models.CharField(max_length=120,blank=True,default="Birthday,Wedding,Destnation Wedding, Anniverary,Festive Party,Special")	
	specialty 	= models.CharField(max_length=20,blank=False,default='')

	objects 	= EmfManager()  #objects = QuerySet()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

