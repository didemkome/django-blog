from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class BaseModel(models.Model):
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
        )
    update_at = models.DateTimeField(
        auto_now=True, 
        verbose_name=_('updated at')
    )
    class Meta:
        abstract = True

class PostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=Post.POST_STATUS_ONLINE)
    
    def latest_posts(self, amount=5):
        return self.active().order_by('-update_at')[:amount]
    
class Post(BaseModel):

    POST_STATUS_OFF = 0
    POST_STATUS_ONLINE = 1
    POST_STATUS_DRAFT = 2

    POST_STATUS_CHOICE = (
        (POST_STATUS_OFF, 'Off'),
        (POST_STATUS_ONLINE, 'Online'),
        (POST_STATUS_DRAFT, 'Draft'), 
    )

    status = models.IntegerField(
        choices=POST_STATUS_CHOICE, 
        default=POST_STATUS_ONLINE,
        verbose_name=_('status'),
    )
    title = models.CharField(
        max_length=255, 
        verbose_name=_('title'),
    )
    body = models.TextField(verbose_name=_('body of post'))

    objects = models.Manager()
    custom_objects = PostQuerySet.as_manager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])
        # '/blog/{pk}/'.format(pk=self.pk)

    def get_update_url(self):
        return reverse('post-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('post-delete', args=[self.pk])