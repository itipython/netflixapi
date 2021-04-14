from django.contrib import admin
from Netflix.models.Show import *
from Netflix.models.Profile import *

# Register your models here.
admin.site.register(Show)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Producer)
admin.site.register(Prize)
admin.site.register(Actor)

admin.site.register(Country)


admin.site.register(Profile)
admin.site.register(Membership)
admin.site.register(Watch)
admin.site.register(WatchLater)
admin.site.register(Watched)