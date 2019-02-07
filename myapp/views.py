from django.shortcuts import render,redirect
from myapp.models import UserProfile

#user authentication modules
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='signin')
def home(request):
	profile = UserProfile.objects.get(user=request.user)
	context = {'role':profile.role,'name':profile.user.username}
	return render(request,"myapp/home.html",context)


@login_required(login_url='signin')
def users(request,role):
	profle = UserProfile.objects.get(user=request.user)
	context = {'users':None,'role':profile.role}
	if user.role == 'student' and role != 'student':
		return redirect('users',role='student')
	else:
		user_list = UserProfile.objects.filter(role=role)
		context['users']=user_list
	return render(request,"myapp/users.html",context)


def signin(request):
	context = {}
	if request.method=='POST':
		email = request.POST.get('email',None)
		password = request.POST.get('password',None)
		user = User.objects.filter(email=email).first()
		if user:
			auth = authenticate(request,username=user.username,email=user.email, password=password)
			if auth:
				login(request,user)
				return redirect('home')
		context={'error':True,'email':email,'password':password}
	return render(request,"myapp/signin.html",context)


def signup(request):
	context = {}
	if request.method=='POST':
		email = request.POST.get('email',None)
		name = request.POST.get('username',None)
		password = request.POST.get('password',None)
		role = request.POST.get('role',None).lower()
		if User.objects.filter(email=email).exists():
			context.update({'email_exists':True})
			return render(request,"myapp/signup.html",context)
		if User.objects.filter(username=name).exists():
			context.update({'user_exists':True})
			return render(request,"myapp/signup.html",context)
		if email and name and password and role:
			user = User.objects.create_user(username=name,email=email,password=password)
			profile = UserProfile(user=user,role=role)
			profile.save()
			login(request,user)
			return redirect('home')
		context={'missing_info':True}
	return render(request,"myapp/signup.html",context)




def google_signup(request):
	context = {}
	if request.method == 'GET':
		email = request.GET.get('email')
		name = request.GET.get('name')
		context.update({'name':name,'email':email})
	if request.method=='POST':
		email = request.POST.get('email',None)
		name = request.POST.get('username',None)
		password = request.POST.get('password',None)
		role = request.POST.get('role',None).lower()
		if User.objects.filter(email=email).exists():
			context.update({'email_exists':True})
			return render(request,"myapp/google-signup.html",context)
		if User.objects.filter(username=name).exists():
			context.update({'user_exists':True})
			return render(request,"myapp/google-signup.html",context)
		if email and name and password and role:
			user = User.objects.create_user(username=name,email=email,password=password)
			profile = UserProfile(user=user,role=role)
			profile.save()
			login(request,user)
			return redirect('home')
		context={'missing_info':True}
	return render(request,"myapp/google-signup.html",context)




@login_required(login_url='signin')
def logout_user(request):
	logout(request)
	return redirect("signin")


def form(request):
	return redirect('home')
