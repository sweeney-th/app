from django.contrib import admin

# Register your models here.

# import and register the Thing class


### Thing class and related

from collection.models import Thing

# create an admin class for it
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    # these are attributes of the Thing
    list_display = ('name', 'description',)
    # auto slug
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Thing, ThingAdmin)
