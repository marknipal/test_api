from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Groups(models.Models):
	account_id = models.AutoField(primary_key=True)
	hexcode = models.CharField(max_length=30)
	