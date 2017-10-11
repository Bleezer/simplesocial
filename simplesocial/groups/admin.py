from django.contrib import admin
from . import models

# Register your models here.
# Ezzel a TabularInline-nal beállítjuk hogy az Admin felületen is lehessen szerkezteni, ilyenkor már nem kell külön regisztrálni a GroupMember-t 
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember



admin.site.register(models.Group)
