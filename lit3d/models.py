from django.db import models
from django.utils.text import slugify
import datetime

class PortfolioPage(models.Model):
    # Выпадающий список для section
    SECTION_CHOICES = [
        ('russia', 'Выставка Россия'),
        ('rmi', 'Россия - моя история'),
        ('exhibition', 'Выставочные пространства'),
        ('PDA', 'PlayDigital Art'),
        ('concepts', 'Концепты'),
    ]
    
    # Основные поля
    title = models.CharField('Название проекта', max_length=200)
    slug = models.SlugField('URL-адрес', max_length=200, unique=True, blank=True)
    section = models.CharField(
        'Раздел', 
        max_length=50, 
        choices=SECTION_CHOICES,
        default='exhibition'
    )
    date = models.DateField(default=datetime.date(2023, 1, 1), verbose_name='Дата проекта')
    
    # Текстовые блоки
    description_short = models.TextField('Краткое описание', max_length=500, blank=True, null=True)
    description_extended = models.TextField('Подробное описание', blank=True, null=True)
    content = models.TextField('Контент (HTML)', blank=True, null=True)
    
    # Изображения
    # main_image = models.ImageField(
        # 'Главное изображение',
        # upload_to='portfolio/main_images/'
    # )
    
    # Мета-поля
    is_active = models.BooleanField('Опубликовано', default=True)
    order = models.PositiveIntegerField('Порядок сортировки', default=0)
    
    class Meta:
        verbose_name = 'Страница проекта'
        verbose_name_plural = 'Страницы проектов'
        ordering = ['-date', 'order']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.get_section_display()} - {self.title}"
    
    @property
    def year(self):
        return self.date.year