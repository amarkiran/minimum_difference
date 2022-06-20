from django.urls import path
from . import difference

urlpatterns = [
    path('minimum_difference', difference.arrayValue.as_view()),

]
data = None
