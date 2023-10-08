from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoles.MODERATOR

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner