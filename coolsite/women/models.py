from django.db import models
from django.urls import reverse
# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотографии')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_ablsolut_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категроии'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_ablsolut_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.name
