from django.urls import path

from .views import test, index, signup, contact, correotest

app_name = 'usuarios'
urlpatterns = [
    # path('test/', test, name='test'),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('accounts/signup/', signup, name='signup'),
    path('correotest/', correotest, name='correotest')
]