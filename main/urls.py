from django.urls import path
from . import views
from .views import MainPage, Reg, Log, logout_user, DeletePost,UpdatePost
from django.conf.urls import url

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('reg', Reg.as_view(), name='registration'),
    path('log', Log.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('addpost', views.addpost.as_view(), name='addpost'),
    path('<int:pk>/delete/', DeletePost.as_view(), name='delete'),
    path('<int:pk>/update/', UpdatePost.as_view(), name='update')


]
