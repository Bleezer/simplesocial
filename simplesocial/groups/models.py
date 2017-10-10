from django.db import models
from django.utils.text import slugify # slugify(value) = If value is "Joel is a slug", the output will be "joel-is-a-slug"

# import misaka #  fast HTML renderer and functionality to make custom renderers
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    desciption = models.TextField(blank=True,default='')
    desciption_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*argrs,**kwargs):
        self.slug = slugify(self.name)
        self.desciption = self.desciption # itt lenne: misaka.html(self.desciption)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('group:singe',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='membership')
    user = models.ForeignKey(User,related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')
