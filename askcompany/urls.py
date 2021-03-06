"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),  # TemplateView
    path('', RedirectView.as_view(
        pattern_name='instagram:post_list'
    ), name='root'),  # TemplateView
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
    path('__debug__/', include(debug_toolbar.urls)),  # debug_toolbar: template에 body태그가 있어야만 활성화된다.
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
