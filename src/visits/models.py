from django.db import models

# Create your models here.
class PageVisits(models.Model):
   # id ->hidden-> primary key ->autofield->1,2 3,4,5
   path =models.TextField(null=True, blank=True) #col 
   timestamp = models.DateTimeField(auto_now_add=True) # auto_now=True #col    
