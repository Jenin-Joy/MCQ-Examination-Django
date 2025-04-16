from django.urls import path,include
from Cordinator import views
app_name="Cordinator"
urlpatterns=[

    path('candidateregistration/',views.candidateregistration,name='candidateregistration'),
    path('delcan/',views.delcan,name='delcan'),
    path('editcan/',views.editcan,name='editcan'),
    path('home/',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('examinationdetails/',views.examinationdetails,name='examinationdetails'),
    path('startexam/<int:id>',views.startexam,name='startexam'),
    path('delexm/<int:id>',views.delexm,name='delexm'),
    path('addquestions/<int:id>',views.addquestions,name='addquestions'),
    path('delqus/<int:id>/<int:did>',views.delqus,name='delqus'),
    path('addoptions/<int:id>',views.addoptions,name='addoptions'),
    path('delopt/<int:id>/<int:did>',views.delopt,name='delopt'),

    path('completedexam/',views.completedexam,name="completedexam"),
    path('viewresult/<int:id>',views.viewresult,name="viewresult"),
    path('completexam/<int:id>',views.completexam,name="completexam"),
]
