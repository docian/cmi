from django.urls import path
from .views import PacientsListView, get_pacient
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacientViewSet,TimeTableViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'pacient', PacientViewSet)
router.register(r'timetable', TimeTableViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pacients/', PacientsListView.as_view()),
    path('pacient_/', get_pacient)
]