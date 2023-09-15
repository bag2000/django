from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"


class IP(models.Model):
    name = models.CharField(max_length=15, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    allow_ports = models.CharField(max_length=250)
    open_ports = models.CharField(max_length=70)
    status = models.CharField(max_length=7)
    update_time = models.CharField(max_length=20, default='Не сканировался')
    scanning_now = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.company}"
