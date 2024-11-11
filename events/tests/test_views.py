"""
This file contains the tests for the events app
"""

import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from events.models import Event, Category, Speaker, Attendee, Reservation


class EventViewTest(APITestCase):
    """
    This class contains the tests for the events app
    """

    def setUp(self):
        """
        This method is called before each test
        """
        # Create a user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

        # Create Speakers
        self.category = Category.objects.create(name="Category 0")
        self.speaker1 = Speaker.objects.create(name="Speaker 1")
        self.speaker2 = Speaker.objects.create(name="Speaker 2")

        # Create events
        self.event1 = Event.objects.create(
            name="Event 1",
            date=datetime.datetime.now() + datetime.timedelta(days=1),
            description="Description 1",
            category=self.category,
        )
        self.event2 = Event.objects.create(
            name="Event 2",
            date=datetime.datetime.now() + datetime.timedelta(days=2),
            description="Description 2",
            category=self.category,
        )

        # Create attendees
        self.attendee1 = Attendee.objects.create(
            name="Attendee 1", email="email@example.com"
        )
        self.attendee2 = Attendee.objects.create(
            name="Attendee 2", email="email@example.com"
        )

        # Create categories
        self.category1 = Category.objects.create(name="Category 1")
        self.category2 = Category.objects.create(name="Category 2")

        # Create reservations
        self.reservation1 = Reservation.objects.create(
            event=self.event1, attendee=self.attendee1, category=self.category1
        )
        self.reservation2 = Reservation.objects.create(
            event=self.event2, attendee=self.attendee2, category=self.category2
        )

        self.event1.speaker.set([self.speaker1])
        self.event2.speaker.set([self.speaker2])

    def test_get_events(self):
        """
        This method tests the get events endpoint
        """
        response = self.client.get("/api/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["results"][0]["name"], "Event 1")
        self.assertEqual(response.data["results"][1]["name"], "Event 2")

    def test_post_event(self):
        """
        This method tests the post event endpoint
        """
        response = self.client.post(
            "/api/events/",
            {
                "name": "Event 3",
                "date": "2023-01-01",
                "description": "Description 3",
                "category": self.category.id,
                "speaker": [self.speaker1.id],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_event(self):
        """
        This method tests the delete event endpoint
        """
        response = self.client.delete(f"/api/events/{self.event1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_event(self):
        """
        This method tests the put event endpoint
        """
        response = self.client.put(
            f"/api/events/{self.event1.id}/",
            {
                "name": "Event 3",
                "date": "2023-01-01",
                "description": "Description 3",
                "category": self.category.id,
                "speaker": [self.speaker1.id],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Event 3")

    def test_get_reservations(self):
        """
        This method tests the get reservations endpoint
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/reservations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(
            response.data["results"][0]["event"]["id"], self.event1.id
        )
        self.assertEqual(
            response.data["results"][1]["event"]["id"], self.event2.id
        )

    def test_get_speakers(self):
        """
        This method tests the get speakers endpoint
        """
        response = self.client.get("/api/speakers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["results"][0]["name"], "Speaker 1")
        self.assertEqual(response.data["results"][1]["name"], "Speaker 2")

    def test_get_categories(self):
        """
        This method tests the get categories endpoint
        """
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)
        self.assertEqual(response.data["results"][0]["name"], "Category 0")
        self.assertEqual(response.data["results"][1]["name"], "Category 1")

    def test_post_category(self):
        """
        This method tests the post category endpoint
        """
        response = self.client.post("/api/categories/", {"name": "Category 3"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_attendees(self):
        """
        This method tests the get attendees endpoint
        """
        response = self.client.get("/api/attendees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["results"][0]["name"], "Attendee 1")
        self.assertEqual(response.data["results"][1]["name"], "Attendee 2")

    def test_post_attendee(self):
        """
        This method tests the post attendee endpoint
        """
        response = self.client.post(
            "/api/attendees/",
            {
                "name": "Attendee 3",
                "email": "email@example.com",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
