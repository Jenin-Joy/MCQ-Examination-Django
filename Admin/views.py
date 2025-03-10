from Admin.models import *
from django.shortcuts import render,redirect
def add(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        c=a+b
        return render(request,'Admin/Add.html',{'result':c})
    else :
        return render(request,'Admin/Add.html')
def largest(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        if a>b:
            return render(request,'Admin/Add.html',{'result':a})
        else :
            return render(request,'Admin/Add.html',{'result':b})
    else :
        return render(request,'Admin/Largest.html')
def calculator(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        btn=request.POST.get("btn")
        if btn=='+':
            c=a+b
            return render(request,'Admin/Calculator.html',{'result':c})
        elif btn=='-':
            c=a-b
            return render(request,'Admin/Calculator.html',{'result':c})
        elif btn=='*':
            c=a*b
            return render(request,'Admin/Calculator.html',{'result':c})
        elif btn=='/':
            c=a/b
            return render(request,'Admin/Calculator.html',{'result':c})
    else :
        return render(request,'Admin/Calculator.html')

def district(request):
    dist=tbl_district.objects.all()
    if  request.method=="POST":
        district=request.POST.get("dis")
        tbl_district.objects.create(district_name=district)
        return render(request,'Admin/District.html',{'dis':dist})
    else:
        return render(request,'Admin/District.html')

def category(request):
    cate=tbl_category.objects.all()
    if  request.method=="POST":
        category=request.POST.get("cat")
        tbl_category.objects.create(category_name=category)
        return render(request,'Admin/Category.html',{'cat':cate})
    else:
        return render(request,'Admin/Category.html',{'cat':cate})        
       
def adminreg(request):
    rege=tbl_admin.objects.all()
    if  request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pswd")
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_pswd=password)
        return render(request,'Admin/AdminReg.html',{'reg':rege})
    else:
        return render(request,'Admin/AdminReg.html',{'reg':rege})

def deladmin(request,id): 
    tbl_admin.objects.get(id=id).delete()
    return redirect("Admin:adminreg")
def delcate(request,id): 
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category")  
def place(request):
    dis=tbl_district.objects.all()
    return render(request,'Admin/Place.html',{'result':dis})

def delsubcate(request,id): 
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory") 
      
def brand(request):
    cate=tbl_brand.objects.all()
    if  request.method=="POST":
        brand=request.POST.get("bran")
        tbl_brand.objects.create(brand_name=brand)
        return render(request,'Admin/Brand.html',{'result':cate})
    else:
        return render(request,'Admin/Brand.html',{'result':cate})   

def delbran(request,id): 
    tbl_brand.objects.get(id=id).delete()
    return redirect("Admin:brand")   
def editbran(request,id): 
    brand=tbl_brand.objects.get(id=id)
    brand1=tbl_brand.objects.all()
    if request.method=="POST":
        brand.brand_name=request.POST.get("bran")  
        brand.save()
        return redirect("Admin:brand")   
    else:
        return render(request,'Admin/Brand.html',{'r':brand,'result':brand1}) 

def editsub(request,id): 
    subcategory=tbl_subcategory.objects.get(id=id)
    category=tbl_category.objects.all()
    if request.method=="POST":
        subcategory.subcategory_name=request.POST.get("subcat")  
        subcategory.save()
        return redirect("Admin:subcategory")   
    else:
        return render(request,'Admin/Subcategory.html',{'r':subcategory,'result':category}) 
def place(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("District"))
        tbl_place.objects.create(place_name=request.POST.get("place"),district=dist) 
        return redirect("Admin:place")
    else:
        return render(request,"Admin/Place.html",{'result':district,'dis':place})

def subcategory(request):
    c=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        cate=tbl_category.objects.get(id=request.POST.get("cat"))
        tbl_subcategory.objects.create(subcategory_name=request.POST.get("subcat"),category=cate) 
        return redirect("Admin:subcategory")
    else:
        return render(request,"Admin/Subcategory.html",{'result':c,'subcat':subcategory})



      



# Create your views here.
