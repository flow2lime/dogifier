from django.urls import path
from owners.views import OwnerProfilerView, DogProfilerView

urlpatterns = [
    # path('', DogifierView.as_view()),
    path('/owner_profiler', OwnerProfilerView.as_view()),
    path('/dog_profiler', DogProfilerView.as_view()),
]