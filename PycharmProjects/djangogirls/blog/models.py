from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    class Meta:

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'