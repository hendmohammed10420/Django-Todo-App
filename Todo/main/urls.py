from django.urls import path
from . import views
urlpatterns = [
  path('', views.home,name='home'),
  path('detailed/<str:id>', views.detailed,name='detailed'),
  path('create/', views.create,name='create'),
  path('update/<str:id>', views.update,name='update'),
  path('delete/<str:id>', views.delete,name='delete'),
    path('signup', views.createUser, name='signup'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout')
  
]
