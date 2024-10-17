from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .form import UserProfileForm


def signup(request):
        if request.method == "POST":
               fullname = request.POST['fullname']
               username = request.POST['username']
               email = request.POST['email']
               password = request.POST['password']
               password1 = request.POST['password1']
               dob = request.POST['dob']
               phone = request.POST['phone']
               city = request.POST['city']
               bio = request.POST['bio']
               
               

               if User.objects.filter(username=username).exists():
                       messages.error(request, "Username is Already Exists!!")
                       return redirect(signup)
               
               elif User.objects.filter(email=email).exists():
                       messages.error(request, "Email is Already Exists!!")
                       return redirect(signup)
               
               else:
                       if password == password1:
                               user =  User.objects.create_user(
                                     username=username, 
                                     email=email, 
                                     password=password,
                                     first_name=fullname
                                )
                               user.save()

                               UserProfile.objects.create(
                                     user=user,
                                     phone=phone,
                                     bio=bio,
                                     dob=dob,
                                     city=city
                               )
                               messages.success(request, "Account Created Successfully!!")
                               return redirect(signin)
                       
                       else:
                               messages.error(request, "Password Not Matched!!")

                               return redirect(signup)

                                


        else:
                return render(request, 'signup.html')

def signin(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']

                user = authenticate(request, username=username, password=password)

                if user is not None:
                        login(request, user)
                        messages.success(request, f'Hello {username}')
                        return redirect('home')
                
                else:
                        messages.info(request, "Create Your Account!!")
                        return render(request, 'signin.html')
        else:
                
                return render(request, 'signin.html')

def signout(request):
        logout(request)
        # messages.success(request, 'You have successfully logged out.')
       # return redirect('signin')

        return render(request, 'signout.html')



@login_required
def user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None  # Or handle it however you prefer

    return render(request, 'user_profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile does not exist
        return redirect('signup')  # Redirect to a profile creation page or show an error

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})
