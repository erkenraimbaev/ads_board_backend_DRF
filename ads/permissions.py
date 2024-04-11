from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = 'Вы не являетесь модератором!'

    def has_permission(self, request, view):
        if request.user.groups.filter(name='admin').exists():
            return True
        return False


class IsAuthor(BasePermission):
    message = 'Вы не являетесь автором!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False
