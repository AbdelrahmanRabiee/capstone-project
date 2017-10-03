"""multichat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *
from django.contrib.auth.views import(
    password_reset,
    password_reset_done,
    password_reset_complete,
    password_reset_confirm,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$',login_view),
    url(r'^logout/$',logout_view,),
    url(r'^dbdump/$',dbdump),
    url(r'^inbox/$',home),
    url(r'^send-message/$',send_message),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',home),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]

# url for password reset
urlpatterns += [

    url(r'^password-reset/$', password_reset, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
]

#for API Registeration
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'profile'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
