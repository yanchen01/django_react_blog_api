from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write only permissions are only allowed to author of a post
        return obj.author == request.user