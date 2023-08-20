from django.contrib import admin
from myapp.models import Suggest
from myapp.models import MenuItem
from myapp.models import Feedback
# Register your models here.
admin.site.register(Suggest)
admin.site.register(Feedback)
admin.site.register(MenuItem)
