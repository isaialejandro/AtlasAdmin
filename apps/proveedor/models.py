import uuid
from datetime import datetime, timedelta

from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html


class Responsable(models.Model):
	"""
	COMPRAS
	RECEPCION
	DIRECCION
	etc
	"""
	nombre = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.nombre

class Placa(models.Model):

	placa = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.placa

class Material(models.Model):

	class Meta:
		verbose_name_plural = 'Materiales'

	nombre = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.nombre

class Compania(models.Model):

	class Meta:
		verbose_name_plural = 'Compañias'

	nombre = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.nombre


class Proveedor(models.Model):

	class Meta:
		verbose_name_plural = 'Proveedores'
	
	uuid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
	entrada = models.DateTimeField(default=timezone.now)
	operador = models.CharField(max_length=50, blank=False, null=False)
	compania = models.ForeignKey('Compania', on_delete=models.SET_NULL, null=True)
	material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
	placa = models.ForeignKey('Placa', on_delete=models.SET_NULL, null=True)
	hora_inicio_descarga = models.TimeField(blank=True, null=True)
	hora_salida = models.TimeField(blank=True, null=True)
	# tiempo_estancia = models.CharField(max_length=50, blank=False, null=False) # Calculado
	observaciones = models.TextField(blank=True, null=True)
	responsable = models.ForeignKey('Responsable', on_delete=models.SET_NULL, null=True, related_name='responsable')
	programado = models.BooleanField(default=True)
	recibido = models.ForeignKey('Responsable', on_delete=models.SET_NULL, null=True)

	"""@admin.display
	def colored_name(self):
		return format_html(
			'<span style="color: #79CDD7;">{} {}</span>',
			self.operador,
			self.compania
		)"""

	# @property - To show in a custom HTML template. 
	@admin.display
	# Get the substraction of 2 dates:
	def tiempo_estancia(self):
		hr_entrada = self.entrada.time()
		hr_salida = self.hora_salida

		hr_entrada = timedelta(hours=hr_entrada.hour, minutes=hr_entrada.minute)
		hr_salida = timedelta(hours=hr_salida.hour, minutes=hr_salida.minute)
		tiempo_estancia = hr_salida - hr_entrada

		return f'{tiempo_estancia} hrs.'

	def __str__(self):
		return self.operador

