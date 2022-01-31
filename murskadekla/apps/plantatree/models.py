from django.db import models
from django.db.models.signals import pre_save

import datetime
import hashlib

# Create your models here.
class PlantATreeKey(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=8, blank=True, null=True)
    activated = models.BooleanField(default=False)
    LOT = models.CharField(max_length=5)
    GTIN = models.CharField(max_length=14) #planiram maknuti to sve nepotrebno i raditi kodove negdje drugdje
    timestamp = models.DateTimeField(auto_now_add=True)
    activated_time = models.DateTimeField()

def pre_save_plant_a_tree_key(sender, instance, *args, **kwargs):
    if not instance.activated:
        if not instance.key:
            year = str(datetime.datetime.now().year)
            month = str(datetime.datetime.now().month)
            day = str(datetime.datetime.now().day)
            hour = str(datetime.datetime.now().hour)
            minute = str(datetime.datetime.now().minute)
            second = str(datetime.datetime.now().second)
            microsecond = str(datetime.datetime.now().microsecond)
            gtin = instance.GTIN
            lot = instance.LOT
            key_string = year + month + day + hour + minute + second + microsecond + gtin + lot

            instance.key = hashlib.shake_256(key_string.encode()).hexdigest(4)

pre_save.connect(pre_save_plant_a_tree_key, sender=PlantATreeKey)

