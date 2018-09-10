from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('challenges', views.challenges, name='challenges'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login_app', views.login_app),
    path('logout_app', views.logout_app),
    path('user_registration', views.user_registration),
]
