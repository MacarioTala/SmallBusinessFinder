from functools import wraps
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

def is_owner_permission_required(model, name='pk'):
    def decorator(view, func):
        def wrap(request, *args,**kwargs):
            pk=kwargs.get(pk_name,none)
            if pk is None:
                raise RuntimeError('no primary key')
            is_owner_func = getattr(model, 'is_owner',none)
            if is_owner_func is None:
                raise RuntimeError('is_owner must be implemented by model {}'.format(model))
            o=model.objects.get(pk=pk)
            if o.is_owner(request.user):
                return view_func(request, *args,**kwargs)
            else:
                raise PermissionDenied
            return wraps(view_func)(wrap)
        return decorator