from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

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

@login_required
def edit_thing(request, slug):
    # get the object
    thing = Thing.objects.get(slug = slug)
    # verify it's the proper user
    if thing.user != request.user:
        raise Http404
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

# make a class creation for new users to make thier Thing
def create_thing(request):
    # what are we making?
    form_class = ThingForm
    # if we are getting a POST request
    if request.method == 'POST':
        # get data and apply to object
        form = form_class(request.POST)
        if form.is_valid():
            # create object, don't save it yet # could use contructor?
            thing = form.save(commit = False)
            thing.slug = slugify(thing.name)
            # we've set attributes, now save
            thing.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        # just make the form
        form = form_class()
        # return the Thing
        return render(request, 'things/create_thing.html', {
            'form': form,
        })
