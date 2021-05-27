from django.db import models
from django.forms import ModelForm

class Branza(models.Model):
	branza=models.CharField(max_length=50)
	def __str__(self):
		return self.branza
class Branza_sub(models.Model):
	branza_sub=models.CharField(max_length=50)
	def __str__(self):
		return self.branza_sub
class Kraj(models.Model):
	kraj=models.CharField(max_length=50)
	def __str__(self):
		return self.kraj

class Miasto(models.Model):
	miasto=models.CharField(max_length=50)
	def __str__(self):
		return self.miasto

class Lista(models.Model):
	nazwa=models.CharField(max_length=50)
	miasto=models.ForeignKey(Miasto,on_delete=models.CASCADE)
	kraj=models.ForeignKey(Kraj,on_delete=models.CASCADE)
	branza=models.ForeignKey(Branza,on_delete=models.CASCADE)
	sub_branza=models.ForeignKey(Branza_sub,on_delete=models.CASCADE)
	wyskosc=models.FloatField()
	szerokosc=models.FloatField()
	logo=models.ImageField(upload_to='database/logos/', height_field=None, width_field=None, max_length=100,)
	strona=models.URLField(max_length=200)
	
class BranzaForm(ModelForm):
	class Meta:
		model = Lista
		fields = ['branza']

class KrajForm(ModelForm):
	class Meta:
		model = Lista
		fields = ['kraj']
		
