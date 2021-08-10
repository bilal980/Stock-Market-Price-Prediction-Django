from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

admin.site.site_header = 'Fox trading Admin'
admin.site.site_title = 'Fox trading Admin'
admin.site.index_title = "Welcome to Fox trading Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.foxLogin,name='login_page'),
    path('signup/', views.foxSignup, name='signup'),
    path('login/', views.handleLogin, name='login'),
    path('accounts/login/', views.handleLogin, name='login'),
    path('logout/', views.foxLogout, name='logout'),
    path('register/', views.handleSignup, name='register'),
    path('home/', views.foxHome, name='home'),
    path('about/', views.about, name='about'),
    path('password/', views.change_password, name='change_password'),

    path('blog/', include('blog.urls')),
    path('trading/', include('trading.urls')),

    # Forget Password
    path('reset_password/',  auth_views.PasswordResetView.as_view(),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
