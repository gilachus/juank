from django.db import models


class Usuario(models.Model):

	numero_id = models.CharField(max_length=50)
	tipo_documento = models.CharField(default="cédula", max_length=50)