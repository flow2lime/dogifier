from django.urls import path
from owners.views import DogifierView

urlpatterns = [
    path('', DogifierView.as_view()),
]