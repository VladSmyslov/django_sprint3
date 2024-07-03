from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
        'description'
    )
    search_fields = ('title', )
    list_filter = ('is_published', )
    list_display_links = ('title', )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'text',
        'is_published',
        'author',
        'category'
    )
    search_fields = ('title', 'category', )
    list_filter = ('author', 'category', 'location', 'is_published', )
    list_display_links = ('title', )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published', )
    search_fields = ('name', )
    list_filter = ('is_published', )
    list_display_links = ('name', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
