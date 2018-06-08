from registration.backends.simple.views import RegistrationView

# subclass the RegistrationView class to take use to custom location
class MyRegistrationView(RegistrationView):
    # URL we want to redirect to afterregistration
    success_url = 'registration_create_thing'
