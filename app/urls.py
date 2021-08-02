
from django.urls import path
from .import views

urlpatterns = [
path('', views.home),
path('register', views.register , name="register"),
path('login', views.login , name="login"),
path('logout', views.logout, name="logout"),
path('blog',views.blog , name="blog"),
path('BlogDetail/<int:id>' , views.BlogDetail , name="BlogDetail"),
path('edit/<int:id>',views.edit , name="edit"),
path('delete/<int:id>',views.delete , name="delete"),
]
