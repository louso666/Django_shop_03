from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название тега')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Тег блога'
        verbose_name_plural = 'Теги блога'

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(BlogTag, related_name='posts', verbose_name='Теги')
    content = CKEditor5Field(verbose_name='Содержание')
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True, verbose_name='Изображение')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    date_published = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'
        ordering = ['-date_published']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.date_published:
            self.date_published = timezone.now()
        super().save(*args, **kwargs)
