from django.urls import path
from .views import get_recommended_jobs

urlpatterns = [
    path('recommend/', get_recommended_jobs, name='recommend_jobs'),
]
