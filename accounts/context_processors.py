from .views import LoginForm, RegisterForm

def login_form_context(request):
    return {
        'login_form': LoginForm(prefix='modal'),
        'register_form': RegisterForm(prefix='modal')
    }
