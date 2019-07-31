from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('users/<int:pk>', views.RetrieveUpdateUserView.as_view(), name='update'),

]

urlpatterns = format_suffix_patterns(urlpatterns)