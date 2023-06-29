from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

class StaffRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)