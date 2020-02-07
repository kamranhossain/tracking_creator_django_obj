from django.db import models
from .middleware import local

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, **NULL_AND_BLANK)

    def save(self, *args, **kwargs):
        if self.pk is None and hasattr(local, 'user'):
            self.creator = local.user
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True