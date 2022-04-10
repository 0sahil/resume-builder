from re import template
from django.db import models
from django.conf import settings


# abstractuser vs abstractbaseuser
class UserDetails(models.Model):
    u_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True) 
    # referencing USER table id field, id is pk in USER table django
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    profile_pic = models.ImageField()
    dob = models.DateField()
    mobile_no = models.CharField()
    email_add = models.EmailField()
    job_role = models.CharField(max_length=20)
    referal = models.CharField(max_length=20)
    social_media_handles = models.CharField(max_length=20)

class UserAddress(models.Model):
    u_id = models.OneToOneField(UserDetails, on_delete=models.CASCADE, primary_key=True) 
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    pincode = models.CharField()

class UserSkill(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    skill_name = models.CharField(max_length=50)

class UserHobby(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    hobby_name = models.CharField(max_length=50)

class UserLanguage(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    lang_name = models.CharField(max_length=50)

class UserSocialMediaHandles(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    social_media_handle = models.CharField(max_length=50) # check type url

class UserEducation(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    qualification = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)

class UserWorkExp(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    role = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    # maybe a function here to determine the time worked (end_date - start_date)

class ResumeTemplateList(models.Model):
    t_id = models.IntegerField(primary_key=True) # it shoud be the primary key
    template = models.FileField()
    u_id = models.ManyToManyField(UserDetails) # many to many, favourite scenario

class AllTemplates(models.Model):
    t_id = models.IntegerField(primary_key=True)
    template = models.FileField()
    base_template_id = models.IntegerField() # from ResumeTemplateList

class UserResume(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    t_id = models.OneToOneField(AllTemplates, on_delete=models.CASCADE) # kuch gadbad lag rahi yahan
    # shayad ye one to one nahi hoga