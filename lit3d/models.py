from django.db import models

class ProjectCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название раздела")
    description = models.TextField(blank=True, verbose_name="Описание раздела")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Раздел проектов"
        verbose_name_plural = "Разделы проектов"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects",
        verbose_name="Раздел проектов"
    )
    date = models.DateField(verbose_name="Дата проекта", null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано?")
    preview_image = models.ImageField(upload_to="projects/previews/", verbose_name="Превью проекта", null=True, blank=True)
    large_image = models.ImageField(upload_to="projects/large/", verbose_name="Большая картинка проекта", null=True, blank=True)
    video = models.FileField(upload_to="projects/videos/", blank=True, null=True, verbose_name="Видео для проекта")
    short_description = models.TextField(verbose_name="Краткое описание", null=True, blank=True)
    full_description = models.TextField(verbose_name="Подробное описание", null=True, blank=True)
    content = models.TextField(verbose_name="Контент (HTML)", null=True, blank=True)
    order_number = models.PositiveIntegerField(default=0, verbose_name="Порядковый номер", null=True, blank=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class Employee(models.Model):
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True, verbose_name="Фото сотрдуника")
    name = models.CharField(max_length=255, verbose_name="Имя")
    position = models.CharField(max_length=255, verbose_name="Позиция")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано?")
    order_number = models.PositiveIntegerField(default=0, verbose_name="Порядковый номер", null=True, blank=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона")
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name="email")
    instagram_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="Instagram URL")
    vk_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="VK URL")
    pinterest_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="Pinterest URL")
    behance_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="Behance URL")

    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"

    def __str__(self):
        return f"Контактные данные"


class Slogans(models.Model):
    main_heading = models.TextField(max_length=1024)
    main_subheading = models.TextField(max_length=1024)
    about_heading = models.TextField(max_length=1024)
    about_text = models.TextField(max_length=1024)
    slogan = models.TextField(max_length=1024)
    contact_heading = models.TextField(max_length=1024)
    contact_subheading = models.TextField(max_length=1024)

    class Meta:
        verbose_name = "Слоганы"
        verbose_name_plural = "Слоганы"

    def __str__(self):
        return "Объект слоганов"