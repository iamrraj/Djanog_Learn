from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [

    
    path('login', auth_views.login, {'template_name': 'login.html'}, name='login'), # For Login
    path('signup', views.signup, name='signup'), # For SignUp
    path('logout', auth_views.logout, {'next_page': 'login'}, name='logout'), # For Auth Logout
    path('detail', views.detail, name='detail'), # For View User Deatils After Login

    
    # path('settings', views.settings, name='settings'),
    path('settings/password', views.password, name='password'),  # This is For Change Password

    path('oauth/', include('social_django.urls', namespace='social')),  # This is For Social Login
]

    

