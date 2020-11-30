from django.contrib import admin
from .models import processo
from .models import cadastro_processo

# Register your models here.
admin.site.register(processo)
admin.site.register(cadastro_processo)