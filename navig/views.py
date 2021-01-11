from django.shortcuts import render, redirect
from django.http import HttpResponse
from navig.models import Socket, Gitandvsc, Pygame, Submission
from django.contrib import messages
import datetime

# Create your views here.
def navig(request):
    return render(request, 'navigate.html')

def home(request):
    return render(request, 'home.html')

def course(request,course,val):
    crs=course.upper()
    if request.method=='POST':
        count=request.POST.get('count')
        alll=request.POST.get('all')
        if request.POST.get('next'):
            if int(count)!=int(alll):
                return redirect('/'+course+'/'+str(int(val)+1))
            else:
                messages.success(request,"Session Ended!")
        if request.POST.get('back'):
            if int(count)!=1:
                return redirect('/'+course+'/'+str(int(val)-1))
            else:
                messages.success(request,"Cannot go back from first lecture!")

    if course=='socket':
        obj=Socket.objects.get(numb=int(val))
        cc={"crs":crs,"vid":obj.vid,"name1":obj.name1,"file1":obj.file1,"name2":obj.name2,"file2":obj.file2,"all":Socket.objects.count(),"count":val}
        return render(request, 'course.html', cc)

    if course=='gitandvsc':
        obj=Gitandvsc.objects.get(numb=int(val))
        cc={"crs":crs,"vid":obj.vid,"name1":obj.name1,"file1":obj.file1,"all":Gitandvsc.objects.count(),"count":val}
        return render(request, 'course.html', cc)

    if course=='pygame':
        obj=Pygame.objects.get(numb=int(val))
        cc={"crs":crs,"vid":obj.vid,"name1":obj.name1,"file1":obj.file1,"all":Pygame.objects.count(),"count":val}
        return render(request, 'course.html', cc)


def mail(request,option):
    if option=="joining the team" or option=="working with us" or option=="promoting your work" or option=="certifications" or option=="contact":
        if request.method=='POST':
            ied=request.POST.get('ied')
            option=request.POST.get('option')
            date=datetime.datetime.now()
            user=Submission.objects.create(ied=ied,option=option,date=date,did="NO")
            user.save()
            return render(request, 'home.html')
        return render(request, 'mail.html',{'option':option,'optup':option.upper()})
    else:
        return HttpResponse("WHAT?")