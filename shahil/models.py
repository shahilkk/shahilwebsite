from django.db import models


class Details(models.Model):
    name = models.CharField(max_length=3000) 
    email = models.CharField(max_length=30000)
    address =  models.CharField(max_length=30000)
    def __str__(self):
        return self.name