from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField  # Библиотека для изменения размера изображений

class Category(models.Model):
  name = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('store:product_list_by_category', args=[self.slug])
  

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  name = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200)
#  image = models.ImageField(upload_to='products', blank=True)
  image = ResizedImageField(
      upload_to='products/images/',  # Папка для загрузки изображений
      size=[800, 800],  # Размер, до которого будет изменено изображение
      quality=85,  # Качество изображения (от 0 до 100)
      force_format='JPEG',  # Формат изображения
      blank=True,
      null=True
  )
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  is_available = models.BooleanField(default=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('store:product_detail', args=[self.id, self.slug])
  
