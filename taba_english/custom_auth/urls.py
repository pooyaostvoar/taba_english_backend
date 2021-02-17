from django.conf.urls import url
from custom_auth import views
# SET THE NAMESPACE!
app_name = 'custom_auth'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.Registration.as_view(),name='register'),
]