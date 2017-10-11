from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

from django.core.urlresolvers import reverse
from django.views import generic

from groups.models import Group,GroupMember
# Create your views here.

class CreateGrup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGrup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
