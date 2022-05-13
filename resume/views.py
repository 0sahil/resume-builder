from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import UserDetails, UserAddress, UserHobby, UserLanguage, UserSkill, UserSocialMediaHandles, UserEducation, UserWorkExp
from .forms import UserDetailsForm


# render the home page
def home(request):
    if request.method == 'GET':

        # check if uname session_id exists or not
        try:
            context = {'users': User.objects.get(
                username=request.session['uname'])}
        except Exception as e:
            print(e, ':', e.__class__)
            context = {}

        return render(request, 'resume_templates/resume1.html', context)

# TODO: Can't access if user is not logged in
# TODO: Do Exception handling


def show_user_filled_resume(request):

    c_user_details = UserDetails.objects.get(
        pk=User.objects.get(username=request.session['uname']).id)
    c_user_skills = UserSkill.objects.filter(u_id=c_user_details)
    c_user_address = UserAddress.objects.get(u_id=c_user_details)
    c_user_work_exp = UserWorkExp.objects.get(u_id=c_user_details)
    c_user_hobbies = UserHobby.objects.filter(u_id=c_user_details)
    c_user_langs = UserLanguage.objects.filter(u_id=c_user_details)
    c_user_social_handles = UserSocialMediaHandles.objects.filter(
        u_id=c_user_details)
    c_user_edu = UserEducation.objects.filter(u_id=c_user_details)

    context = {
        'c_user_details': c_user_details,
        'c_user_skills': c_user_skills,
        'c_user_address': c_user_address,
        'c_user_work_exp': c_user_work_exp,
        'c_user_hobbies': c_user_hobbies,
        'c_user_langs': c_user_langs,
        'c_user_social_handles': c_user_social_handles,
        'c_user_edu': c_user_edu
    }
    return render(request, 'all_resumes/a_1.html', context)


def login(request):
    pass


def after_login():
    curr_user = User.objects.get()
    curr_user_details = UserDetails(
        u_id='get the details from above curr_user', f_name='', l_name='', email_add='')


