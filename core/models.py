from django.db import models
from django.conf import settings
from django.contrib import admin

# Create your models here.
# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

    @admin.display(ordering='user__first_name')
    def first_name(self):
         return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
         return self.user.last_name
    

    class Meta:
        ordering = ['user__first_name', 'user__last_name']



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'




class SlideshowImage(models.Model):
    image = models.ImageField(upload_to='slideshow_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else 'Slideshow Image'



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question



class NewsUpdate(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    date = models.DateField()
    description = models.TextField()
    full_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    



class NewsLetter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    

    def __str__(self):
        return self.name

