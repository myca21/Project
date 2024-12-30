from django.urls import path
from .views import StudentCreateView, StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
