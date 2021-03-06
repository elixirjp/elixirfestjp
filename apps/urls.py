"""apps URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from core import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^noc/$', TemplateView.as_view(template_name='noc.html'), name='noc'),
    url(r'^admin/', admin.site.urls),
]

if settings.PUBLICATION_STATUS == settings.PUBLICATION_STATUS_ACCEPTING:
    urlpatterns += [
        url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
        url(r'^entry/$', login_required(views.EntryFormView.as_view()), name='entry'),
        url(r'^entry/complete/$', TemplateView.as_view(template_name='form_complete.html'), name='entry-complete'),
        url(r'^auth/', include('social_django.urls', namespace='social')),
        url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    ]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
