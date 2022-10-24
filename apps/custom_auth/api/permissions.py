from rest_framework import permissions


class ChangePasswordPermission(permissions.BasePermission):
    """
    Permissao para alterar senha de usuarios.

    Somente os donos das contas (ou DIRETORES/ADMINISTRADORES) podem mudar senhas de usuarios
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj
