"""pg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from emfs.views import EmfListView, EmfDetailView 
from accounts.views import RegisterView, LoginView, login_page
from pages.views import home_view,about_view, contact_view,register_view,logout_view, coming_soon
from search import urls

urlpatterns = [
	path('',home_view,name='home'),
   # path('login/',login_view,name='login'),
    path('admin/', admin.site.urls),
    path('login/',login_page,name='login'), #earlier used
    path('logout/',logout_view,name='logout'),
    
    # path('register/',register_view,name='register'), #earilier used
    path('register',RegisterView.as_view(),name='register'),
    # path('login/',LoginView.as_view(),name='login'),
    
    path('contact/',contact_view,name='contact'),
    path('about/',about_view,name='about'),
    
    path('emfs/',EmfListView.as_view(),name='emfs'),
    path('emfs/<int:pk>/',EmfDetailView.as_view(),name='emfsd'), 
    path('search/',include('search.urls',namespace='search')),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)