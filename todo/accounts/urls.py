from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'add-user/', views.add_user, name='add_user'),
]
