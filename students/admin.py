from django.contrib import admin

# Register your models here.

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'course', 'fees')
    search_fields = ('name', 'email', 'course')
    list_filter = ('course',)