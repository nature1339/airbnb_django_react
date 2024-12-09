from django.db import models
from common.models import CommonModel



# Create your models here.
class Room(CommonModel):
    """Room Model Definition"""


    country = models.CharField(max_length=50, default="한국",)
    
    name = models.CharField(max_length=180, default="",)
    
    city = models.CharField(max_length=80, default="서울",)
    price = models.PositiveBigIntegerField()
    rooms = models.PositiveBigIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250,)
    pet_friendly = models.BooleanField(default=True,)
    kind = models.CharField(
        max_length=20, choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    
    amenities = models.ManyToManyField("rooms.Amenity",)
    def __str__(self) -> str:
        return self.name
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Amenity(CommonModel):
   """Amenity Definition"""
   name = models.CharField(max_length=150,)
   description = models.CharField(max_length=150 null=True,)
   
   def __str__(self) -> str:
       return self.name
   
   class Meta:
       verbose_name_plural="Amenities"
   
   