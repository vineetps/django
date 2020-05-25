from django.db import models

# Create your models here.

class ShareDetails(models.Model):
    company_name = models.CharField(max_length=16 ,unique=True)
    date_bought = models.DateField()
    shares_bought = models.IntegerField()
    share_price = models.FloatField()

    def __str__(self):
        return str(self.company_name)