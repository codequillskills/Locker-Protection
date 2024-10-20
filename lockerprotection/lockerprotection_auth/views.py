from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import FileUploadForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@login_required
@csrf_protect
def dashboardPage(request):
    user = request.user
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            fileName = form.cleaned_data.get('fileName')
            description = form.cleaned_data.get('description')
            fileUpload = form.cleaned_data.get('fileUpload')
            if fileUpload:
                models.Data.objects.create(user=user, fileName=fileName, description=description, fileUpload=fileUpload)
            else:
                models.Data.objects.create(user=user, fileName=fileName, description=description)
            return redirect('dashboard')
    else:
        form = FileUploadForm()
    return render(request, 'dashboard.html', {'form': form, 'user': user})

@login_required
@csrf_protect
def viewDataPage(request):
    user = request.user
    user_data = models.Data.objects.filter(user=request.user)
    return render(request, 'viewData.html', {'username': user, 'user_data': user_data})

@login_required
@csrf_protect    
def deleteDataPage(request, dataId):
    data = get_object_or_404(models.Data, id=dataId, user=request.user)
    data.delete()
    return redirect('viewdata')

@csrf_protect
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if password != repassword:
            return redirect('register')
        if User.objects.filter(username=username).exists():
            return redirect('register')
        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
        except Exception as e:
            return redirect('register')
    return render(request, 'register.html')

@csrf_protect
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
@csrf_protect
def logoutPage(request):
    logout(request)
    return redirect('login')
