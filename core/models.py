from django.db import models
from django.utils import timezone

class Company(models.Model):
	company_name = models.CharField(max_length=100, unique=True)
	Address = models.CharField(max_length=50)
	Location = models.CharField(max_length=30)
	job_title = models.CharField(max_length=100)
	Description = models.TextField(max_length=4000)
	Date = models.DateTimeField(default=timezone.now)
	Rank = models.CharField(max_length=30)
	Roles = models.TextField(max_length=500)