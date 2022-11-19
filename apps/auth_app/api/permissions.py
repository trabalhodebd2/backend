from rest_framework import permissions


class ChangePasswordPermission(permissions.BasePermission):
    """
    Permissao para alterar senha de usuarios.
    Somente os donos das contas (ou DIRETORES/ADMINISTRADORES) podem mudar senhas de usuarios
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        is_authenticated = bool(request.user and request.user.is_authenticated)

        if request.method == "POST":
            return not is_authenticated

        return is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj or user.is_superuser
