from django.contrib import admin

# Register your models here.
# to import from all we are using *
from  .models import *

admin.site.register(Task)