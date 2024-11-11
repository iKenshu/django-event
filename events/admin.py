import csv

from django.contrib import admin
from django.http import HttpResponse

from .admin_filters import (
    EventDateFilter,
    CategoryFilter,
    ReservationNameFilter,
    ReservationEmailFilter,
    SpeakerFilter,
    EventFilter,
)
from .models import Event, Category, Speaker, Attendee, Reservation


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin for the Event model
    """

    list_display = ("name", "date", "description", "category")
    search_fields = ("name", "date", "speaker__name", "category__name")
    list_filter = (CategoryFilter, EventDateFilter, SpeakerFilter)
    actions = ["export_to_csv"]

    @admin.action(description="Export to CSV")
    def export_to_csv(self, request, queryset):
        """
        Export events to CSV
        """
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="events.csv"'
        writer = csv.writer(response)
        writer.writerow(["Name", "Date", "Description", "Category"])
        for event in queryset:
            writer.writerow(
                [event.name, event.date, event.description, event.category]
            )
        return response


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin for the Category model
    """

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    """
    Admin for the Speaker model
    """

    list_display = ("name", "bio")
    search_fields = ("name",)
    list_filter = (EventFilter,)


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    """
    Admin for the Attendee model
    """

    list_display = ("name", "email")
    search_fields = ("name", "email")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Admin for the Reservation model
    """

    list_display = ("event", "attendee", "category")
    search_fields = ("event__name", "attendee__email", "category__name")
    list_filter = (
        CategoryFilter,
        ReservationNameFilter,
        ReservationEmailFilter,
    )
    actions = ["export_to_csv"]

    @admin.action(description="Export to CSV")
    def export_to_csv(self, request, queryset):
        """
        Export reservations to CSV
        """
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="reservations.csv"'
        )
        writer = csv.writer(response)
        writer.writerow(["Event", "Attendee", "Category"])
        for reservation in queryset:
            writer.writerow(
                [
                    reservation.event.name,
                    reservation.attendee.email,
                    reservation.category,
                ]
            )
        return response
