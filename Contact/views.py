from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    return render(request, 'contact.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Sending email
        try:
            send_mail(
                f'Message from {name}',
                message,
                'harshitveram2004@gmail.com',  # Replace with your email
                [email],  # Recipient's email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent!')
            return redirect('home')  # Redirect to a success page
        except Exception as e:
            messages.error(request, f'Error sending message: {str(e)}')
    
    return render(request, 'contact.html')
