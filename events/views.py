"""
This module contains the viewsets for the events app
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Event, Category, Speaker, Attendee, Reservation
from .serializers import (
    EventSerializer,
    CategorySerializer,
    SpeakerSerializer,
    AttendeeSerializer,
    ReservationSerializer,
)


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    ordering = ["date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        date = self.request.query_params.get("date")
        category = self.request.query_params.get("category")
        speaker = self.request.query_params.get("speaker")
        if name:
            queryset = queryset.filter(name__icontains=name)
        if date:
            queryset = queryset.filter(date__eq=date)
        if category:
            queryset = queryset.filter(category__name=category)
        if speaker:
            queryset = queryset.filter(speaker__name=speaker)

        order_by = self.request.query_params.get("order_by")
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SpeakerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows speakers to be viewed or edited.
    """

    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        email = self.request.query_params.get("email")
        if name:
            queryset = queryset.filter(name__icontains=name)
        if email:
            queryset = queryset.filter(email__icontains=email)
        return queryset


class AttendeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attendees to be viewed or edited.
    """

    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        email = self.request.query_params.get("email")
        if name:
            queryset = queryset.filter(name__icontains=name)
        if email:
            queryset = queryset.filter(email__icontains=email)
        return queryset


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservations to be viewed or edited.
    """

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    ordering = ["event__date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        email = self.request.query_params.get("email")
        if name:
            queryset = queryset.filter(attendee__name__icontains=name)
        if email:
            queryset = queryset.filter(attendee__email__icontains=email)

        order_by = self.request.query_params.get("order_by")
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset
