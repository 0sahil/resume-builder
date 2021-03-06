# Generated by Django 4.0.2 on 2022-04-11 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllResume',
            fields=[
                ('t_id', models.IntegerField(primary_key=True, serialize=False)),
                ('template', models.FileField(upload_to='')),
                ('base_template_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('u_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('f_name', models.CharField(max_length=30)),
                ('m_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('dob', models.DateField()),
                ('mobile_no', models.CharField(max_length=10)),
                ('email_add', models.EmailField(max_length=254)),
                ('job_role', models.CharField(max_length=20)),
                ('referal', models.CharField(max_length=20)),
                ('social_media_handles', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('u_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='resume.userdetails')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserWorkExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialMediaHandles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media_handle', models.CharField(max_length=50)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='resume.allresume')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=50)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserHobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby_name', models.CharField(max_length=50)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeTemplateList',
            fields=[
                ('t_id', models.IntegerField(primary_key=True, serialize=False)),
                ('template', models.FileField(upload_to='')),
                ('u_id', models.ManyToManyField(to='resume.UserDetails')),
            ],
        ),
    ]
