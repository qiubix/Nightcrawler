from django.db import models


class Procurer(models.Model):
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        return self.company_name

    def hasLocation(self):
        if self.latitude is None or self.longitude is None:
            return False
        else:
            return True


class Contractor(models.Model):
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        return self.company_name


class Tender(models.Model):
    number = models.IntegerField
    date = models.DateField('date published')
    procurer = models.ForeignKey(Procurer, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
