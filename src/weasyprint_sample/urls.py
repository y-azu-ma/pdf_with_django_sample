from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'weasyprint_sample'
urlpatterns = [
    path('', views.index, name='index'),
    path('weasy_test', views.weasy_test, name='weasy_test'),
    # path('sample/', TemplateView.as_view(template_name='weasyprint_sample/test_template.html')),
]