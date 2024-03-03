from django.shortcuts import render, HttpResponseRedirect
from .models import post
from django.contrib import messages
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    posts = post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['disc']
                pst = post(title=title, disc=desc) 
                pst.save()
                messages.success(request, "Post Added Successfully!!! ")
            return HttpResponseRedirect('/blog/dashboard/') 
        else:
            form = PostForm() 
            return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/blog/login')
    
    
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = post.objects.get(pk=id)
            form = PostForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request, "Post Updated Successfully!!! ")
            return HttpResponseRedirect('/blog/dashboard/') 
            
        else:
            data = post.objects.get(pk=id)
            form = PostForm(instance=data)
            return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/blog/login/')


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = post.objects.get(pk=id)
            data.delete()
            messages.success(request, "Post Deleted Successfully!!! ")
            return HttpResponseRedirect('/blog/dashboard')
    else:
        return HttpResponseRedirect('/blog/login')

def dashboard(request):
    if request.user.is_authenticated:
        posts = post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        group = user.groups.all()
        return render(request, 'blog/dashboard.html', 
                    {'posts':posts, 'username':request.user,
                    'full_name':full_name, 'groups':group})
    else:
        messages.info(request, "You Are Not Logged In, please Do Login First!!")
        return HttpResponseRedirect('/blog/login')



def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome {uname} you are logged in successfully" )
                    return HttpResponseRedirect('/blog/dashboard/')
                
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/blog/dashboard/')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            messages.success(request, f"Welcome {uname} you are logged in successfully" )
            user = form.save()  
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/blog/')
    else:
        form = SignUpForm()
        return render(request, 'blog/signup.html', {'form':form})



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/')


# def forgot_pass(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = SetPasswordForm(user=request.user, data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 update_session_auth_hash(request, form.user)
#                 messages.success(request, "Your Password changed Successfully")
#                 return HttpResponseRedirect('/blog/login/')
#         else:
#             form = SetPasswordForm(user=request.user)
#         return render(request, 'blog/forgotpass.html', {'form':form})
#     else:
#         return HttpResponseRedirect('blog/login')