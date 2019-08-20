from django.contrib import admin

from core.models import Picture, BackColor


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
	pass


@admin.register(BackColor)
class BackColorAdmin(admin.ModelAdmin):
	pass