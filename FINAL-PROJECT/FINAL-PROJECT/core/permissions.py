from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # DELETE ONLY for users with True in is_staff
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user.is_staff
        # SAFE METHODS (like GET) will be allowed for all.
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        # SAFE METHODS (like GET) will be allowed for all.
        if request.method in SAFE_METHODS:
            return True
        # CHECKING FOR is_staff BEFORE DELETING
        return request.user.is_staff