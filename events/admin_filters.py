"""
This file contains the custom admin filters for the events app
"""

import datetime
from django.contrib.admin import SimpleListFilter

from .models import Event, Reservation, Category, Speaker


class EventDateFilter(SimpleListFilter):
    """
    Filter events by date
    """

    title = "date"
    parameter_name = "date"

    def lookups(self, request, model_admin):
        return [
            ("past", "Past Events"),
            ("today", "Today"),
            ("future", "Future Events"),
        ]

    def queryset(self, request, queryset):
        today = datetime.date.today()

        if self.value() == "past":
            return queryset.filter(date__lt=today)
        if self.value() == "today":
            return queryset.filter(date=today)
        if self.value() == "future":
            return queryset.filter(date__gt=today)

        return queryset


class CategoryFilter(SimpleListFilter):
    """
    Filter events and reservations by category
    """

    title = "category"
    parameter_name = "category"

    def lookups(self, request, model_admin):
        return [
            (category.id, category.name) for category in Category.objects.all()
        ]

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category=category_id)
        return queryset


class ReservationNameFilter(SimpleListFilter):
    """
    Filter reservations by attendee name
    """

    title = "reservation"
    parameter_name = "reservation"

    def lookups(self, request, model_admin):
        return [
            (reservation.id, reservation.attendee.name)
            for reservation in Reservation.objects.all()
        ]

    def queryset(self, request, queryset):
        reservation_id = self.value()
        if reservation_id:
            return queryset.filter(reservation=reservation_id)
        return queryset


class ReservationEmailFilter(SimpleListFilter):
    """
    Filter reservations by attendee email
    """

    title = "reservation"
    parameter_name = "reservation"

    def lookups(self, request, model_admin):
        return [
            (reservation.id, reservation.attendee.email)
            for reservation in Reservation.objects.all()
        ]

    def queryset(self, request, queryset):
        reservation_id = self.value()
        if reservation_id:
            return queryset.filter(reservation=reservation_id)
        return queryset


class SpeakerFilter(SimpleListFilter):
    """
    Filter speakers by event
    """

    title = "speaker"
    parameter_name = "speaker"

    def lookups(self, request, model_admin):
        return [(speaker.id, speaker.name) for speaker in Speaker.objects.all()]

    def queryset(self, request, queryset):
        speaker_id = self.value()
        if speaker_id:
            return queryset.filter(speaker__id=speaker_id)
        return queryset


class EventFilter(SimpleListFilter):
    """
    Filter events by speaker
    """

    title = "event"
    parameter_name = "event"

    def lookups(self, request, model_admin):
        return [(event.id, event.name) for event in Event.objects.all()]

    def queryset(self, request, queryset):
        event_id = self.value()
        if event_id:
            return queryset.filter(event__id=event_id)
        return queryset
