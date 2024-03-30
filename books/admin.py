from django.contrib import admin

from books import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags",)
    autocomplete_fields = ("category",)


class BookInline(admin.StackedInline):
    model = models.Book
    fields = ("title",)
    readonly_fields = ("title",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    inlines = [
        BookInline,
    ]


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    ...
