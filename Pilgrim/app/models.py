from django.db import models





class zapis(models.Model):
    # id = models.IntegerField()
    soderjanie = models.CharField(max_length=333)
    
    def __str__(self):
     return f" Zapis {self.id}: {self.soderjanie} "






















