from django.urls import path,include
from Admin import views
app_name="Admin"

urlpatterns = [
   path('add/',views.add,name='add'),
   path('largest/',views.largest,name='largest'),
   path('calculator/',views.calculator,name='calculator'),
   path('district/',views.district,name='district'),
   path('category/',views.category,name='category'),
   path('adminreg/',views.adminreg,name='adminreg'),
   path('deladmin/<int:id>',views.deladmin,name='deladmin'),
   path('delcate/<int:id>',views.delcate,name='delcate'),
   path('place/',views.place,name='place'),
   path('brand/',views.brand,name='brand'),
   path('delbran/<int:id>',views.delbran,name='delbran'),
   path('editbran/<int:id>',views.editbran,name='editbran'),
   path('subcategory/',views.subcategory,name='subcategory'),
   path('delsubcate/<int:id>',views.delsubcate,name='delsubcate'),
   path('editsub/<int:id>',views.editsub,name='editsub')





]
