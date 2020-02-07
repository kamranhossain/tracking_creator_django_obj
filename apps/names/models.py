from django.db import models
from project.base import BaseModel

class Name(BaseModel):
    english_representation = models.CharField(max_length=100)
    vernacular_representation = models.CharField(max_length=100)

    def __str__(self):
        return self.english_representation
