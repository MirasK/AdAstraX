from django.urls import path
from .views import (
    PostListView,
    CalendarView
    )

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('calendar', CalendarView.as_view(), name='calendar')
]