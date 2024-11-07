from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method in ['PUT', 'PATCH']:
            return request.user.is_authenticated
        return request.method == 'DELETE' and request.user.is_staff