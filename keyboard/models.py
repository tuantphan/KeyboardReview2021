from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class KeyboardType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='keyboardtype'

class KeyboardName(models.Model):
    keyboardname=models.CharField(max_length=255)
    keyboardtype=models.ForeignKey(KeyboardType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    keyboardurl=models.URLField()
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.keyboardname

    class Meta:
        db_table='keyboardname'

class KeyboardReview(models.Model):
    keyboardname=models.ForeignKey(KeyboardName, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    dateentered=models.DateField()
    keyboardimage=models.URLField()
    keyboardreview=models.TextField()

    def __str__(self):
        return self.keyboardimage

    class Meta:
        db_table='keyboardimage'
