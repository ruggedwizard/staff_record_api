from django.urls import path
from base import views

urlpatterns = [
    path('all_staff_records/',views.StaffReocrdAPIView.as_view(), name="all_staff_reocrds")
]