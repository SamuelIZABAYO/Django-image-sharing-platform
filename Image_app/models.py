from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.urls import reverse


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',
                         unique=True,
                         db_index=True,
                         max_length=200,
                         editable=False,
                         )
    url = models.URLField()
    image = models.ImageField(
        upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail',
                       kwargs={'id': self.id,
                               'slug': self.slug})
