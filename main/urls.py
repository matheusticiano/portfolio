from django.urls import path
from .views import portfolio

app_name = 'main'

urlpatterns = [
    path('portfolio/', portfolio, name='portfolio'),
]
