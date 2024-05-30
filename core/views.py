from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views import View
from .models import Post, Project, Comment, SlideshowImage, FAQ, NewsUpdate
from .forms import NewsLetterForm

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        projects = Project.objects.all()
        slideshow_images = SlideshowImage.objects.all()
        faqs = FAQ.objects.all()
        news_updates = NewsUpdate.objects.all()
        form = NewsLetterForm()
        return render(request, 'core/home.html', {
            'posts': posts,
            'projects': projects,
            'slideshow_images': slideshow_images,
            'faqs': faqs,
            'news_updates': news_updates,
            'form': form,
            
        })

    def post(self, request):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        posts = Post.objects.all()
        projects = Project.objects.all()
        slideshow_images = SlideshowImage.objects.all()
        faqs = FAQ.objects.all()
        news_updates = NewsUpdate.objects.all()
        return render(request, 'core/home.html', {
            'posts': posts,
            'projects': projects,
            'slideshow_images': slideshow_images,
            'faqs': faqs,
            'news_updates': news_updates,
            'form': form,
        })


class LoginView(View):
    def get(self, request):
        return render(request, 'core/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid username or password'})

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'core/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('home')
        return render(request, 'core/register.html', {'form': form})

class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        return render(request, 'core/post_detail.html', {'post': post, 'comments': comments})

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('post_detail', pk=pk)
