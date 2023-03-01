from django.db import models
 
class Prezentare(models.Model):
# atribute

	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='PAG_prezentare/files/covers')
	