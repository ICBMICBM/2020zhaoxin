from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class filter(MiddlewareMixin):
    def process_request(self, request):
        if not (request.path.startswith('/chall/random') or request.path.startswith('/chall/check')):
            print("request path is" + request.path)
            allowed = ['/api/user/login', '/login', '/api/user/register', '/register','/index','static']
            flag = False
            for path in allowed:
                if request.path.startswith(path):
                    print(path)
                    flag = True
            if request.session.get('email') is None and not flag:
                print("redirecting {} to /index".format(request.path))
                return redirect('/index')
            else:
                pass
