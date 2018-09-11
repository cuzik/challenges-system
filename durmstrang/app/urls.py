from django.urls import path

from durmstrang.app import views

urlpatterns = [
    path("", views.home.index, name="index"),
    path("challenges", views.challenges.index, name="challenges"),
    path("challenges/new", views.challenges.new, name="challenges_new"),
    path("sign_in", views.session.sign_in, name="sign_in"),
    path("sign_up", views.session.sign_up, name="sign_up"),
    path("login_app", views.session.login_app),
    path("logout_app", views.session.logout_app),
    path("user_registration", views.session.user_registration),
]
