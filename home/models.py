# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Drill(models.Model):

    #__Drill_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE)

    #__Drill_FIELDS__END

    class Meta:
        verbose_name        = _("Drill")
        verbose_name_plural = _("Drill")


class Location(models.Model):

    #__Location_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)

    #__Location_FIELDS__END

    class Meta:
        verbose_name        = _("Location")
        verbose_name_plural = _("Location")



#__MODELS__END
