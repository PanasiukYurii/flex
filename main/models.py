from django.db import models


# Create your models here.
class Flex(models.Model):
    message = models.CharField(max_length=28)

    def __str__(self):
        return "%s" % self.message
