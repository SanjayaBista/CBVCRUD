from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='draft')
    author = models.CharField(max_length=500) 

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk': self.pk})