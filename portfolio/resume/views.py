from django.shortcuts import render, redirect
from django.core.mail import send_mail
# import settings
from django.conf import settings
from .models import contact
# Create your views here.

def base(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')


def Contact(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save in database
        Contact=contact(name=name, email=email, subject=subject, message=message)
        Contact.save()

        # Send "Thank you" email to the user
        thank_you_subject = "Thank you for contacting me"
        thank_you_message = f"Hi {name},\n\nThank you for reaching out to us! I've received your message and will get back to you soon.\n\nBest regards,\nAnupam yadav"

        try:
            send_mail(
                thank_you_subject,
                thank_you_message,
                settings.DEFAULT_FROM_MAIL,  # From your Mailjet verified sender
                [email],  # To the user's email
                fail_silently=True,
            )
            status_message = "Your message has been sent. A confirmation email has been sent to you."
        except Exception as e:
            status_message = f"Message saved, but failed to send confirmation email: {e}"
        print(status_message)
        return render(request, 'thankyou.html', {'message': status_message})

    return render(request, 'contact.html')
