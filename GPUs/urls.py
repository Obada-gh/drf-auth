from django.urls import path
from .views import GpusListView,GpusDetails



urlpatterns = [
    
    path('',GpusListView.as_view(), name='GPUs_api'), # /api/v1/GPUs
    path('<int:pk>',GpusDetails.as_view(), name='GPUs_details'), #/api/v1/GPUs/<int:pk>


]


