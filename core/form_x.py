from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Make_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')
        widgets={}

class Make_profile_form(forms.ModelForm):
    class Meta:
        model = User_model
        #'user_of','has_mark','has_model','has_part','has_school','Position_found','name','profile_activity','user_phone','location_branch','rate_lvl'
     
        fields = ('user_of',
                  'has_mark',
                  'has_model',
                  'has_part',
                    'has_petrol',
                    'has_school',
                  'has_deco',
                  'user_img',
                  'name',
                  'profile_activity',
                  'user_phone',
                  'location_branch',
                  'address')
        widgets={
            
            'has_mark':forms.HiddenInput(),
            'has_model':forms.HiddenInput(),
            'has_part':forms.HiddenInput(),
            'has_deco':forms.HiddenInput(),
            'has_petrol':forms.HiddenInput(),
            'has_school':forms.HiddenInput(),
            
#has_school,has_petrol

        }
        exclude = ['user_of']





class Add_School_form(forms.ModelForm):
    class Meta:
        model = School_of_drive
        fields = "__all__"


class Add_part_item_form(forms.ModelForm):
    #NOTE:قطع غيار اساسية ولا أكسسوارت
    class Meta:
        model = Part_model
        fields = "__all__"


class Add_decore_item_form(forms.ModelForm):
    #NOTE:قطع غيار اساسية ولا أكسسوارت
    class Meta:
        model = Decorator_model
        fields = "__all__"



class Add_Petrol_form(forms.ModelForm):
    #NOTE:قطع غيار اساسية ولا أكسسوارت
    class Meta:
        model = Petrol_area
        fields = "__all__"