from django.urls import *
from .views import *
from .models import *
from django.contrib.auth import views as log_x

app_name='core'
#url = reverse("core:marks")
urlpatterns = [
      path('login',log_x.LoginView.as_view(template_name='registration/login.html'),name='login'),
      path('logout/',log_x.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
      path('new_user',Add_user_page.as_view(),name='add_user'),
      path('new_user/profile_for_<str:user_x>/make_profile',Make_profile_page.as_view(),name='make_user_profile'),
      path('new_user/profile_for_<str:user_x>/user<int:u_key>_<str:username>/name_of/<str:profile_name>',display_profile,name='view_user_profile'),
      #----------------TEST--------------\
      #path('user<int:user_key>_<str:user_name>/name_of/<str:profile_name>/add_petrol',Add_Petrol_zone_page.as_view(),name='user_add_petrol'),
      
      #http://127.0.0.1:710/user41_Remakun50/name_of/Eltyyar%20Cars/user41_Remakun50/name_of/Remakun50
      #path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:user_name>/name_of/<str:profile_name>/',petrol_owned,name='user_has_petrols'),
      #------------------------------/
      
      # path("user<int:user_key>_<str:user_name>/name_of/<str:profile_name>",has_a_fix_center,name='user_has_fix_center'),
      #------------------------------
      path('new_user/profile_for_<str:user_x>/user<int:u_key>_<str:username>/name_of/<str:profile_name>/add_school',Add_School_page.as_view(),name='user_add_school'),
      path('new_user/profile_for_<str:user_x>/user<int:u_key>_<str:username>/name_of/<str:profile_name>',schools_that_I_owne,name='user_displays_school'),

























      path('',Menu.as_view(),name='home'),
      path('Marks',all_marks,name='marks'),
      path('Marks_of_<int:k>-<str:mark_name>',mark_models,name='mark_item'),
      path('Marks_of_<int:k>-<str:mark_name>/model_name_<str:model_name>:<int:model_num>',model_details,name='dit_item'),
    
]