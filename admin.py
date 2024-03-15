from django.contrib import admin
from .models import Page, Post, Song
# Register your models here
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_publish','user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['post_title','post_cat','post_publish_date','user']

# @admin.register(Song)
# class SongAdmin(admin.ModelAdmin):
#     list_display=['songname','songduration','writtenby']
    

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'written_by_name')  # replace 'written_by__name' with the correct reference
    def written_by_name(self, obj):
        return obj.written_by.name
    written_by_name.short_description = 'Written By'


