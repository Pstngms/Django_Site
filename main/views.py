from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from .forms import *
from .models import *


def about(request):
    return render(request, 'main/about.html')


def pageNotFound(request, exception):
    return render(request, 'main/404.htm')


def log(request):
    return render(request, 'main/log.html')


class addpost(CreateView):
    form_class = AddPost
    template_name = 'main/addpost.html'
    success_url = reverse_lazy('home')


class MainPage(ListView):
    paginate_by = 3
    model = Project
    queryset = Project.objects.order_by('-time_create')
    template_name = 'main/index.html'
    context_object_name = 'posts'


class Reg(CreateView):
    form_class = UserCreationForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('login')


class Log(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/log.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class DeletePost(DeleteView):
    model = Project
    success_url = reverse_lazy('home')
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UpdatePost(UpdateView):
    model = Project
    form_class = AddPost
    template_name = 'main/addpost.html'
    success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super(Projects, self).form_valid(form)
