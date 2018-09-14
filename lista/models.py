# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Notas(models.Model):
	texto = models.CharField(max_length=100)
	creado = models.DateTimeField(auto_now_add=True)
	archivado = models.BooleanField(default=False)

	def __str__(self):
		return self.texto
