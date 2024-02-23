"""pre_registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from accounts.views import portal, students, advisors

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', portal.home, name='home'),

    path('admin-panel/', include('admin_panel.urls')),

    path('advisor/', include('advisor.urls')),

    path('student/', include('student.urls')),

    path('accounts/signup/', portal.SignUpView.as_view(), name='signup'),

    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),

    path('accounts/signup/advisor/', advisors.AdvisorSignUpView.as_view(), name='advisor_signup'),

    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),

    re_path(r'^accounts/reset/$',
            auth_views.PasswordResetView.as_view(
                template_name='password_reset.html',
                email_template_name='password_reset_email.html',
                subject_template_name='password_reset_subject.txt'
            ),
            name='password_reset'),
    re_path(r'^accounts/reset/done/$',
            auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
            name='password_reset_done'),
    re_path(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
            name='password_reset_confirm'),
    re_path(r'^accounts/reset/complete/$',
            auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
            name='password_reset_complete'),

    re_path(r'^accounts/settings/password/$',
            auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
            name='password_change'),

    re_path(r'^accounts/settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
            name='password_change_done'),

]
