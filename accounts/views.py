from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request, user)
           messages.success(request, 'You are now logged in')
           return redirect('dashboard')
       else:
           messages.error(request, 'Invalid credentials')
           return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
       
       #Get form value
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

        #Check if Passwords match
       if password == password2:
         #Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
            #Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The Email has already been used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email, last_name=last_name)
                    #login after registration
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')
                    
                    #redirect to login page after register
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')

       else:
            messages.error(request, 'Passwords does not match')
            return redirect('register')

    #Register User
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_time').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)