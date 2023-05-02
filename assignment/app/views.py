from .models import Client,Work,Artist
from django.shortcuts import render,redirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        username=request.POST['username']
        pass1 = request.POST['pass1']
        pass2= request.POST['pass2']
        print(User.objects.filter(username=username))
        
        if pass1==pass2:
          if User.objects.filter(email=email).exists():
            return redirect('/register')
          elif User.objects.filter(username=username).exists():
            return redirect('/register')
          else:
            user = User.objects.create_user(email=email,username=username,password=pass1)
            user.save();
            return redirect('/',{'messages': messages})
    else:
        return render(request,'register.html')

def work_by_type(request,work_type):
   works = Work.objects.filter(work_type = work_type)
   print(works)
   workObj = Work.objects.values_list('work_type')
   
   payload = {'works' : works , 'work_type' : work_type}
   return render(request , 'workType.html',payload)

def work(request):
   works = Work.objects.order_by().values('work_type').distinct()
   payload = {'works' : works}
   return render(request , 'allWorks.html' , payload)

def search(request):
      query = request.GET.get('query')
      data = Artist.objects.filter(name__icontains=query)
      return render(request , 'search.html' , {'query' : query , 'data' : data})
   