from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    blogs = Blog.objects.filter(isApproved=True)
    context={'blogs':blogs}
    return render(request, 'index.html', context)

def validatePost(request):
    blogger = Blogger.objects.get(blogUser=request.user)
    context={}
    if(blogger.userType.userType=='Supervisor'):
        blogs = Blog.objects.filter(isApproved=False)
        context={'blogs':blogs}
        return render(request, 'validatePost.html', context)
    else:
        err='Only Supervisor can validate the posts'
        context={'err':err}
        return render(request, 'validatePost.html', context)
        


def validatePostById(request, id):
    blogs = Blog.objects.get(id=id)
    blogs.isApproved=True
    blogs.save()
    
    return redirect('/validatePost/')

def requestSupervisor(request, id):
    blogger = Blogger.objects.get(blogUser=User.objects.get(id=id))
    sups = SupervisorReqs.objects.all()
    if(blogger not in sups):
        nsup=SupervisorReqs(blogger=blogger)
        nsup.save()
    return redirect('/accounts/accinfo')

def allReqSup(request):
    if(request.user.is_superuser):
        reqs=SupervisorReqs.objects.filter(isSupervisor=False)
        context={'reqs':reqs}
        return render(request, 'supreq.html', context)
    else:
        return redirect('/')


def makesup(request, id):
    if(request.user.is_superuser):
        blogger = Blogger.objects.get(id=SupervisorReqs.objects.get(id=id).blogger.id)
        blogger.userType=UserTag.objects.get(userType='Supervisor')
        blogger.isSupervisor=True;
        blogger.save()
        
        supreq = SupervisorReqs.objects.get(id=id)
        supreq.delete()
        return redirect('/supreq')

def newpost(request):
    if(request.user.is_authenticated):
        if(request.method=='POST'):
            title = request.POST['title']
            content = request.POST['content']
            Blog(author=request.user, blogTitle=title, blogContent=content).save()
            return redirect('/')
        canPost = True
        blogger =  Blogger.objects.get(blogUser=request.user)
        currPosts = (Blog.objects.filter(author=request.user)).count()
        print(blogger.userType.maxPost)
        print(currPosts)
        if(currPosts>blogger.userType.maxPost and blogger.userType.maxPost!=-1):
            canPost=False
        if(canPost):
            return render(request, 'newPost.html')
        else:
            return redirect('/getPremium')
    
    else:
        return redirect('/accounts/login')

def getPremium(request):
    return render(request, 'getPremium.html')