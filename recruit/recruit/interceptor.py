from django.shortcuts import redirect

class filter(object):
    def process_request(self, request):
        allowed = ['/api/user/login', '/login', '/api/user/register', '/register','/index']
        if request.path not in allowed and request.session['email'] is None:
            print("redirecting {} to /index".format(request.path))
            return redirect('/index')
