from django.contrib import admin

from ecommerce.models import *

admin.site.register([Ticket, Order])
