from django.contrib import admin
from .models import *
# Register your models here.
admin.site.login_template='registration/login.html'
admin.site.logout_template='registration/logout.html'

print("total models :\n"+str(models))
#for m in range(len(list(models))):print("model:"+str(m))

class NameAdmin_1(admin.ModelAdmin):pass

admin.site.register(Mark_model, NameAdmin_1)

class NameAdmin_2(admin.ModelAdmin):pass

admin.site.register(Car_model, NameAdmin_2)


class NameAdmin_3(admin.ModelAdmin):pass

admin.site.register(Part_model, NameAdmin_3)



class NameAdmin_4(admin.ModelAdmin):pass

admin.site.register(School_of_drive, NameAdmin_4)



class NameAdmin_5(admin.ModelAdmin):pass

admin.site.register(Drive_News, NameAdmin_5)


class NameAdmin_6(admin.ModelAdmin):pass

admin.site.register(Decorator_model, NameAdmin_6)



