from django.contrib import admin
from django.urls import path, include
from resume import views
from django.conf import settings
from django.conf.urls.static import static


# from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # home page render
    path('accounts/', include('accounts.urls')), # for login/sign up
    path('fill-details/', views.profile_details, name='profile_details'), # fill details of user for resume
    path('show-resume/', views.show_user_filled_resume, name='show_user_filled_resume') # for showung filled user resume
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += urlpatterns('django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}), )