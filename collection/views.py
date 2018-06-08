from django.shortcuts import render, redirect
from collection.forms import ThingForm
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

def edit_thing(request, slug):
    # get the object
    thing = Thing.objects.get(slug = slug)
    # set Form (will define soon)
    form_class = ThingForm
    # if we're coming from a submitted form
    if request.method == 'POST':
        # get the data from the submitted forms
        form = form_class(data = request.POST, instance = thing)
        if form.is_valid():
            # save and return
            form.save()
            return redirect('thing_detail',slug = thing.slug)

    else:
        # just make the form
        form = form_class(instance = thing)

    # render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form'  : form
    })
