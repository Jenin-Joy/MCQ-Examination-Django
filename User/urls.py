from django.urls import path,include
from User import views

app_name="User"
urlpatterns = [
    path('home/',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),

    path('viewexam/',views.viewexam,name='viewexam'),
    path('viewquestion/<int:id>',views.viewquestion,name='viewquestion'),
    path('ajaxexamanswer/',views.ajaxexamanswer,name='ajaxexamanswer'),
    path('ajaxtimer/',views.ajaxtimer,name='ajaxtimer'),
    path('successer/',views.successer,name='successer'),

    path('viewresult/<int:id>',views.viewresult,name='viewresult'),
]