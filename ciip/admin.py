import logging
from django.contrib import admin
from ciip.models import UserProfile
from django.contrib.auth.models import User
#from django.contrib.auth.admin import UserAdmin

#from django.contrib.auth.models import User



class CiipAdmin(admin.ModelAdmin):
  

    model=UserProfile
    
    fieldsets = [
      
        ('Personal Information', {'fields':['gender','passport','first_name','last_name','passport_number','birth_date_day','birth_date_month','birth_date_year']}),
        ('Contact Information',{'fields':['email','phone','address_line1','address_line2','city','zip_code','country']}),
        ('Academic Information', {'fields':['university','year_of_graduation','degree','average']}),
        ('Motivational Questions', {'fields':['question_1', 'question_2']}),
        ('Status Update',{'fields':['status']}),
        ('CV',{'fields':['file_name','file_cv']}),
        ('Image', {'fields':['image']}),
        ('Skills',{'fields':['skill_1','skill_level_1','skill_2',
            'skill_level_2','skill_3','skill_level_3']}),
        ('Interests',{'fields':['interest_1','interest_2','interest_3']}),
    ]
    #readonly_fields=['gender','first_name','last_name','passport_number','birth_date_day','birth_date_month','birth_date_year','email','phone','address_line1','address_line2','city','zip_code','country']
    readonly_fields=['gender','passport','first_name','last_name','passport_number',
    'birth_date_day','birth_date_month','birth_date_year','email','phone',
    'address_line1','address_line2','city','zip_code','country','university',
    'year_of_graduation','degree','average','question_1', 'question_2','file_name',
    'skill_1','skill_level_1','skill_2','skill_level_2','skill_3','skill_level_3',
    'interest_1','interest_2','interest_3',]
    list_display = ('first_name', 'last_name','status','university','user_email')
    list_filter = ['university', 'status']


    def user_email(self, instance):
        return instance.user.email
    

admin.site.register(UserProfile, CiipAdmin)


#admin.site.unregister(User)

