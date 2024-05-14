from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import *
from .models import *
from .form_x import *
from django.contrib.auth import login
import django.contrib.auth.views as log_y
from django.contrib.auth.decorators import login_required
from django.views.generic.base import *
from django.views.generic import *
from django.urls import *
from .links import *
from .Extra_action1 import *

from django.db.models import Q
# Create your views here.


class Logging_into(log_y.LoginView):
    template_name='registration/login.html'
    def get_context_data(self, **kwargs):
        context = super(Logging_into, self).get_context_data(**kwargs)
        print("\ncalling Logging_IN class \n")
        return context


class Logging_out(log_y.LogoutView):
    template_name='registration/logout.html'
    def get_context_data(self, **kwargs):
        context = super(Logging_out, self).get_context_data(**kwargs)
        print("\ncalling Logging_OUT class \n")
        return context




class Menu(TemplateView):
    
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        print("MENU AREA")
        mark_list=Mark_model.objects.all()
        print("marks\n"+str(mark_list))
        if self.request.user.is_authenticated:
            try:
             context['profile_x']=User_model.objects.get(user_of=self.request.user.pk)
             print("\nUser profile model "+str(context['profile_x'])+"\n")
            except User_model.DoesNotExist:
                print("\nUser profile dose not exisit\n")
                context['profile_x']="NOT EXISIT"
                context['add_user/profile_for_'+str(self.request.user.username)+'/user']="NOT EXISIT"
                return redirect("logout")
        else:
            print("No user found")

        return context


class Add_user_page(CreateView):
    
    template_name='registration/add_user.html'
    form_class=Make_user_form
    model=User
    #success_url='add_user/profile_for_<str:user_x>/make_profile'
    def get_context_data(self, **kwargs):
        context = super(Add_user_page, self).get_context_data(**kwargs)
        
        print("ADD USER AREA "+str(self.request.user.username))
        self.success_url='add_user/profile_for_'+str(self.request.user.username)+'/make_profile'
        print("\n"+str(self.success_url)+"\n")
        return context
    def get_success_url(self):
        user_of= User.objects.last()
        login(self.request,user_of )
        print("\nadd_user/profile_for_"+str(user_of)+"/make_profile\n")
        return f'add_user/profile_for_'+str(user_of)+'/make_profile'
     
    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            print("\nSOMETHING WRONG.... in user making phase\n")
            return False
        # Custom Logic
        print("\nthe user "+str(self.request.user.username)+"\n")
        return redirect()
    
    
    


