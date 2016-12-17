from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import RichText
from mezzanine.pages.models import Page


class CustomPage(Page, RichText):
    '''
    A page representing the format of the custom page
    '''

    class Meta:
        verbose_name = _("Custom page")
        verbose_name_plural = _("Custom pages")
