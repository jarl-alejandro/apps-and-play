from django.db import models


class App(models.Model):
	titulo = models.CharField(max_length = 140)
	imagen = models.ImageField(upload_to="imagen")
	url = models.CharField(max_length = 300)
	detalle = models.CharField(max_length = 300)

	def __unicode__(self):
		return self.titulo

class Equipo(models.Model):
	nombre = models.CharField(max_length = 140)
	cargo = models.CharField(max_length = 140)
	frase = models.CharField(max_length = 140)
	avatar = models.ImageField(upload_to = 'avatar')
	facebook = models.CharField(max_length = 140, default = '')
	twitter = models.CharField(max_length = 140, default = '')

	def __unicode__(self):
		return "%s (%s)" % (self.nombre, self.cargo)

class Nosotros(models.Model):
	nosotros = models.TextField(default = '')
	mision = models.TextField(default = '')
	vision = models.TextField(default = '')

	class Meta:
		verbose_name = u'Nosotro'

	def __unicode__(self):
		return self.nosotros