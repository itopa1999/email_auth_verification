from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import random
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        verification_code = str(random.randint(100000, 999999))
        mail_subject = 'Token'
        message = render_to_string('login_email_template.html', {
            'token':verification_code ,
        })
        email = EmailMessage(mail_subject, message, to=[request.POST.get('email')])
        email.content_subtype = 'html'
        email.send(fail_silently=False)
        return HttpResponse('verification code for auth sent to your mail box')
    
    return render(request, 'index.html')

    