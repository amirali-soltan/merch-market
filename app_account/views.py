from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from .forms import SignupForm
from django.contrib import messages
from app_market.models import Category
from .forms import UserForm, ProfileForm, AddressForm , ChangePasswordForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Address

def welcomeview(request):
    return render(request,'welcome.html')

def loginview(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    return render(request,'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')

def signupview(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = SignupForm()
    return render(request , 'register.html' , {'form':form})

def profileview(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    context = {
        'category': Category.objects.all(),
        'profile': profile,
    }
    return render(request,'profile.html',context)

@login_required
def profile_editview(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'profile-additional-info.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'category': Category.objects.all() 
    })

@login_required
def profile_address(request):

    if request.method == 'POST':
        if 'delete_address_id' in request.POST: 
            address_id = request.POST.get('delete_address_id')
            address = get_object_or_404(Address, id=address_id, user=request.user)
            address.delete()  
            return redirect('profile_address')
            
        
        else: 
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.user = request.user
                address.save()
                return redirect('profile_address') 
    else:
        form = AddressForm()

    addresses = Address.objects.filter(user=request.user)
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'profile-addresses.html', {
        'form': form,
        'addresses': addresses ,
        'profile': profile,
        'category': Category.objects.all() 
    })

@login_required
def pass_changeview(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)

            messages.success(request, 'رمز عبور با موفقیت تغییر یافت.')
            return redirect('profile')
    else:
        form = ChangePasswordForm(user=request.user)

    return render(request, 'password-change.html', {'form': form})
