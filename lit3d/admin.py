from django.contrib import admin
from .models import Project, ProjectCategory, Employee, ContactInfo, Slogans


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "description")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "date", "is_published")
    list_filter = ("is_published", "category", "date")
    search_fields = ("title", "short_description", "full_description")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "is_published")
    list_filter = ("name", "position", "is_published")
    search_fields = ("name", "position")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "email", "instagram_url", "vk_url", "pinterest_url", "behance_url")


@admin.register(Slogans)
class ContactInfoAdmin(admin.ModelAdmin):
    ...