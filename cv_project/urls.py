"""cv_project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from cv.views import IndexView, XpView, CategoryView, AbilitieView, SpareTimeView, ExperienceView, EducationView, EducView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^exp/$', ExperienceView.as_view(), name='experiences'),
    url(r'^educ/$', EducationView.as_view(), name='education'),
    url(r'^abilities/$', AbilitieView.as_view(), name='skills'),
    url(r'^sparetime/$', SpareTimeView.as_view(), name='spare-time'),
    url(r'^experience/(?P<slug>[-\w]+)/$', XpView.as_view(), name='experience-detail'),
    url(r'^education/(?P<slug>[-\w]+)/$', EducView.as_view(), name='education-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
