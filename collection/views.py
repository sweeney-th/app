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
        'form' : form,
    })


# add below your edit_thing view
# add below your edit_thing view
def create_thing(request):
    form_class = ThingForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            thing = form.save(commit=False)
            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)
            # save the object
            thing.save()
            # redirect to our newly created thing
            return redirect('thing_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class()
        return render(request, 'things/create_thing.html', {
                'form': form,
        })

def browse_by_name(request, initial = None):
    # if they asked for something specific give it?
    if initial:
        things = Thing.objects.filter(
        name__istartswith = initial).order_by('name')
    else:
        # or else list by name
        things = Thing.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'things': things,'initial': initial,
})
