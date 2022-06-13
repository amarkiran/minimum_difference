from django.urls import path
from . import difference

urlpatterns = [
    path('minimum_difference', difference.Minimum_difference.as_view()),

]
data = None
