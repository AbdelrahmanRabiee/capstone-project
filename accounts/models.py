# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender",null=True)
     reciever = models.ForeignKey(User, related_name="receiver",null=True)
     message_content = models.CharField(max_length=250,null=True,blank=True)
     creation_time = models.DateTimeField(null=True,auto_now_add=True)

     def __str__(self):
         return self.message_content





