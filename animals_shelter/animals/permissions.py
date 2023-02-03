from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to check out if user is Admin
    if he is - return True. Else return False.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsAdminOrAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Permission to check out if user is Authenticated or Admin.
    If he is - return True. Else return False
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_staff:
            return True

        if request.method in ('PUT', 'PATCH') and request.user.is_authenticated:
            return True

        return False
