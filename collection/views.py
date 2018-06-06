from django.shortcuts import render

# Create your views here.
def index(request):
    # creating some random thing
    number = 6
    thing = "Yakazoopa!"
    # pass it to the view
    return render(request, 'index.html', {
        'number':number,
        'thing':thing,
    })

# This is basically like a getter function if
# a webapp was itself a class
