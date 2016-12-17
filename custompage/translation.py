from modeltranslation.translator import translator
from mezzanine.core.translation import TranslatedRichText
from custompage.models import CustomPage


class TranslatedCustomPage(TranslatedRichText):
    fields = ()

    
translator.register(CustomPage, TranslatedCustomPage)
