from future.builtins import str

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.generic.fields import CommentsField, RatingField
from mezzanine.utils.models import AdminThumbMixin, upload_to


class PortfolioPost(Displayable, Ownable, RichText, AdminThumbMixin):
    """
    A Portfolio post.
    """

    categories = models.ManyToManyField("PortfolioCategory",
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="portfolioposts")
    
    rating = RatingField(verbose_name=_("Rating"))
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("portfolio.PortfolioPost.featured_image", "portfolio"),
        format="Image", max_length=255, null=True, blank=True)
    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("Portfolio post")
        verbose_name_plural = _("Portfolio posts")
        ordering = ("-publish_date",)

    def get_absolute_url(self):
        """
        URLs for Portfolio posts can either be just their slug, or prefixed
        with a portion of the post's publish date, controlled by the
        setting ``Portfolio_URLS_DATE_FORMAT``, which can contain the value
        ``year``, ``month``, or ``day``. Each of these maps to the name
        of the corresponding urlpattern, and if defined, we loop through
        each of these and build up the kwargs for the correct urlpattern.
        The order which we loop through them is important, since the
        order goes from least granular (just year) to most granular
        (year/month/day).
        """
        url_name = "portfolio_post_detail"
        kwargs = {"slug": self.slug}
        date_parts = ("year", "month", "day")
        if settings.BLOG_URLS_DATE_FORMAT in date_parts:
            url_name = "portfolio_post_detail_%s" % settings.BLOG_URLS_DATE_FORMAT
            for date_part in date_parts:
                date_value = str(getattr(self.publish_date, date_part))
                if len(date_value) == 1:
                    date_value = "0%s" % date_value
                kwargs[date_part] = date_value
                if date_part == settings.BLOG_URLS_DATE_FORMAT:
                    break
        return reverse(url_name, kwargs=kwargs)
        #return ''


class PortfolioCategory(Slugged):
    """
    A category for grouping Portfolio posts into a series.
    """

    class Meta:
        verbose_name = _("Portfolio Category")
        verbose_name_plural = _("Portfolio Categories")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return ("portfolio_post_list_category", (), {"category": self.slug})