class Make_profile_page(CreateView):
    
    template_name='user_profile/make_model.html'
    form_class=Make_profile_form
    model=User_model
    #success_url=User_model.get_absolute_url
    def get_context_data(self, **kwargs):
        context = super(Make_profile_page, self).get_context_data(**kwargs)
        
        context['profile_owner']=self.kwargs['user_x']
        print(f"\nmaking a profile for user "+str(context['profile_owner'])+"\n")
        return context
    
    '''def save(self, *args, **kwargs):
       if self.request.user.is_authenticated:
         user_key=User.objects.get(username=self.request.user.username)
         self.request['user_of']=user_key
       
         return super().post(self.request,*args, **kwargs) # Call the real save() method'''
    
    def form_valid(self, form: Make_profile_form):
        user_x=self.request.user
        form.instance.user_of=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Make_profile_page,self).form_valid(form)
    
    


    def get_success_url(self):
        user_key= self.kwargs['user_x']
        profile_x=User_model.objects.get(user_of=self.request.user.pk)
        if profile_x.profile_activity ==User_activity[0][0]:
         print("PROFESSION 0:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"/add_marks_that_you_own\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"/add_marks_that_you_own"
        if profile_x.profile_activity ==User_activity[1][0]:
         print("PROFESSION 1:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)
        if profile_x.profile_activity ==User_activity[2][0]:
         print("PROFESSION 2:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"/add_car_parts\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"/add_car_parts"
        if profile_x.profile_activity ==User_activity[3][0]:
         print("PROFESSION 3:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"_rent\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"_rent"
        if profile_x.profile_activity ==User_activity[4][0]:
         print("PROFESSION 4 PETROL:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"/add_petrol\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"/add_petrol"
        if profile_x.profile_activity ==User_activity[5][0]:
         print("PROFESSION 5:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"_buy\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"_buy"
        if profile_x.profile_activity ==User_activity[6][0]:
         print("PROFESSION 6:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"_buy_sell_rent\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"_buy_sell_rent"
        if profile_x.profile_activity ==User_activity[7][0]:
         print("PROFESSION 7:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"/add_a_decore_model\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"/add_a_decore_model"
        if profile_x.profile_activity ==User_activity[8][0]:
         print("PROFESSION 8:"+str(profile_x.profile_activity))
         print("\nCALLED URL:/add_user/profile_for_"+str(self.request.user.username)+"/user"+str(self.request.user.pk)+"_"+str(self.request.user.username)+"/name_of/"+str(profile_x.name)+"/add_train_center\n")
         return f'add_user/profile_for_'+str(self.request.user.username)+'/user'+str(self.request.user.pk)+'_'+str(self.request.user.username)+'/name_of/'+str(profile_x.name)+"/add_marks_that_you_own"+str(profile_x.name)+"/add_train_center"
    

    
    
    
@login_required
def display_profile(h,u_key,username,profile_name):
    print("display User profile of"+str(username)+" with a key of "+str(profile_name)+"\n")
    the_x_user=User.objects.get(username=username)
    the_x_profile=User_model.objects.get(user_of=u_key)
    return render(h,"user_profile/display_model.html",{'add_user/profile_for_'+str(self.request.user.username)+'/user':the_x_user,'user_profile':the_x_profile})


@login_required
def user_profile(h,u_key,username,profile_name):
    print("from bottom_menu.html display User profile of"+str(username)+" with a key of "+str(profile_name)+"\n")
    the_x_user=User.objects.get(username=username)
    the_x_profile=User_model.objects.get(user_of=u_key)
    return render(h,"bottom_menu.html",{'add_user/profile_for_'+str(self.request.user.username)+'/user':the_x_user,'user_profile':the_x_profile})


def all_marks(h):
    mark_list=Mark_model.objects.all()
    print("your list is \n"+str(mark_list))
    return render(h,"cars/marks.html",{'marks':mark_list})



def mark_models(h,k,mark_name):
    target_mark=Mark_model.objects.get(pk=k)
    target_models=Car_model.objects.filter(family_of=target_mark)
    print("\nExploring models of "+str(target_mark)+" and key model\n")
    return render(h,"cars/list_mark_model.html",{'models_of_mark':target_models,'mark':mark_name})


def model_details(h,k,mark_name,model_name,model_num):
    target_car_model=Car_model.objects.get(pk=model_num)
    print("obtaining Car details")
    return render(h,"cars/list_model_dit.html",{'the_car_model':target_car_model,'model':model_name,'mark':mark_name})





#for the fix center page



def has_a_fix_center(h,user_key,user_name,profile_name):
    return render(h,"user_profile/model_2_fix_center.html")


#for the driving school page

class Add_School_page(CreateView):
    model = School_of_drive
    form_class=Add_School_form
    template_name='learn_center/add_school.html'
    def get_context_data(self, **kwargs):
        context = super(Add_School_page, self).get_context_data(**kwargs)
        get_user=self.kwargs['user_key']
        #get_username=self.kwargs['user_name']
        
        #get_profile=self.kwargs['profile_name']
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\nmakeing a driving school for  user {get_user} profile {get_profile}\n")
        return context
    def get_success_url(self):
        
        get_profile=User_model.objects.get(user_of=self.request.user.pk)
        print(f"\nuser{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}\n")
        return f"user{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}"


def schools_that_I_owne(h,user_key,user_name,profile_name,school_name):
    print("\nOWEND SCHOOLS INCLUDED\n")
    #filter is not for one to one model key
    main_user=User_model.objects.filter(Q(user_of=user_key)|Q(has_school=school_name))
    return render(h,"user_profile/model_5_learn_center.html",{'the_school':main_user})


#for the obtained marks

def add_marks_that_I_deal_with(h,user_key,user_name,profile_name):
    marks_list=Mark_model.objects.all()
    dealed_marks=[]
    print(f"making the selected marks list for user {user_name}:{user_key} profile name {profile_name}.....")
    if h.method=='POST':
        print("post action applied")
        for d in range(len(marks_list)):
            dealed_marks.insert(d,marks_list[d])
            print("\n"+str(marks_list[d])+" inserted\n")

        print(f"\nadding to the dealed list\n{dealed_marks}\n")
        #return redirect()
        
        
    else:
        print("No post action applied")
    return render(h,"mark_owner/select_marks.html",{'all_marks':marks_list,'dealed_marks':dealed_marks})


def view_marks_that_I_deal_with(h,user_key,user_name,profile_name):
    print("\nOWEND MARKS INCLUDED\n")
    return render(h,"user_profile/model_1_mark_owner.html")



#for the obtained parts

class Add_Obtained_Parts_page(CreateView):
    model = Part_model
    form_class=Add_part_item_form
    template_name='car_parts/add_part.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Obtained_Parts_page, self).get_context_data(**kwargs)
        get_user=self.kwargs['user_key']
        #get_username=self.kwargs['user_name']
        #get_profile=self.kwargs['profile_name']
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\nmakeing an obtained parts for  user {get_user} profile {get_profile}\n")
        return context
    def get_success_url(self):
        get_user=self.kwargs['user_key']
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\na driving school was created for {get_user} profile {get_profile}\n")
        return f"user{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}"

def parts_that_i_have(h,user_key,user_name,profile_name):
    print("\nCAR PARTS INCLUDED\n")
    return render(h,"user_profile/model_3_car_parts.html")




#for the Decore parts


class Add_Decore_Parts_page(CreateView):
    model = Decorator_model
    form_class=Add_decore_item_form
    template_name='decore/add_decore.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Decore_Parts_page, self).get_context_data(**kwargs)
        get_user=self.kwargs['user_key']
        #get_username=self.kwargs['user_name']
        #get_profile=self.kwargs['profile_name']
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\nmkeing a Decore parts for  user {get_user} profile {get_profile}\n")
        return context
    def get_success_url(self):
        
        get_user=self.kwargs['user_key']
        get_profile=User_model.objects.get(user_of=get_user)
        return f"user{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}_decore_parts"


def decore_i_have(h,user_key,user_name,profile_name):
    print("\nDECORE CARS INCLUDED\n")
    return render(h,"user_profile/model_4_decore.html",{'x':profile_name})



class Add_Petrol_zone_page(CreateView):
    model = Petrol_area
    form_class=Add_Petrol_form
    template_name='petrol_zone/add_item.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Petrol_zone_page, self).get_context_data(**kwargs)
        get_user=self.kwargs['user_key']
        #get_username=self.kwargs['user_name']
        #get_profile=self.kwargs['profile_name']
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\nmkeing a Decore parts for  user {get_user} profile {get_profile}\n")
        return context
    def get_success_url(self):
        
        get_user=self.kwargs['user_key']
        get_profile=User_model.objects.get(user_of=get_user)
        return f"user{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}_petrol_zone"



def petrol_owned(h,user_key,user_name,profile_name,petrol):
    print("\npetrol station\n")
    return render(h,"user_profile/model_6_petrol.html")




