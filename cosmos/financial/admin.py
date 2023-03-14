from django.contrib import admin
from .models import CorpHistoricalModel
# Register your models here.
@admin.register(CorpHistoricalModel)
class CorpHistoricalAdmin(admin.ModelAdmin):
    pass