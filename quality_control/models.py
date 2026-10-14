from django.db import models

# Create your models here.

class RawMaterial(models.Model):
    supplier_name = models.CharField(max_length=100)
    purchase_order = models.CharField(max_length=50)
    material_grade = models.CharField(max_length=50)
    heat_number = models.CharField(max_length=50, unique=True)
    quantity = models.PositiveIntegerField()
    certificate_reference = models.CharField(max_length=100)
    received_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.heat_number
