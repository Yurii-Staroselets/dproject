from django.contrib import admin
from .models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'salary', 'shop']

# Register your models here.
