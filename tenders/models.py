from django.db import models


class Procurer(models.Model):
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class Contractor(models.Model):
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Tender(models.Model):
    number = models.IntegerField
    date = models.DateField('date published')
    procurer = models.ForeignKey(Procurer, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
