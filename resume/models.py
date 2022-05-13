from re import template
from django.db import models
from django.conf import settings

# set blank = true for models for required fields


# abstractuser vs abstractbaseuser
class UserDetails(models.Model):
    u_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True) 
    # referencing USER table id field, id is pk in USER table django
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile_img')
    dob = models.DateField(null=True)
    mobile_no = models.CharField(max_length=10)
    email_add = models.EmailField()
    job_role = models.CharField(max_length=20)
    referal = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_details'

class UserAddress(models.Model):
    u_id = models.OneToOneField(UserDetails, on_delete=models.CASCADE, primary_key=True) 
    house_street = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6) # may have to add more fields

    class Meta:
        db_table = 'user_address'
    

class UserSkill(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    skill_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_skill'

class UserHobby(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    hobby_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_hobby'

class UserLanguage(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    lang_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_lang'

class UserSocialMediaHandles(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    social_media_handle = models.CharField(max_length=50) # check type url

    class Meta:
        db_table = 'user_social_media'

class UserEducation(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    qualification = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_education'

class UserWorkExp(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE) 
    role = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    # maybe a function here to determine the time worked (end_date - start_date)

    class Meta:
        db_table = 'user_work_exp'

class ResumeTemplateList(models.Model):
    t_id = models.IntegerField(primary_key=True) # it shoud be the primary key
    template_html = models.FileField()
    template_css = models.FileField()
    template_js = models.FileField()
    u_id = models.ManyToManyField(UserDetails) # many to many, favourite scenario

    class Meta:
        db_table = 'resume_template_list'

class AllResume(models.Model):
    t_id = models.IntegerField(primary_key=True)
    template = models.FileField()
    base_template_id = models.IntegerField() # from ResumeTemplateList

    class Meta:
        db_table = 'all_resume'

class UserResume(models.Model):
    u_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    t_id = models.OneToOneField(AllResume, on_delete=models.CASCADE) # kuch gadbad lag rahi yahan
    # shayad ye one to one nahi hoga

    class Meta:
        db_table = 'user_resume'