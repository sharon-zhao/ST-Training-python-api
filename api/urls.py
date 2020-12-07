from django.urls import path
from django.conf.urls import url
from .views.application_views import Applications, ApplicationDetail
from .views.course_display_views import CourseDisplays, CourseDisplayDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.course_display_views import CourseDisplays


urlpatterns = [
    path('applications/', Applications.as_view(), name='applications'),
    path('applications/<int:pk>', ApplicationDetail.as_view(), name='application_detail'),
    path('course_display/', CourseDisplays.as_view(), name='course_display'),
    path('course_display/<int:pk>/', CourseDisplayDetail.as_view(), name='mycourse_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('my-course/', CourseDisplays.as_view(), name='course-display')
]
