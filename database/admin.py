from django.contrib import admin
from .models import Lista
from .models import Branza
from .models import Branza_sub
from .models import Kraj
from .models import Miasto

@admin.register(Lista)
class DatabaseAdmin(admin.ModelAdmin):
	list_display=('id','nazwa','miasto','branza','sub_branza','wyskosc','szerokosc','logo')
	
@admin.register(Branza)
class DatabaseAdmin(admin.ModelAdmin):
	list_display=('id','branza')

@admin.register(Branza_sub)
class DatabaseAdmin(admin.ModelAdmin):
	list_display=('id','branza_sub')
	
@admin.register(Kraj)
class DatabaseAdmin(admin.ModelAdmin):
	list_display=('id','kraj')
	
@admin.register(Miasto)
class DatabaseAdmin(admin.ModelAdmin):
	list_display=('id','miasto')
	