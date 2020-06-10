"""steve_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('', core_views.homepage, name = "homepage"),
    path('snippets/', core_views.snippet_list, name ="snippet_list"),
    path('snippets/<int:snippet_pk>', core_views.show_snippet, name = 'show_snippet'),
    path('snippets/<int:snippet_pk>/', core_views.show_public_snippet, name = 'show_public_snippet'),
    path('snippets/create_snippet/', core_views.create_snippet, name='create_snippet'),
    path('snippets/<int:pk>/edit/', core_views.edit_snippet, name='edit_snippet'),
    path('snippets/<int:pk>/delete/', core_views.delete_snippet, name='delete_snippet'),
    path('tags/<str:tag_name>', core_views.view_tag, name='view_tag'),
    path('snippets/search/', core_views.search_snippets, name='search_snippets'),
    path('snippets/copy/<int:snippet_pk>/', core_views.copy_snippet, name='copy_snippet'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
