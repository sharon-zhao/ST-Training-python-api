from django.urls import path
from .views.application_views import Applications, ApplicationDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
	# Restful routing
    path('applications/', Applications.as_view(), name='applications'),
    path('applications/<int:pk>/', ApplicationDetail.as_view(), name='application_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
