
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from  django.contrib import messages
from .models import Blog
from .forms import EditBlogForm
#from.forms import EditBlog

def home(request):
    blog = Blog.objects.all()
    
    return render(request ,"app/home.html"  , {'blog':blog})

def register(request):

    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'User Created')
                return redirect('login')


        else:
            messages.info(request,'Password Not Matching')
            return redirect('register')
    else:
        return render(request, 'app/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'app/login.html')

def logout(request):
    auth.logout(request)
    return redirect('register')

    
def blog(request):
    if request.method =="POST": # suppose data apn send krt ahot
        title =request.POST.get('title') # to receive title data get('name)
        content =request.POST.get('content')
        
        blog = Blog(title = title, content= content)# 1st title related to model nd 2nd is above title
        blog.save()
        messages.success(request,"post has been submited successfully")
        return redirect('blog') # blog is url
    return render(request , "app/blog.html")

def BlogDetail(request , id):
    blog =Blog.objects.get(id=id) # get use whene we have only one value ie unique value
    return render(request , "app/detail.html",{'blog':blog})


def delete(request,id):
    blog= Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,'post has been deleted')
    return redirect('/')

def edit(request, id):
    blog= Blog.objects.get(id=id)
    if request.method == 'POST':
        form = EditBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            
            return render(request, 'app/edit.html')  
        else:
            form = EditBlogForm(instance=blog)
    else:
        form = EditBlogForm(instance=blog)
    return render(request, 'app/edit.html', {'form':form, 'blog':blog})

