from registration.backends.simple.views import RegistrationView


#subclass the RegistrationView class to take use to custom location

# in the book:
class MyRegistrationView(RegistrationView):
    # the named URL that we want to redirect to after
    # successful registration
    success_url = 'registration_create_thing'


# # from the github
# class MyRegistrationView(RegistrationView):
#     def get_success_url():
#         # the named URL that we want to redirect to after
#         # successful registration
#         return 'registration_create_thing'
