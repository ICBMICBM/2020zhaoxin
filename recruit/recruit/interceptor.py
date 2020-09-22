from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class filter(MiddlewareMixin):
    def process_request(self, request):
        allowed = ['/api/user/login', '/login', '/api/user/register', '/register','/index']
        flag = False
        for path in allowed:
            if request.path.startswith(path):
                flag = True
        if not flag and request.session.get('email') is None:
            print("redirecting {} to /index".format(request.path))
            return redirect('/index')
