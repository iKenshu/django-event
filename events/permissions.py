from rest_framework.permissions import BasePermission


class CanViewFutureEvents(BasePermission):
    """
    Permission to view future events
    """

    def has_permission(self, request, view):
        return request.user.has_perm("events.view_future_events")


class CanEditAllEvents(BasePermission):
    """
    Permission to edit all events
    """

    def has_permission(self, request, view):
        return request.user.has_perm("events.edit_all_events")
