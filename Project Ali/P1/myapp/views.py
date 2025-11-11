from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Apply,WebsiteUser,ContactMessage
from myapp.forms import ContactMessageForm

# @login_required(login_url='login')
def home_view(request):
   
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('country')

        # Save in database
        Apply.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            city=city,
            country=country
        )

        messages.success(request, 'Your information has been submitted successfully!')
        return redirect('home')
    return render(request,'index.html')

def service_view(request):
    return render(request,'service.html')

def about_view(request):
    return render(request,'about.html')




def ContactMessage_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')  # optional thank you page
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if WebsiteUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = WebsiteUser(username=username, email=email)
        user.set_password(password1)
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        try:
            user = WebsiteUser.objects.get(username=username)
        except WebsiteUser.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('login')

        if user.check_password(password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid password.")
            return redirect('login')

    return render(request, 'login.html')



def logout_view(request):
    request.session.flush()  
    messages.success(request, "You have been logged out.")
    return redirect('home')


def UK_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        

        # Save in database
        Apply.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            
        )

        messages.success(request, 'Your information has been submitted successfully!')
        return redirect('home')
    return render(request,'UK.html')
def USA_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        

        # Save in database
        Apply.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            
        )

        messages.success(request, 'Your information has been submitted successfully!')
        return redirect('home')
    return render(request,'USA.html')
def canada_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        

        # Save in database
        Apply.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            
        )

        messages.success(request, 'Your information has been submitted successfully!')
        return redirect('home')
    return render(request,'canada.html')

def austrila_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        

        # Save in database
        Apply.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            
        )

        messages.success(request, 'Your information has been submitted successfully!')
        return redirect('home')
    return render(request,'Austriala.html')
@login_required
def Admissionform(request):
    return render(request,'form.html')
