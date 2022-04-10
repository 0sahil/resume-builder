from dataclasses import fields
from django.forms import ModelForm
import models

class UserDetailsForm(ModelForm):
    class Meta:
        model = models.UserDetails
        exclude = ['u_id']

class UserAddressForm(ModelForm):
    class Meta:
        model = models.UserAddress
        exclude = ['u_id']

# class UserSkillForm(ModelForm):
#     class Meta:
#         model = models.UserSkill
#         exclude = ['u_id']