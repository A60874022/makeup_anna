from django.contrib import admin

from gallery.models import Gallery, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('tags', 'image', 'pub_date')
    search_fields = ('tags',)
    list_filter = ('pub_date',)
