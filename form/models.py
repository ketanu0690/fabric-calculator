from django.db import models

# Create your models here.
class EndUser(models.Model):
    End_User = models.CharField(max_length=100)
    
    def __str__(self):
        return self.End_User

class Fabricprop(models.Model):
    fabric_Type = models.CharField(max_length=100)
    fabric = models.ForeignKey("Fabric",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fabric_Type
    
    def __unicode__(self):
        return u'%s' % self.fabric_Type

    

class Fabric(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.name    

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.name