def profile_details(request):
    if request.method == 'GET':
        # I think it will be done after login only
        curr_user_auth_data = User.objects.get(pk=1)
        # curr_user_details = UserDetails.objects.get(pk='')
        # context = {'user_details': curr_user_details}
        context = {}
        # after it, pre fill the details in the frontend
        return render(request, 'profile-details.html', context)
    elif request.method == 'POST':
        filled_user_details = {}
        filled_user_details['f_name'] = request.POST.get('f_name')
        filled_user_details['m_name'] = request.POST.get('m_name')
        filled_user_details['l_name'] = request.POST.get('l_name')
        filled_user_details['profile_pic'] = request.FILES.get('image')
        filled_user_details['dob'] = request.POST.get('dob')
        filled_user_details['mobile_no'] = request.POST.get('mobile_no')
        filled_user_details['email_add'] = request.POST.get('email_add')
        filled_user_details['job_role'] = request.POST.get('job_role')
        filled_user_details['referal'] = request.POST.get('referal')
        filled_user_details['house_street'] = request.POST.get('house_street')
        filled_user_details['city'] = request.POST.get('city')
        filled_user_details['state'] = request.POST.get('state')
        filled_user_details['country'] = request.POST.get('country')
        filled_user_details['pincode'] = request.POST.get('pincode')
        filled_user_details['skills_list'] = request.POST.getlist('skill')
        filled_user_details['hobby_list'] = request.POST.getlist('hobby')
        filled_user_details['lang_list'] = request.POST.getlist('lang')
        filled_user_details['social_media_list'] = request.POST.getlist(
            'social_media')
        # filled_user_details['user_education_list'] = {'qualification': request.POST.getlist('qualification'), 'e_institution': request.POST.getlist('e_institution'), 'grade': request.POST.getlist('grade')}
        # filled_user_details['user_work_exp_list'] = {'w_role': request.POST.getlist('w_role'), 'w_institution': request.POST.getlist('w_institution'), 'start_date': request.POST.getlist('start_date'), 'end_date': request.POST.getlist('end_date')}

        h_institution = request.POST.get('high_edu')
        h_grade = request.POST.get('high_edu_grade')

        g_institution = request.POST.get('graduation')
        g_grade = request.POST.get('graduation_grade')

        m_institution = request.POST.get('masters')
        m_grade = request.POST.get('masters_grade')

        w_role = request.POST.get('w_role')
        w_institution = request.POST.get('w_institution')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        # check validness of the form here
        # check validness of the data in frontend as well
        if 1:  # if valid data
            curr_user_details = UserDetails(
                u_id=User.objects.get(username=request.session['uname']),
                f_name=filled_user_details['f_name'],
                m_name=filled_user_details['m_name'],
                l_name=filled_user_details['l_name'],
                profile_pic=filled_user_details['profile_pic'],
                dob=filled_user_details['dob'],
                mobile_no=filled_user_details['mobile_no'],
                email_add=filled_user_details['email_add'],
                job_role=filled_user_details['job_role'],
                referal=filled_user_details['referal']
            )
            curr_user_address = UserAddress(
                u_id=UserDetails.objects.get(pk=User.objects.get(
                    username=request.session['uname']).id),
                house_street=filled_user_details['house_street'],
                city=filled_user_details['city'],
                state=filled_user_details['state'],
                country=filled_user_details['country'],
                pincode=filled_user_details['pincode']
            )
            for i in range(len(filled_user_details['skills_list'])):
                # print(skill)
                curr_user_skill = UserSkill(
                    u_id=UserDetails.objects.get(pk=User.objects.get(
                        username=request.session['uname']).id),
                    skill_name=filled_user_details['skills_list'][i]
                )
                curr_user_skill.save()
            for hobby in filled_user_details['hobby_list']:
                curr_user_hobby = UserHobby(
                    u_id=UserDetails.objects.get(pk=User.objects.get(
                        username=request.session['uname']).id),
                    hobby_name=hobby
                )
                curr_user_hobby.save()
            for lang in filled_user_details['lang_list']:
                curr_user_lang = UserLanguage(
                    u_id=UserDetails.objects.get(pk=User.objects.get(
                        username=request.session['uname']).id),
                    lang_name=lang
                )
                curr_user_lang.save()
            for social_media in filled_user_details['social_media_list']:
                curr_user_social_media_handle = UserSocialMediaHandles(
                    u_id=UserDetails.objects.get(pk=User.objects.get(
                        username=request.session['uname']).id),
                    social_media_handle=social_media
                )
                curr_user_social_media_handle.save()

            # custom user education save
            curr_user_edu = UserEducation(
                u_id=UserDetails.objects.get(pk=User.objects.get(
                    username=request.session['uname']).id),
                qualification='Higher Education',
                institution=h_institution,
                grade=h_grade
            )
            curr_user_edu.save()

            curr_user_edu = UserEducation(
                u_id=UserDetails.objects.get(pk=User.objects.get(
                    username=request.session['uname']).id),
                qualification='Graduation',
                institution=g_institution,
                grade=g_grade
            )
            curr_user_edu.save()

            curr_user_edu = UserEducation(
                u_id=UserDetails.objects.get(pk=User.objects.get(
                    username=request.session['uname']).id),
                qualification='Masters',
                institution=m_institution,
                grade=m_grade
            )
            curr_user_edu.save()

            # custom work exp save
            curr_user_work_exp = UserWorkExp(
                u_id=UserDetails.objects.get(pk=User.objects.get(
                    username=request.session['uname']).id),
                role=w_role,
                institution=w_institution,
                start_date=start_date,
                end_date=end_date
            )
            curr_user_work_exp.save()

            curr_user_details.save()
            curr_user_address.save()
            return redirect('res')
        else:
            pass
            # TODO: show the same page with filled data to enter the data again
