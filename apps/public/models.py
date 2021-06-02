from django.db import models

# Create your models here.

class Prediction(models.Model):
    date = models.DateField(max_length=40)
    sp = models.IntegerField()
    nq = models.IntegerField()
    dw = models.IntegerField()
    
    def __str__(self):
        label = self.date
        label = label.strftime("%Y/%m/%d")
        return label