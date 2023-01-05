from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *
from main.models import *

# Create your views here.

def signup(request):
    if(request.method == 'POST'):
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if(pass1==pass2):
            if(not(User.objects.filter(username=uname).exists())):
                user = User.objects.create_user(uname, email, pass1)
                user.save()
                Blogger.objects.create(blogUser=User.objects.get(username=uname), userType=UserTag.objects.get(userType='Standard User'))
                return redirect('/accounts/login/')
            else:
                msg={'err':f'Sorry! The username {uname} is alredy taken, Please try someothing else'}
                return render(request, 'error.html', msg)
        else:
            msg={'err':'The Password Dosen\'t matches'}
            return render(request, 'error.html', msg)
    else:
        context={}
        return render(request, 'signup.html', context)



def login(request):
    if(request.method=='POST'):
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        
        currentUser = auth.authenticate(username=uname, password=pass1)
        if(currentUser is not None):
            # cus=Customer(user=User.objects.get(username=uname))
            # cus.save()
            auth.login(request, currentUser)
            return redirect('/')
        else:
            msg={'err':f'The Username or Password is incorrect'}
            return render(request, 'usererr.html', msg)
        
    context={}
    return render(request, 'login.html', context)



def logout(request):
    auth.logout(request)
    return redirect('/')


def accinfo(request):
    context={}
    if request.user.is_authenticated:
        blogger = Blogger.objects.get(blogUser=User.objects.get(username=request.user))
        btntxt=''
        link='#'
        if(blogger.userType.userType!='Supervisor' and not request.user.is_superuser):
            btntxt='Request for a Supervisor'
            link='requestSupervisor/'+f'{request.user.id}'
        elif(blogger.userType.userType=='Supervisor'):
            btntxt='Allow the blogpost'
            link='validatePost'
        elif(request.user.is_superuser):
            btntxt='Validate Supervisors'
            link='supreq'
        context={'blogger':blogger, 'btntxt':btntxt, 'link':link}
    return render(request, 'accinfo.html', context)