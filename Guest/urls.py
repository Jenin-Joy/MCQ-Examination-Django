from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns=[
 path('login/',views.login,name='login'),
 path('registration/',views.registration,name='registration'),
 path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
 path('cordinatorregistration/',views.cordinatorregistration,name='cordinatorregistration'),

]   