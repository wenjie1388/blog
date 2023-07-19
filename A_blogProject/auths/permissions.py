from rest_framework import permissions

# from rest_framework.permissions import AllowAny


class IsAnonymousUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return False
        return True


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    对象级权限仅允许对象的所有者对其进行编辑
    假设模型实例具有`author`属性。
    """

    def has_object_permission(self, request, view, obj):
        # 任何请求都允许读取权限，
        # 所以我们总是允许GET，HEAD或OPTIONS 请求.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
