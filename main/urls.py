from django.urls import path
from django.views.generic import TemplateView

from main import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.main, name='home' ),
    path('boardList', views.boardList, name='boardList'),
    path('boardView', views.boardView, name='boardView'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]