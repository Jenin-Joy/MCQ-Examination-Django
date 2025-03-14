from django.shortcuts import render ,redirect
from User.models import *
from Admin.models import *
from Guest.models import *
from Cordinator.models import *
from django.http import JsonResponse
import json
from datetime import time, datetime, timedelta

def home(request):
 return render(request,'User/Homepage.html',{'home':home})

def profile(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    return render(request,'User/Myprofile.html',{'user':user})

def EditProfile(request):
    b=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        b.user_name=request.POST.get("user_name")
        b.user_email=request.POST.get("user_email")
        b.user_contact=request.POST.get("user_contact")
        b.user_address=request.POST.get("user_address")
        if 'user_photo' in request.FILES:  # Handle file upload
            b.user_photo = request.FILES['user_photo']
        b.save()
        return render(request,"User/Myprofile.html",{'user':b})
    else:
        return render(request,"User/EditProfile.html",{'a':b})

def ChangePassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_user.objects.get(id=request.session['uid'])
     olda=b.user_password
     oldb= new=request.POST.get("user_old_pasword")
     new=request.POST.get("user_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.user_password=request.POST.get("re_type_password")
                b.save()
                return redirect("User:profile")
            else:
                return render(request,"User/ChangePassword.html",{'error1':error1})
        else:
            return render(request,"User/ChangePassword.html",{'error2':error2})
     else:
         return render(request,"User/ChangePassword.html")

def viewexam(request):
    exam = tbl_examination.objects.all()
    for i in exam:
        exambodycount = tbl_examinationbody.objects.filter(examination=i.id,user=request.session["uid"],examinationbody_status=1).count()
        if exambodycount > 0:
            i.examstatus = 1
    return render(request,"User/ViewExam.html",{'exam':exam})

def viewquestion(request,id):
    question = tbl_questions.objects.filter(examination=id)
    optioncount = 0
    for i in question:
        count = tbl_options.objects.filter(questions=i.id).count()
        if count > 0:
            optioncount = optioncount + 1
    examcount = tbl_examinationbody.objects.filter(examination=id,user=request.session["uid"]).count()
    if examcount > 0:
        exambodyid = tbl_examinationbody.objects.get(examination=id,user=request.session["uid"])
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})
    else:
        exambodyid = tbl_examinationbody.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),examination=tbl_examination.objects.get(id=id))
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})

def ajaxexamanswer(request):
    exam_answer = request.GET.get('answers')
    answers_dict = json.loads(exam_answer)
    for question_key, option_id in answers_dict.items():
        questionid = question_key.split("_")[1]
        options = tbl_options.objects.get(questions=questionid,status=True)
        if option_id == None:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),correct_answer=tbl_options.objects.get(id=options.id))
        else:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),myanswer=tbl_options.objects.get(id=option_id),correct_answer=tbl_options.objects.get(id=options.id))
    exambody = tbl_examinationbody.objects.get(id=request.GET.get('exambodyid'))
    exambody.examinationbody_status = 1
    exambody.save()
    return JsonResponse({"msg":"Examination Submitted Sucessfully..."})

def ajaxtimer(request):
    exam = tbl_examination.objects.get(id=request.GET.get('exam'))
    timecount = tbl_timmer.objects.filter(exam=exam).count()
    if timecount > 0:
        timer_obj = tbl_timmer.objects.get(exam=exam)
        if timer_obj.timmer > time(0, 0, 0):
            current_datetime = datetime.combine(datetime.today(), timer_obj.timmer)
            new_datetime = current_datetime - timedelta(seconds=1)
            new_time = new_datetime.time()
            timer_obj.timmer = new_time
            timer_obj.save()
            time_str = new_time.strftime("%H:%M:%S")
            return JsonResponse({"msg": time_str,"status":False})
        else:
            exam.examination_status = 2
            exam.save()
            return JsonResponse({"msg": "Time's up","status":True})
    else:
        tbl_timmer.objects.create(exam=exam,timmer=exam.time)
        return JsonResponse({"msg": ""})

def successer(request):
    return render(request,"User/Success.html")

def viewresult(request, id):
    result = tbl_examinationanswers.objects.filter(examinationbody__examination=id,examinationbody__user=request.session["uid"],examinationbody__examinationbody_status=1)
    if result[0].examinationbody.total_marks == 0:
        total = 0
        for i in result:
            if i.myanswer and i.myanswer.id == i.correct_answer.id:
                total += 1
        exambody = tbl_examinationbody.objects.get(examination=id,user=request.session["uid"],examinationbody_status=1)
        exambody.total_marks = total
        exambody.save()
    return render(request,"User/viewResult.html",{"result": result,"question":question,"total":question})