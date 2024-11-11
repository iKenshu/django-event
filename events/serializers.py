"""
This module contains the serializers for the events app
"""

from rest_framework import serializers

from .models import Event, Category, Speaker, Attendee, Reservation


class SpeakerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Speaker model
    """

    class Meta:
        model = Speaker
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model
    """

    speaker = SpeakerSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "date",
            "description",
            "category",
            "speaker",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model
    """

    class Meta:
        model = Category
        fields = "__all__"


class AttendeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attendee model
    """

    class Meta:
        model = Attendee
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reservation model
    """

    attendee = AttendeeSerializer(read_only=True)
    event = EventSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            "attendee",
            "event",
            "category",
        ]
