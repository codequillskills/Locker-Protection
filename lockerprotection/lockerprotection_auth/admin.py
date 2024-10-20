from django.contrib import admin
from .models import Data

class AdminData(admin.ModelAdmin):
    list_display = ('id', 'user', 'fileName', 'description', 'fileUpload')
    search_fields = ('user', 'fileName', 'description')
    list_filter = ('user', 'fileName', 'description')

admin.site.register(Data, AdminData)
