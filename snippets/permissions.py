from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request 
        # 읽기 권한은 어떤 요청에도 허용됨 
        # So we'll always allow GET, HEAD or OPTIONS requests 
        # 따라서, 우리는 언제나 GET, HEAD 혹은 OPTIONS 요청들을 허용함 
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet 
        # 해당 snippet 의 owner 만 작성 권한이 허용됨 
        return obj.owner == request.user