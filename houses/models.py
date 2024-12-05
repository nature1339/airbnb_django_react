from django.db import models

# Create your models here.
class House(models.Model):
    
    """House Definition for Houses"""
    
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name='Price',help_text="Positive Numbers only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True,
        help_text="Does these allow pets?",)
      
    
    def _str_(self):
        return self.name