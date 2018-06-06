from django.shortcuts import render
from collection.models import Thing

# Create your views here.
def index(request):
    # get all the things objects
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
})

# This is basically like a getter function if
# a webapp was itself a class
def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'things/thing_detail.html', {
    'thing': thing,
})
