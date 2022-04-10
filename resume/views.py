from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import UserDetails
from .forms import UserDetailsForm

# Create your views here.

# render the home page
def home(request):
    return render()

class ProfileView(View):
    form_class = UserDetailsForm
    # template_name = 

    def get(self, request, *args, **kwargs):
        curr_user_instance_model = User.objects.get() # get the current user's prefilled details
        form = self.form_class(instance=curr_user_instance_model)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/') # or redirect

        return render(request, self.template_name, {'form': form})

def after_login():
    curr_user = User.objects.get()
    curr_user_details = UserDetails(u_id='get the details from above curr_user', f_name='', l_name='', email_add='')
