from django.urls import path
from .views import ClassificationCreateView, ClassificationDeleteView, ClassificationListview, ClassificationUpdateView

urlpatterns = [
    path('', ClassificationListview.as_view(), name='list'),
    path('create/', ClassificationCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ClassificationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ClassificationDeleteView.as_view(), name='delete'),

  
]