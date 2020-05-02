from rest_framework.permissions import BasePermission


class IsAuthOrNotPremium(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous and obj.premium:
            return False
        else:
            return True
