from django.shortcuts import redirect
from functools import wraps

def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if 'usuario_email' not in request.session:
                return redirect('login')
            if request.session.get('usuario_rol') != required_role:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator