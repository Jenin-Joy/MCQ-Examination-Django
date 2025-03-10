from django.shortcuts import render ,redirect
from Cordinator.models import *
from Guest.models import *
from django.http import JsonResponse
from datetime import datetime

def candidateregistration(request):
    if "uid" in request.session:
        reg=tbl_candidate.objects.all()    
        if  request.method=="POST":
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            password=request.POST.get("txt_pswd")
            tbl_candidate.objects.create(candidate_name=name,candidate_email=email,candidate_password=password)
        return render(request,'Cordinator/AddCandidate.html',{'result':reg})
    else:
        return redirect("Guest:login")

def examinationdetails(request):
    if "uid" in request.session:
        exm=tbl_examination.objects.filter(cordinator=request.session['cid'],examination_status=0)
        cordinator=tbl_cordinator.objects.get(id=request.session['cid'])
        if  request.method=="POST":
            name=request.POST.get("txt_name")
            qno=request.POST.get("txt_qno")
            ftime = request.POST.get("txt_ftime")
            ttime = request.POST.get("txt_ttime")

            ftime_obj = datetime.strptime(ftime, "%H:%M")
            ttime_obj = datetime.strptime(ttime, "%H:%M")
            time_diff = ttime_obj - ftime_obj
            total_seconds = time_diff.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            
            time = str(hours) +" hours and "+ str(minutes) +" minutes"
            tbl_examination.objects.create(examination_name=name,examination_mark=qno,examination_qno=qno,examination_time=time,cordinator=cordinator,time=str(time_diff),start_time=ftime)
    
        return render(request,'Cordinator/AddExamination.html',{'result':exm})
    else:
        return redirect("Guest:login")    

def addquestions(request,id):
    if "uid" in request.session:

        que=tbl_questions.objects.filter(examination=id)
        if  request.method=="POST":
            examination=tbl_examination.objects.get(id=id)
            questions=request.POST.get("txt_question")
            tbl_questions.objects.create(question=questions,examination=examination)
        return render(request,'Cordinator/Addquestion.html',{'result':que,'id':id})
    else:
        return redirect("Guest:login") 
from django.shortcuts import render, redirect
from .models import tbl_questions, tbl_options

def addoptions(request, id):
    que = tbl_options.objects.filter(questions=id)
    if request.method == "POST":
        questions = tbl_questions.objects.get(id=id)
        ans = request.POST.get("txt_answer")
        status = request.POST.get("txt_radio") == "True"
        count = tbl_options.objects.filter(questions=questions, status=True).count()
        if status and count > 0:
            return render(request, 'Cordinator/Addoption.html', {
                'msg': "Corrected Answer is already added",
                'result': que,
                'id': id
            })
        else:
            tbl_options.objects.create(
                answer=ans,
                questions=questions,
                status=status
            )
            return redirect("Cordinator:addoptions", id=id)
    else:
        return render(request, 'Cordinator/Addoption.html', {'result': que, 'id': id})





def delcan(request,id): 
    tbl_candidate.objects.get(id=id).delete()
    return redirect("Cordinator:candidateregistration") 

def editcan(request,id): 
    candidate=tbl_candidate.objects.get(id=id)
    candidate1=tbl_candidate.objects.all()
    if request.method=="POST":
        candidate.candidate_name=request.POST.get("txt_name")
        candidate.candidate_name=request.POST.get("txt_email") 
        candidate.candidate_name=request.POST.get("txt_name")     
        candidate.save()
        return redirect("Cordinator:candidateregistration")   
    else:
        return render(request,'Cordinator/AddCandidate.html',{'r':candidate,'result':candidate1}) 

def home(request):
 return render(request,'Cordinator/Homepage.html',{'home':home}) 

def profile(request):
    cordinator=tbl_cordinator.objects.get(id=request.session["cid"])
    return render(request,'Cordinator/Myprofile.html',{'cordinator':cordinator})   

def EditProfile(request):
    b=tbl_cordinator.objects.get(id=request.session['cid'])
    if request.method=="POST":
        b.cordinator_name=request.POST.get("cordinator_name")
        b.cordinator_email=request.POST.get("cordinator_email")
        b.cordinator_contact=request.POST.get("cordinator_contact")
        b.save()
        return render(request,"Cordinator/Myprofile.html",{'cordinator':b})
    else:
        return render(request,"Cordinator/EditProfile.html",{'a':b})  

def delexm(request,id): 
    tbl_examination.objects.get(id=id).delete()
    return redirect("Cordinator:examinationdetails") 

def delqus(request,id,did): 
    tbl_questions.objects.get(id=id).delete()
    return redirect("Cordinator:addquestions",did) 

def delopt(request,id,did): 
    tbl_options.objects.get(id=id).delete()
    return redirect("Cordinator:addoptions",did) 


def completedexam(request):
    exm=tbl_examination.objects.filter(cordinator=request.session['cid'],examination_status__gt=0)
    return render(request,"Cordinator/CompletedExam.html",{"exam":exm})

# Create your views here.
