from django.contrib import admin

# Register your models here.

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered


app_models = apps.get_app_config('rdiapp').get_models()

class DynamicModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

for model in app_models:
   try:
#        admin.site.register(model)
        admin_class = type(f'{model.__name__}Admin', (DynamicModelAdmin,), {})
        admin.site.register(model, admin_class)
   except AlreadyRegistered:
       pass