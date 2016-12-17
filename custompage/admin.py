from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from custompage.models import CustomPage


admin.site.register(CustomPage, PageAdmin)