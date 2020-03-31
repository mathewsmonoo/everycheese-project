#from django_extensions.db.fields import AutoSlugField
from django.db import models
from django_countries.fields import CountryField


#from models_utils.models import TimeStampedModel

#TimeStampedModel automatically gives the model created and modified fields
#We like to define all our models as subclasses of TimeStampedModel

class Cheese(models.Model):
    name = models.CharField("Name of Cheese", max_length=255)
    #slug = models.AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
    slug = models.SlugField(default=name)
    description = models.TextField("Description", blank=True)
    country_of_origin = CountryField("Country of Origin", blank=True)
    
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft","Semi-Soft"
        SEMI_HARD = "semi-hard","Semi-Hard"
        HARD =  "hard","Hard"

    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    def __str__(self):
        return self.name