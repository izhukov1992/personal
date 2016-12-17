from modeltranslation.translator import translator
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from portfolio.models import PortfolioCategory, PortfolioPost


class TranslatedPortfolioPost(TranslatedDisplayable, TranslatedRichText):
    fields = ()


class TranslatedPortfolioCategory(TranslatedSlugged):
    fields = ()

translator.register(PortfolioCategory, TranslatedPortfolioCategory)
translator.register(PortfolioPost, TranslatedPortfolioPost)