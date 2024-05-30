from django.contrib import admin
from .models import Customer, Post, Project, Comment, SlideshowImage, FAQ, NewsUpdate, NewsLetter

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    ordering = ['user__first_name', 'user__last_name']
    list_select_related = ['user']
    search_fields = ['first_name__istartswith', 'last_name__istartswith' ]
    fields = ['user', 'phone'] 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['author', 'created_at', 'updated_at']



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'created_by']
    search_fields = ['name', 'description']
    list_filter = ['start_date', 'end_date', 'created_by']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
    search_fields = ['post__title', 'author__username']
    list_filter = ['created_at']



@admin.register(SlideshowImage)
class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'caption']
    search_fields = ['caption']



@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question']
    search_fields = ['question']



@admin.register(NewsUpdate)
class NewsUpdateAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    search_fields = ['title', 'description']
    list_filter = ['date']



@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']
