from django.db import models

class UserDetails(models.Model):
    # primary key is user_id
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    profile_pic = models.ImageField()
    dob = models.DateField()
    mobile_no = models.CharField()
    email_add = models.EmailField()
    job_role = models.CharField(max_length=20)
    # skills = models.CharField(max_length=20)
    # hobbies = models.CharField(max_length=20)
    # langs = models.CharField(max_length=20)
    referal = models.CharField(max_length=20)
    social_media_handles = models.CharField(max_length=20)

class UserAddress(models.Model):
    # primary key is user_id
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    pincode = models.CharField()

class UserSkill(models.Model):
    # primary key is user_id
    skill_name = models.CharField(max_length=50)

class UserHobby(models.Model):
    # primary key is user_id
    hobby_name = models.CharField(max_length=50)

class UserLanguage(models.Model):
    # primary key is user_id
    lang_name = models.CharField(max_length=50)

class UserSocialMediaHandles(models.Model):
    # primary key is user_id
    social_media_handle = models.CharField(max_length=50) # check type url

class UserEducation(models.Model):
    # primary key is user_id
    qualification = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)

class UserWorkExp(models.Model):
    # primary key is user_id
    role = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    # maybe a function here to determine the time worked (end_date - start_date)

class TemplateList(models.Model):
    t_id = models.IntegerField() # it shoud be the primary key
    template = models.FileField()

