from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'add-user/', views.add_user, name='add_user'),
    url(r'login-user/', views.login_user, name='login_user'),
    url(r'logout-user/', views.logout_user, name='logout_user'),
]
