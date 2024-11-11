"""
This file contains the urls for the events app
"""

from django.urls import path
from rest_framework import routers
from .views import (
    EventViewSet,
    CategoryViewSet,
    SpeakerViewSet,
    AttendeeViewSet,
    ReservationViewSet,
)

router = routers.DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"speakers", SpeakerViewSet)
router.register(r"attendees", AttendeeViewSet)
router.register(r"reservations", ReservationViewSet)

urlpatterns = router.urls
