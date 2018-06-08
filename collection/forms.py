# this is from Django
from django.forms import ModelForm
# this is something we've created for the project
from collection.models import Thing

class ThingForm(ModelForm):
    class Meta:
        # tell it the model we are using
        model = Thing
        # which fields does it inherit?
        fields = ('name', 'description',)
