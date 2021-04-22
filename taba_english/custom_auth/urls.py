from django.conf.urls import url
from custom_auth import views
# SET THE NAMESPACE!
app_name = 'custom_auth'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.Registration.as_view(),name='register'),
    url(r'^login/$',views.Login.as_view(),name='login'),
    url(r'^logout/$',views.Logout.as_view(),name='logout'),
    url(r'^is_authenticated/$',views.IsAuthenticated.as_view(),name='is_authenticated')
]