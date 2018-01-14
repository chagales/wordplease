from rest_framework.permissions import BasePermission


class UsersPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario puede ejecutar una acción (GET, POST, PUT o DELETE) sobre la visa `view`
        """
        from users.api import UserDetailAPI

        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == "GET" and isinstance(view, UserDetailAPI):
            return True

        return request.user.is_authenticated and (request.method == "PUT" or request.method == "DELETE")

    def has_object_permission(self, request, view, obj):
        """
        El usuario autenticado (request.user) sólo puede trabajar con el usuario solicitado (obj) si es él mismo o es un administrador
        """
        return request.user == obj or request.user.is_superuser
