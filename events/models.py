from django.db import models


class Speaker(models.Model):
    """
    Speaker model
    """

    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category model
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Event(models.Model):
    """
    Event model
    """

    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    speaker = models.ManyToManyField(Speaker, related_name="events")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="events", null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("view_future_events", "Can view future events"),
            ("view_past_events", "Can view past events"),
            ("view_all_events", "Can view all events"),
            ("edit_all_events", "Can edit all events"),
            ("delete_all_events", "Can delete all events"),
        ]


class Attendee(models.Model):
    """
    Attendee model
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """
    Reservation model
    """

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.attendee} - {self.event}"

    class Meta:
        permissions = [
            ("view_future_reservations", "Can view future reservations"),
            ("view_past_reservations", "Can view past reservations"),
            ("view_all_reservations", "Can view all reservations"),
            ("edit_all_reservations", "Can edit all reservations"),
            ("delete_all_reservations", "Can delete all reservations"),
        ]
