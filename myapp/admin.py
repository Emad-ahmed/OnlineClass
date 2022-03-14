from django.contrib import admin
from django.db import models
from myapp.models import CreateClass, JoinClass, AddClassWork, CommentinClass, WorkdoneClass, ProfileClass
# Register your models here.


@admin.register(CreateClass)
class CreateClassAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(JoinClass)
class JoinClassAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(AddClassWork)
class AddClassWorkAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(CommentinClass)
class CommentinClassAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(WorkdoneClass)
class WorkdoneClassAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ProfileClass)
class ProfileClassAdmin(admin.ModelAdmin):
    list_display = ['id']