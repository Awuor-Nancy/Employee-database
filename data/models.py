from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=25)
    eid = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    econtact = models.CharField(max_length=100)

    def __str__(self):
        return '%s' %(self.ename)

class Meta:
            db_table = "employee"
