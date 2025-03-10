from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("txt_pass")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        cordinatorcount=tbl_cordinator.objects.filter(cordinator_email=email,cordinator_password=password).count()
        if usercount>0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"]=user.id
            return redirect("User:home")
        elif cordinatorcount>0:
            cordinator=tbl_cordinator.objects.get(cordinator_email=email,cordinator_password=password)
            request.session["cid"]=cordinator.id
            return redirect("Cordinator:home")

        else:
            return render(request,'Guest/Login.html')
    else:
         return render(request,'Guest/Login.html')
        
        

def registration(request):
    reg=tbl_user.objects.all()
    district=tbl_district.objects.all()
    if  request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        address=request.POST.get("txt_address")
        password=request.POST.get("txt_pswd")
        # dist=tbl_district.objects.get(id=request.POST.get("District"))
        place=tbl_place.objects.get(id=request.POST.get("sel_Place"))
        photo=request.FILES.get("user_photo")
        tbl_user.objects.create(user_name=name,user_contact=contact,user_email=email,user_address=address,user_password=password,place=place,user_photo=photo)

    return render(request,'Guest/Registration.html',{'result':district})
    # else:
    #     return render(request,'Guest/Registration.html',{'result':district}) 

def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})

def cordinatorregistration(request):
    reg=tbl_cordinator.objects.all()
    if  request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pswd")
        tbl_cordinator.objects.create(cordinator_name=name,cordinator_contact=contact,cordinator_email=email,cordinator_password=password)
    return render(request,'Guest/CordinatorRegistration.html')
        # else:
        #      return render(request,'Guest/CordinatorRegistration.html')





