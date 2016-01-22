from django.db import models


class Procurer(models.Model):
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Contractor(models.Model):
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
